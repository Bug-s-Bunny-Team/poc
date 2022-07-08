import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [svelte()],
    define: {
        '__BUILD_TIMESTAMP__': JSON.stringify(new Date().toISOString()),
        '__API_BASE__': JSON.stringify(process.env.ENV === 'prod' ? 'https://api' : 'http://localhost:3000')
    }
})
