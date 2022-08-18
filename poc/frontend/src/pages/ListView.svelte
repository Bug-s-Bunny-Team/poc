<script lang="ts">
    import type { Location } from "../models";
    import { ListPresenter } from "../presenters/ListPresenter";
    let presenter = new ListPresenter();
    let locations: Promise<Location[]>;
    locations = presenter.refresh();
</script>

<div>
    <h2 class="title">Locations</h2>
    <button class="refresh outline" disabled={locations === null} on:click={() => {locations = presenter.refresh()}}>Refresh</button>
    
    {#await locations}
        <p>Loading locations...</p>
        <progress />
    {:then locations} 
        {#if locations && locations.length > 0}
            <div class="grid">
                {#each locations as location}
                    <article>
                        <header>
                            <strong>Location</strong>: 
                            {location.name}
                        </header>
                        <strong>Score</strong>:
                        {location.score}
                    </article>
                {/each}
            </div>
        {:else if locations && locations.length == 0}
            <p>No locations</p>
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
