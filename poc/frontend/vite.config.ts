import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte()],
    define: {
        '__BUILD_TIMESTAMP__': JSON.stringify(new Date().toISOString())
    },
    server: {
        proxy: {
            '/dev-api': {
                target: 'http://127.0.0.1:3000/',
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/dev-api/, '')
            }
        }
    }
})
