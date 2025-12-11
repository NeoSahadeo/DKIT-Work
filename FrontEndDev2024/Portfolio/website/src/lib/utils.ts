import { logger } from './store';
import { PROD } from '$lib/shared.svelte';
import { base } from '$app/paths';
import { user_data } from '$lib/shared.svelte';

export function cache_control({
	name,
	method,
	data = ''
}: {
	name: string;
	method: 'set' | 'get' | 'clear' | 'delete';
	data?: string;
}): undefined | string {
	if (method === 'set') window.localStorage.setItem(`oto_${name}`, data);
	if (method === 'delete') window.localStorage.removeItem(`oto_${name}`);
	if (method === 'clear') window.localStorage.clear();
	if (method === 'get') {
		const data = window.localStorage.getItem(`oto_${name}`);
		return data ? data : undefined;
	}
	return undefined;
}

const update_background_gradient = (color: string) => {
	const element = document.getElementById('background_gradient');
	if (element) {
		const red = parseInt(color[1] + color[2], 16);
		const green = parseInt(color[3] + color[4], 16);
		const blue = parseInt(color[5] + color[6], 16);
		const gradient = `linear-gradient(rgba(${red},${green},${blue},0.4660243371598536) 0%, rgba(0, 0, 0, 0.8533871021448501) 100%)`;
		element.style.background = gradient;
	}
};

const toggle_display = (element: HTMLElement | null, display: boolean) => {
	if (element) {
		if (display) {
			element.style.display = 'block';
		} else {
			element.style.display = 'none';
		}
	}
};

const update_background_image = (display: boolean) => {
	const element = document.getElementById('background_image_blur');
	toggle_display(element, display);
};
const update_background_dull = (display: boolean) => {
	const element = document.getElementById('background_darken');
	toggle_display(element, display);
};
const update_background_toggle_gradient = (display: boolean) => {
	const element = document.getElementById('background_gradient');
	toggle_display(element, display);
};

export const update_user_data = (data: any) => {
	// This is for visual updates only
	update_background_gradient(data.preferred_color);
	update_background_toggle_gradient(data.keep_gradient);
	update_background_dull(data.keep_dull);
	update_background_image(data.keep_image);
	//--------------------------------

	user_data.preferred_color = data.preferred_color;
	user_data.keep_image = data.keep_image;
	user_data.keep_dull = data.keep_dull;
	user_data.keep_gradient = data.keep_gradient;
	user_data.ahead = data.ahead;

	cache_control({
		name: 'user_data',
		method: 'set',
		data: JSON.stringify(data)
	});
};

// Load localStorage
export const load_user_data = (): JSON | null => {
	logger.send('Data loaded');
	const data = cache_control({
		name: 'user_data',
		method: 'get'
	});
	if (data) {
		const parsed_data = JSON.parse(data);
		update_user_data(parsed_data);
		return parsed_data;
	}
	return null;
};

export const blob_to_b64 = async (blob: Blob): Promise<Base64URLString> => {
	// Get the array buffer from Blob
	const array_buffer = await blob.arrayBuffer();

	// Create an unsigned 8 bit integer array with the buffer contents
	const u8_array = new Uint8Array(array_buffer);

	// Convert the array to a binary string
	let binary_string = '';
	u8_array.forEach((byte) => {
		binary_string += String.fromCharCode(byte);
	});

	// Return the ASCII/Base64 repr of the string
	return btoa(binary_string);
};

export const b64_to_blob = (b64_string: string, type: string) => {
	// Conver the base64 string back to a binary string
	const binary_string = atob(b64_string);
	const len = binary_string.length;

	// Create an unsigned 8 bit integer array of the size of the string
	const bytes = new Uint8Array(len);

	// Loop through an mutate bytes to the character codes
	for (let x = 0; x < len; ++x) {
		bytes[x] = binary_string.charCodeAt(x);
	}

	return new Blob([bytes], { type: type });
};

// IndexDB

export class DatabaseControl {
	private request: IDBOpenDBRequest;
	private object_store: IDBObjectStore | null;
	private db: IDBDatabase | null;
	public is_open: boolean;
	constructor() {
		this.object_store = null;
		this.db = null;
		this.is_open = false;

		this.request = window.indexedDB.open('OtoDB', 1);

		this.request.onerror = (event: Event) => {
			logger.send('Database open: ' + event.type);
		};

		this.request.onsuccess = (event: Event) => {
			this.db = (event.target as IDBOpenDBRequest).result;
			this.is_open = true;
			logger.send('Database open: ' + event.type);
		};

		this.request.onupgradeneeded = (event: Event) => {
			this.db = (event.target as IDBOpenDBRequest).result;
			if (this.db && !this.db.objectStoreNames.contains('Songs')) {
				logger.send('Creating Object Store: Songs');
				this.object_store = this.db.createObjectStore('Songs', {
					keyPath: 'id',
					autoIncrement: true
				});
				this.object_store.createIndex('name', 'name', { unique: true });
			}
		};
	}
	poll_open(): Promise<boolean> {
		return new Promise((resolve, reject) => {
			const x = setInterval(() => {
				if (this.is_open) {
					clearInterval(x);
					resolve(true);
				}
			}, 100);
		});
	}
	set({ name, data }: { name: string; data: string }) {
		if (!this.db) {
			return null;
		}
		const transaction = this.db.transaction(['Songs'], 'readwrite');
		const object_store = transaction.objectStore('Songs');
		const request = object_store.add({ name, data });

		request.onsuccess = () => {
			logger.send('Song added successfully');
		};

		request.onerror = (event: any) => {
			console.error('Error adding song:', event.target.error);
		};
	}
	get(name: string): Promise<IDBDatabase | null> {
		return new Promise((resolve, reject) => {
			if (!this.db) {
				return null;
			}
			const transaction = this.db.transaction(['Songs'], 'readwrite');
			const object_store = transaction.objectStore('Songs');
			const index = object_store.index('name');

			const request = index.get(name);

			request.onsuccess = (event) => {
				resolve((event.target as IDBOpenDBRequest).result);
			};

			request.onerror = (event) => {
				reject();
			};
		});
	}
}

export const url_resolver = (): string => {
	if (PROD) {
		return 'https://mysql05.comp.dkit.ie/D00264604/oto/'; // This is mysql
	}
	return 'http://localhost:5173/';
};

export const sec_to_min = (seconds: number) => {
	const minutes = Math.floor(seconds / 60);
	const _seconds = Math.ceil(seconds % 60);

	const formatted_min = String(minutes).padStart(2, '0');
	const formatted_sec = String(_seconds).padStart(2, '0');

	return `${formatted_min}:${formatted_sec}`;
};

export const shuffler = (array: any[], type = 'fisher_yates'): any[] => {
	logger.send('Shuffling array');
	if (type === 'fisher_yates') {
		logger.send('Using Fisher Yates');
		let array_length = array.length;

		while (array_length) {
			const random_element = Math.floor(Math.random() * array_length);
			const x = array[array_length - 1];

			array[array_length - 1] = array[random_element];
			array[random_element] = x;

			array_length--;
		}
	}

	return array;
};
