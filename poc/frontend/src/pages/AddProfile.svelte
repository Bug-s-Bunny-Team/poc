<script lang="ts">
    import { Navigate } from "svelte-router-spa";

    const modes = ["Username", "URL"];
    let mode = modes[0];
    let scrapeInput = "";
    let showProgress = false;
    let showPeople = false;

    function timeout(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
    }

    async function handleSubmit() {
        let request = {
            [mode.toLowerCase()]: scrapeInput,
        };

        showProgress = true;
        // await timeout(2000);
        fetch('/dev-api/posts', {
            method: "POST",
            body: JSON.stringify(request),
        })
            .then((res) => res.json())
            .then((data) => {
                console.log(data);
                showProgress = false;
                showPeople=true;
                // navigateTo("/listview");
            })
            .catch((err) => {
                console.log(err)
                showProgress = false;
            });
    }


    // per vedere le persone
    import { onDestroy, onMount } from "svelte";
    import spinnerUrl from "../assets/pulse-rings-3.svg";
    import { ListPresenter } from "../presenters/ListPresenter";

    /*
    let presenter= new AddProfilePresenter();
    let addprofile;
    const interval= setIntervla(() => presenter.refreshAddProfile(), 6000);
    
    presenter.addprofile.subscribe( data => {
        addprofile = data;
    })
    */

    let presenter = new ListPresenter();
    let posts;
    const interval = setInterval(() => presenter.refresh(), 6000);

    // https://svelte.dev/tutorial/writable-stores
    presenter.posts.subscribe(data => {
        posts = data;
    })

    onMount(() => {
        presenter.refresh();
    });

    onDestroy(() => {
        clearInterval(interval);
    })
</script>

<article> 
    <form on:submit|preventDefault={handleSubmit} autocomplete="off">
    <div class="grid">
    <label for="scrape-input">
        Search a new profile
                <input
                    type="search"
                    id="scrape-input"
                    bind:value={scrapeInput}
                    placeholder="testuser123"
                    required
                    disabled={showProgress}
                    pattern="^[^\s]+$"
                />
    </label>
    <button id="submit" type="submit" disabled={showProgress}> Search </button>
    </div>
    </form>

    {#if showProgress}
        <progress />
    {/if}
</article>

{#if showPeople && scrapeInput !=""}
    {#if posts && posts.length > 0}
    <div class="grid">
        {#each posts as post}
            <article>
                <header>
                    <ul>
                        <li>
                            <strong>Username</strong>: {post.profile
                                .username}
                        </li>
                       
                        <!-- bisogna aggiungere il resto -->
                    </ul>
                </header>
                <div class="img-container">
                    <img src={`/${post.media_url}`} alt="idk" />
                </div> 
                
                <strong class="link"><Navigate to="/"> Segui </Navigate></strong> <br>
                                 
            </article>
        {/each}
    </div>
    {:else if posts && posts.length == 0}
    <p>No posts</p>
    {:else}
    <p>Loading posts...</p>
    <progress />
    {/if}
{/if}


<style>
    button {
        margin: auto;
    }

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
