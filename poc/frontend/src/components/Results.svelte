<script lang="ts">
    let results = [
        {
            "username": "testuser123",
            "location": null,
            "caption": "",
            "caption_score": 1,
            "media_score": 1,
        }
    ]
</script>

<div>
    <h2>Results</h2>
    {#each results as result}
        <article>
            <header class="no-bottom-padding">
                <ul>
                    <li><strong>Username</strong>: {result.username}</li>
                    <li><strong>Location</strong>: {result.location ? result.location : "N/A"}</li>
                </ul>
            </header>
            <div class="img-container">
                <img src="https://bestpetsvet.com/wp-content/uploads/2019/02/cat-2146089_1280.jpg" alt="idk">
            </div>
            <footer class="no-bottom-padding">
                <ul>
                    <li><strong>Caption score</strong>: {result.caption_score}</li>
                    <li><strong>Media score</strong>: {result.media_score}</li>
                </ul>
            </footer>
        </article>
    {/each}
</div>

<style>
    li {
        list-style-type: none;
    }
    .no-bottom-padding {
        padding-bottom: 0px;
    }
    .img-container {
        text-align: center;
    }
    img {
        max-width: 80%;
    }
</style>
