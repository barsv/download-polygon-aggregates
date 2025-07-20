import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [sveltekit()],
	server: {
		// Proxy only needed for development
		proxy: {
			'/api': {
				target: 'http://localhost:8000',
				changeOrigin: true,
			}
		}
	}
});
