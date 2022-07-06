<script lang="ts">
    import catUrl from "../assets/cat.jpg";

    let posts = [
        {
            username: "testuser1",
            location: "Rome, Italy",
            caption: "",
            caption_score: 1,
            media_score: 1,
        },
        {
            username: "testuser2",
            location: "Rome, Italy",
            caption: "",
            caption_score: 1,
            media_score: 1,
        },
    ];
</script>

<div>
    <h2>Posts</h2>
    <div class="grid">
        {#each posts as post}
            <article>
                <header class="no-bottom-padding">
                    <ul>
                        <li><strong>Username</strong>: {post.username}</li>
                        <li>
                            <strong>Location</strong>: {post.location
                                ? post.location
                                : "N/A"}
                        </li>
                    </ul>
                </header>
                <div class="img-container">
                    <img src={catUrl} alt="idk" />
                </div>
                <footer class="no-bottom-padding">
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
</div>

<style>
    li {
        list-style-type: none;
    }
    img {
        max-width: 80%;
    }
    .no-bottom-padding {
        padding-bottom: 0px;
    }
    .img-container {
        text-align: center;
    }
</style>
