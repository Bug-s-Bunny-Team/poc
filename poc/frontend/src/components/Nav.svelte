<script lang="ts">
    import routes from "../routes";
    export let currentRoute;

    let dark = false;

    function setTheme() {
        document.getElementsByTagName('html')[0].dataset.theme = dark ? "dark" : "light";
    }
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
            <label for="dark-switch">
                Dark
                <input
                    class="theme-selector"
                    type="checkbox"
                    id="dark-switch"
                    role="switch"
                    bind:checked={dark}
                    on:change={setTheme}
                />
            </label>
        </li>
    </ul>
</nav>

<style>
    .current {
        --background-color: var(--primary-focus);
        --color: var(--primary-hover);
    }
</style>
