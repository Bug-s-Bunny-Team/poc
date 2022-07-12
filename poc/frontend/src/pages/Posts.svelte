<script lang="ts">
    import type { Post } from "../models";
    import { onDestroy, onMount } from "svelte";
    import spinnerUrl from "../assets/pulse-rings-3.svg";

    let posts: Array<Post> = [];
    const interval = setInterval(() => refreshPosts(), 6000);

    function refreshPosts() {
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                posts = data;
            })
            .catch((err) => {
                console.log(err);
                posts = [];
            });
    }

    function refresh() {
        posts = null;
        refreshPosts();
    }

    onMount(() => {
        refresh();
    });

    onDestroy(() => {
        clearInterval(interval);
    })
</script>

<div>
    <h2 class="title">Posts</h2>
    <button class="refresh outline" disabled={posts === null} on:click={refresh}>Refresh</button>
    
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
