<script lang="ts">

    //MAP VIEW
    import * as L from 'leaflet';
    // If you're playing with this in the Svelte REPL, import the CSS using the
    // syntax in svelte:head instead. For normal development, this is better.
    import 'leaflet/dist/leaflet.css';
    let map;
    let yes=false;
  
    function createMap(container) {
      let m = L.map(container).setView([45.420, 11.895], 13);
      L.tileLayer(
        'https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png',
        {
          attribution: `&copy;<a href="https://www.openstreetmap.org/copyright" target="_blank">OpenStreetMap</a>,
            &copy;<a href="https://carto.com/attributions" target="_blank">CARTO</a>`,
          subdomains: 'abcd',
          maxZoom: 18,
        }
      ).addTo(m);
  
      return m;
    }
  
    function mapAction(container) {
      map = createMap(container);
      return {
        destroy: () => {
          map.remove();
        },
      };
    }

    // -----------------------------------------------
    //LIST VIEW
    import type { Post } from "../models";
    import { onDestroy, onMount } from "svelte";
    import spinnerUrl from "../assets/pulse-rings-3.svg";
    import { ListPresenter } from "../presenters/ListPresenter";

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

<div>
    <label for="choose view"> choose map view or list view 
    <input type="checkbox" id="choose" role="switch" bind:checked={yes}> 
    </label>
</div>
    {#if yes}
    <head>
        <!-- In the REPL you need to do this. In a normal Svelte app, use a CSS Rollup plugin and import it from the leaflet package. -->
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
        integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
        crossorigin=""/>
    </head>
    
    <div style="height:400px;width:100%" use:mapAction />
    {:else if yes==false}
    <h2 class="title">Posts</h2>
    <button class="refresh outline" disabled={posts === null} on:click={presenter.refresh}>Refresh</button>
    
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
                            <li>
                                <strong>Location</strong>: {post.location
                                    ? post.location.name
                                    : "N/A"}
                            </li>
                            <li class="caption">
                                <details>
                                    <summary><strong>Caption</strong></summary>
                                    <p>{post.caption}</p>
                                </details>
                            </li>
                        </ul>
                    </header>
                    <div class="img-container">
                        <img src={`/${post.media_url}`} alt="idk" />
                    </div>
                    <footer>
                        {#if post.score}
                            <ul>
                                <li>
                                    <strong>Caption score</strong>: {post.score
                                        .caption_score}
                                </li>
                                <li>
                                    <strong>Media score</strong>: {post.score
                                        .media_score}
                                </li>
                            </ul>
                        {:else}
                            <span>
                                <img
                                class="spinner"
                                src="{spinnerUrl}"
                                alt="Loading animation"
                            />
                            Scoring in progress...
                            </span>
                        {/if}
                    </footer>
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









