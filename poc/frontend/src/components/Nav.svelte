<script lang="ts">
    import routes from "../routes";
    import ThemeSwitch from "./ThemeSwitch.svelte";

    export let currentRoute;
</script>

<nav class="container">
    <ul>
        <li><strong>PoC</strong></li>
    </ul>
    <ul>
        {#each routes as route}
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
</style>
