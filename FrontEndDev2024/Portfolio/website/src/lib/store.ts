import { writable } from 'svelte/store';

// Why not use $state?
// IDK how to do some stuff :'''')

// Loading song either from cache or gitlab
export const loading_song = writable(false);

// Other types of loading
export const other_loading = writable(false);

// Store any logs!
class Logger {
	private subscribe: any;
	private set: any;
	private update: any;

	constructor() {
		const { subscribe, set, update } = writable([]);
		this.subscribe = subscribe;
		this.set = set;
		this.update = update;
	}

	send(message: string) {
		this.update((value: string): any => [...value, message]);
	}

	clear() {
		this.set([]);
	}
}
export const logger = new Logger();

// Notification System
export type MessageType = {
	id?: number;
	timeout_ms?: number;
	message?: string;
	dismissable?: boolean;
	type?: 'success' | 'error' | 'warning' | 'info';
};
class Notify {
	private subscribe: any;
	private set: any;
	private update: any;

	constructor() {
		const { subscribe, set, update } = writable([] as MessageType[]);
		this.subscribe = subscribe;
		this.set = set;
		this.update = update;
	}

	send({ message = '', timeout_ms = 3000, dismissable = true, type = 'info' }: MessageType) {
		// Check if dismissable and timeout_ms is exclusive
		if (!dismissable && timeout_ms == 0) {
			console.error('Cannot have dismissable: true and timeout_ms: 0');
			return;
		}

		const id = Math.random();
		this.update((messages: MessageType[]): any => [
			...messages,
			{ id: id, message: message, dismissable, type }
		]);
		if (timeout_ms > 0) {
			setTimeout(() => {
				this.update((messages: MessageType[]): any =>
					messages.filter((element) => element.id != id)
				);
			}, timeout_ms);
		}
	}

	remove(id: number) {
		this.update((messages: MessageType[]): any => messages.filter((element) => element.id != id));
	}
}

export const notify = new Notify();
// Message System END

export const is_mobile = writable(false);
export const has_account = writable(false);
