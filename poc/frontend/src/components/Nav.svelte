<script lang="ts">
    import routes from "../routes";
    export let currentRoute;
    console.log(currentRoute);
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
    </ul>
</nav>

<style>
    .current {
        --background-color: var(--primary-focus);
        --color: var(--primary-hover);
    }
</style>
