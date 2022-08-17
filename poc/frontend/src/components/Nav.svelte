<script lang="ts">

    import { AccountModel } from "../models/accountModel";
    import routes from "../routes";
    import ThemeSwitch from "./ThemeSwitch.svelte";
    
    let isLog=true;
    const account = AccountModel.getInstance().account;
        if(account) {
            isLog=true;
        }
    export let currentRoute;

</script>

<nav class="container">
    <ul>
        <li><strong>BunnyFood</strong></li>
        <li class="timestamp">build: {__BUILD_TIMESTAMP__}</li>
    </ul>
    <ul>
        {#each routes as route}
           {#if isLog && route.typeOfRoute == "public"}
            <li>
                <a
                    class={currentRoute.name == route.name ? "current" : ""}
                    href={route.name}>{route.title}</a
                >
            </li>
            {:else if !isLog && route.typeOfRoute == "private"}
            <li>
                <a
                    class={currentRoute.name == route.name ? "current" : ""}
                    href={route.name}>{route.title}</a
                >
            </li>
           {/if} 
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
