<script lang="ts">
    import type { Post } from "../models";
    import catUrl from "../assets/cat.jpg";

    let posts: Array<Post> = [
        {
            id: 1,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 1,
                username: "testuser1"
            },
            location: {
                id: 1,
                name: "Rome, Italy",
                lat: 0,
                long: 0,
                score: 1,
            }
        },
        {
            id: 2,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 2,
                username: "testuser2"
            },
            location: null
        },
        {
            id: 2,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 2,
                username: "testuser2"
            },
            location: null
        },
        {
            id: 2,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 2,
                username: "testuser2"
            },
            location: null
        },
        {
            id: 2,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 2,
                username: "testuser2"
            },
            location: null
        },
        {
            id: 2,
            caption: "",
            caption_score: 1,
            media_score: 1,
            profile: {
                id: 2,
                username: "testuser2"
            },
            location: null
        },
    ];
</script>

<div>
    <h2>Posts</h2>
    {#if posts && posts.length > 0}
        <div class="grid">
            {#each posts as post}
                <article>
                    <header>
                        <ul>
                            <li><strong>Username</strong>: {post.profile.username}</li>
                            <li>
                                <strong>Location</strong>: {post.location
                                    ? post.location.name
                                    : "N/A"}
                            </li>
                        </ul>
                    </header>
                    <div class="img-container">
                        <img src={catUrl} alt="idk" />
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
        <h2>No posts</h2>
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
