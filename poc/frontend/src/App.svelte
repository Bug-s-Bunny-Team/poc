<script lang="ts">
    import { Router } from 'svelte-router-spa'
    import routes from './routes'
</script>

<main class="container">
    <h1>PoC</h1>

    <Router {routes} />
</main>

<style lang="css" global>
    @import "./style.css";
</style>
