<script lang="ts">
    import { Navigate } from "svelte-router-spa";
    import type { SocialProfile } from "../models";
    import { ExplorePresenter } from "../presenters/ExplorePresenter";

    let presenter = new ExplorePresenter();
    let profiles: Promise<SocialProfile[]> = presenter.refresh();
    let disableButtons: boolean;
    presenter.disableButtons.subscribe(_disableButtons => {disableButtons = _disableButtons});
</script>

<div>
    <h2 class="title">Explore</h2>
    <button class="refresh outline" disabled={disableButtons} on:click={() => {profiles = presenter.refresh()}}>Refresh</button>
    
    {#await profiles}
        <p>Loading most popular profiles...</p>
        <progress />
    {:then profiles} 
        {#if profiles.length > 0}
            <div class="grid">
                {#each profiles as profile}
                    <article>
                        <header>
                            <strong>Username</strong>: {profile.username}
                        </header>
                        <strong>Followers</strong>: {profile.followers}
                        <footer>
                            <strong class="link"><Navigate to="/"> Segui </Navigate></strong> <br>
                        </footer>  
                    </article>
                {/each}
            </div>
        {:else}
            <p>No profiles found</p>
        {/if}
    {/await}
</div>

<style>
    :root[data-theme="light"] {
        --spinner-invert: 0%
    }
    :root:not([data-theme="light"]) {
        --spinner-invert: 100%
    }
    article {
        margin-top: 1em;
        margin-bottom: 1em;
    }
    .title {
        display: inline;
    }
    .refresh {
        display: inline;
        width: fit-content;
        margin-left: 0.5em;
        padding: 0.5em;
    }
    .grid {
        grid-template-columns: repeat(auto-fill, minmax(20em, 1fr));
    }
</style>
