<script lang="ts">
    import { Route } from "svelte-router-spa";
    import Nav from "./Nav.svelte";

    export let currentRoute;
    export let params = {};
</script>

<Nav {currentRoute} />
<main class="container">
    <p class="timestamp">build: {__BUILD_TIMESTAMP__}</p>
    <Route {currentRoute} {params} />
</main>

<style>
    .timestamp {
        font-size: xx-small;
        margin-bottom: 0px;
    }
</style>
