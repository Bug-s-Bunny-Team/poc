<script lang="ts">

    import { ExplorePresenter } from '../presenters/ExplorePresenter';
    import { onDestroy, onMount } from "svelte";
  
    const interval = setInterval(() => presenter.refreshAccounts(), 6000);
    let presenter = new ExplorePresenter();

    onMount(() => {
        presenter.refresh();
    });

    onDestroy(() => {
        clearInterval(interval);
    })
</script>

<div>
    <h2 class="title">Explore</h2>
    <button class="refresh outline" disabled={presenter.accounts === null} on:click={presenter.refresh}>Refresh</button>
    
    {#if presenter.accounts && presenter.accounts.length > 0}
        <div class="grid">
            {#each presenter.accounts as account}
                <article>
                    <header>
                        <ul>
                            <li>
                                <strong>Username</strong>: {account.accountname}
                            </li>
                            <li>
                                <strong>Followers:</strong>
                            </li>
                            <li class="caption">
                                <details>
                                    <p>{account.followers}</p>
                                </details>
                            </li>
                        </ul>
                    </header>
                </article>
            {/each}
        </div>
    {:else if presenter.accounts && presenter.accounts.length == 0}
        <p>No accounts</p>
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
