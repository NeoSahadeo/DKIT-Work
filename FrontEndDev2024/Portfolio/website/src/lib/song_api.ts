import { logger } from './store';
import { cache_control, blob_to_b64, b64_to_blob, DatabaseControl } from './utils';

const API_ENDPOINT = 'https://gitlab.com/api/v4/projects/68692926/';
const ACCESS_TOKEN = '';

export const request_songs = async () => {
	logger.send(`Requesting Song Data from Gitlab.`);
	const songs = [];
	let page = 0;

	while (true) {
		logger.send(`Fetching Songs, page: ${page}`);
		const response = await fetch(API_ENDPOINT + `repository/tree?per_page=100&page=${page}`, {
			method: 'get',
			headers: {
				'PRIVATE-TOKEN': ACCESS_TOKEN
			}
		});
		console.log(response);
		if (response.ok) {
			logger.send(`Page Found!`);
			let data = await response.json();
			data = data.map((element: any) => {
				const name = element.name;
				if (name !== '.gitignore') return name;
			});
			songs.push(...data);
			logger.send(`${[...data]}`);
			if (data.length > 0) {
				page++;
			} else {
				logger.send(`Response was ok but the page is empty.`);
				break;
			}
		} else {
			logger.send(`An error with fetching occured. Token might be invalid.`);
			break;
		}
	}

	logger.send(`Caching Data`);
	cache_control({
		name: 'song_list',
		method: 'set',
		data: JSON.stringify(songs)
	});

	return songs;
};

export const search_songs = (query: string) => {
	logger.send('Searching songs');
	logger.send(`Query: ${query}`);
	logger.send('Fetching song list from cache');

	let entries_found = [];
	const song_list = cache_control({
		name: 'song_list',
		method: 'get'
	});

	if (song_list && query.length > 0) {
		const song_list_data = JSON.parse(song_list);
		const reg_query = new RegExp(query, 'ig');

		for (const x in song_list_data) {
			if (song_list_data[x]) {
				const data_found = [...song_list_data[x].matchAll(reg_query)];
				if (data_found.length > 0) {
					entries_found.push(data_found[0].input);
					logger.send(`${entries_found}`);
				}
			}
		}
	}

	return [...new Set(entries_found)];
};

export const fetch_song = async (
	query: string,
	database: DatabaseControl
): Promise<Blob | null> => {
	logger.send('Fetching song data');

	if (!query) {
		return null;
	}

	const encoded_query = encodeURIComponent(query.trim());

	// Load the song from indexDB
	logger.send('Searching Index DB');
	let song_data = await database.get(encoded_query);
	if (song_data) {
		logger.send('Song found');
		const blob = b64_to_blob((song_data as any).data, 'application/octet-stream');
		logger.send('Converting base64 to blob');
		return blob;
	}

	logger.send('Searching Gitlab');
	// if file is not found fetch it from Gitlab
	const response = await fetch(API_ENDPOINT + 'repository/files/' + encoded_query + '/raw', {
		method: 'get',
		headers: {
			'Content-Type': 'application/octet-stream',
			'PRIVATE-TOKEN': ACCESS_TOKEN
		}
	});

	if (response.ok) {
		const blob = await response.blob();
		const data = await blob_to_b64(blob);
		logger.send('Found song, saving blob and return blob');

		database.set({
			name: encoded_query,
			data: data
		});
		return blob;
	} else {
		logger.send('Song not found in either Gitlab and indexDB');
		return null;
	}
};

export const load_song = async (query: string, database: DatabaseControl) => {
	const encoded_query = encodeURIComponent(query.trim());
	logger.send('Loading Song Data');

	// Load the song from indexDB
	let song_data = await database.get(encoded_query);
	if (song_data) {
		logger.send('Converting base64 to blob');
		const blob = b64_to_blob((song_data as any).data, 'application/octet-stream');

		const audio_url = URL.createObjectURL(blob);
		const player = document.getElementById('audio_player') as HTMLAudioElement;
		logger.send('Push to audio element');
		if (player) {
			player.src = audio_url;
			player.volume = 0.03;
		}
	} else {
	}
};

export const next_song = (): string | null => {
	logger.send('Loading next song in queue');
	const player_data = cache_control({
		name: 'player_data',
		method: 'get'
	});

	if (player_data) {
		const player_data_parsed = JSON.parse(player_data);
		if (player_data_parsed.queue_list.length === 0) {
			return null;
		}

		let next_song = null;
		while (next_song === null) {
			next_song = (player_data_parsed.queue_list as string[]).shift();
		}

		logger.send(`Next song: ${next_song}`);

		logger.send('Updating current song');
		player_data_parsed.prev_queue.push(player_data_parsed.current);
		player_data_parsed.current = next_song;

		logger.send('Updating cache');

		cache_control({
			name: 'player_data',
			method: 'set',
			data: JSON.stringify(player_data_parsed)
		});

		return next_song ? next_song : null;
	}
	return null;
};

export const prev_song = (): string | null => {
	logger.send('Loading previous song in prev_cache');
	const player_data = cache_control({
		name: 'player_data',
		method: 'get'
	});

	if (player_data) {
		const player_data_parsed = JSON.parse(player_data);
		let prev_song = null;
		logger.send('Searching for non-null value in the prev_cache');
		while (prev_song === null) {
			prev_song = (player_data_parsed.prev_queue as string[]).pop() as string | null | undefined;
		}

		if (prev_song === undefined) {
			logger.send('The end of the cache reached without a result.');
			logger.send('Probably load a song?!');
			return null;
		}

		logger.send(`Song found: ${prev_song}`);
		logger.send('Updating current song');

		player_data_parsed.queue_list.unshift(player_data_parsed.current);
		player_data_parsed.current = prev_song;

		logger.send('Updating cache');

		cache_control({
			name: 'player_data',
			method: 'set',
			data: JSON.stringify(player_data_parsed)
		});

		return prev_song;
	}
	return null;
};

export const skip_ahead = (amount: number): string | null => {
	amount++; // Index starts at 0
	logger.send(`Skipping ahead by: ${amount}`);
	const player_data = cache_control({
		name: 'player_data',
		method: 'get'
	});

	if (player_data) {
		let current_song: string | null = '';
		for (let x = 0; x < amount; x++) {
			current_song = next_song();
		}
		return current_song;
	}
	return null;
};

const clean_nulls = () => { };
