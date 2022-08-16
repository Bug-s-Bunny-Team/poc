<script lang="ts">

    import { FolloweesPresenter } from '../presenters/FolloweesPresenter';
    import { Navigate } from 'svelte-router-spa'
    import { onDestroy, onMount } from "svelte";

    let presenter = new FolloweesPresenter();
    let followees;
    const interval = setInterval(() => presenter.refreshFollowees(), 6000);
    
    presenter.followees.subscribe(data => {
        followees = data;
    })

    onMount(() => {
        presenter.refresh();
    });

    onDestroy(() => {
        clearInterval(interval);
    })
</script>

<div>
    <h2 class="title">Explore</h2>
    <button class="refresh outline" disabled={presenter.followees === null} on:click={presenter.refresh}>Refresh</button>
    
    {#if followees && followees.length > 0}
        <div class="grid">
            {#each followees as followees}
                <article>
                    <header>
                        <ul>
                            <li>
                                <strong>Username</strong>: {followees.profile.username}
                            </li>
                            <li>
                                <strong>Followers:</strong>
                            </li>
                            <li class="caption">
                                <details>
                                    <p>{followees.followers}</p>
                                </details>
                            </li>
                            <li>
                                <strong class="link"><Navigate to="/">Rimuovi</Navigate></strong> <br>
                            </li>
                        </ul>
                    </header>
                </article>
            {/each}
        </div>
    {:else if followees && followees.length == 0}
        <p>No following accounts</p>
    {:else}
        <p>Loading accounts...</p>
        <progress />
    {/if}
</div>

<style>
    :root[data-theme="light"] {
        --spinner-invert: 0%
    }
    :root:not([data-theme="light"]) {
        --spinner-invert: 100%
    }
    ul {
        margin-bottom: 0px;
    }
    li {
        list-style-type: none;
    }
    article {
        margin-top: 1em;
        margin-bottom: 1em;
    }
    details {
        margin-bottom: 0px;
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
    .img-container {
        text-align: center;
    }
    .caption {
        margin-bottom: 0px;
    }
    .spinner {
        filter: invert(var(--spinner-invert));
    }
</style>
