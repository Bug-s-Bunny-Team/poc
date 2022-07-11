<script lang="ts">
    import type { Post } from "../models";
    import { onMount } from "svelte";
    import spinnerUrl from "../assets/pulse-rings-3.svg";

    let posts: Array<Post> = null;

    onMount(() => {
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                posts = data;
            })
            .catch((err) => console.log(err));
    });
</script>

<div>
    <h2>Posts</h2>
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
    {:else}
        <p>Loading posts...</p>
        <progress />
    {/if}
</div>

<style>
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
    .grid {
        grid-template-columns: repeat(auto-fill, minmax(20em, 1fr));
    }
    .img-container {
        text-align: center;
    }
    .caption {
        margin-bottom: 0px;
    }
</style>
