<script lang="ts">
    import type { Post } from "../models";
    import { onMount } from "svelte";

    let posts: Array<Post> = [];

    onMount(() => {
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                posts = data;
                console.log(data);
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
                                <strong>Username</strong>: {post.profile.username}
                            </li>
                            <li>
                                <strong>Location</strong>: {post.location
                                    ? post.location.name
                                    : "N/A"}
                            </li>
                        </ul>
                    </header>
                    <div class="img-container">
                        <img src={`/${post.media_url}`} alt="idk" />
                    </div>
                    <footer>
                        <ul>
                            <li>
                                <strong>Caption score</strong>: {post.caption_score}
                            </li>
                            <li>
                                <strong>Media score</strong>: {post.media_score}
                            </li>
                        </ul>
                    </footer>
                </article>
            {/each}
        </div>
    {:else}
        <p>Loading posts...</p>
        <progress></progress>
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
    .grid {
        grid-template-columns: repeat(auto-fill, minmax(20em, 1fr));
    }
    .img-container {
        text-align: center;
    }
</style>
