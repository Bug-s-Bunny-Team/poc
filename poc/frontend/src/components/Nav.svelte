<script lang="ts">

    import { PublicRoutes } from "../routes/PublicRoutes";
    import routes from "../routes";
    import ThemeSwitch from "./ThemeSwitch.svelte";
    
    
    export let currentRoute;
</script>

<nav class="container">
    <ul>
        <li><strong>PoC</strong></li>
        <li class="timestamp">build: {__BUILD_TIMESTAMP__}</li>
    </ul>
    <ul>
        {#each PublicRoutes as route}
            <li>
                <a
                    class={currentRoute.name == route.name ? "current" : ""}
                    href={route.name}>{route.title}</a
                >
            </li>
        {/each}
        <li>
            <ThemeSwitch/>
        </li>
    </ul>
</nav>

<style>
    .current {
        --background-color: var(--primary-focus);
        --color: var(--primary-hover);
    }
    .timestamp {
        font-size: xx-small;
        margin-bottom: 0px;
    }
</style>
