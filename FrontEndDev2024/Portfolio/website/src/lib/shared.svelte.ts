type Message = {
	id: number;
	message: string;
	timeout: number;
	priority: number;
	dismissable?: boolean;
};

export const user_data = $state({
	preferred_color: '#ff0000',
	default_volume: 0,
	keep_image: true,
	keep_gradient: true,
	keep_dull: true,
	ahead: 1 // How many songs to look ahead.
});

export const player_data = $state({
	volume: 0,
	state: true,
	shuffle: true,
	time: 0,
	queue_list: [] as any[],
	prev_queue: [] as any[],
	current: ''
});

export const notifications = $state([] as Message[]);

export const PROD = false;
