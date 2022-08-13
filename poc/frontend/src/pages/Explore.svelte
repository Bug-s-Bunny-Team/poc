<script lang="ts">

    import { ExplorePresenter } from '../presenters/ExplorePresenter';
    import type { Account } from "../models";
    import { onDestroy, onMount } from "svelte";
    import spinnerUrl from "../assets/pulse-rings-3.svg";

    let accounts: Array<Account> = [];
    const interval = setInterval(() => refreshAccounts(), 6000);

    function refreshAccounts() {
        fetch("/dev-api/post")
            .then((response) => response.json())
            .then((data) => {
                accounts = data;
            })
            .catch((err) => {
                console.log(err);
                accounts = [];
            });
    }

    function refresh() {
        accounts = null;
        refreshAccounts();
    }

    onMount(() => {
        refresh();
    });

    onDestroy(() => {
        clearInterval(interval);
    })
</script>

<div>
    <h2 class="title">Explore</h2>
    <button class="refresh outline" disabled={accounts === null} on:click={refresh}>Refresh</button>
    
    {#if accounts && accounts.length > 0}
        <div class="grid">
            {#each accounts as account}
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
    {:else if accounts && accounts.length == 0}
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
