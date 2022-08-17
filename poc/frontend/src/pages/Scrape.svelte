<script lang="ts">
    import { navigateTo } from "svelte-router-spa";

    const modes = ["Username", "URL"];
    let mode = modes[0];
    let scrapeInput = "";
    let showProgress = false;

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
                navigateTo("/listview");
            })
            .catch((err) => {
                console.log(err)
                showProgress = false;
            });
    }
</script>

<h2>Scrape</h2>
<article>
    {#if mode == "Username"}
        <p>Scrape last post from some profile username.</p>
    {:else}
        <p>Scrape a post from its URL.</p>
    {/if}
    <form on:submit|preventDefault={handleSubmit} autocomplete="off">
        <div class="grid">
            {#if mode == "Username"}
                <label for="scrape-input">
                    Username
                    <input
                        type="text"
                        id="scrape-input"
                        bind:value={scrapeInput}
                        placeholder="testuser123"
                        required
                        disabled={showProgress}
                        pattern="^[^\s]+$"
                    />
                </label>
            {:else}
                <label for="scrape-input">
                    URL
                    <input
                        type="url"
                        id="scrape-input"
                        bind:value={scrapeInput}
                        placeholder="https://www.instagram.com/p/Cek7VMLjsOa"
                        required
                        disabled={showProgress}
                    />
                </label>
            {/if}
            <div>
                <label for="mode-select">Mode</label>
                <select
                    id="mode-select"
                    bind:value={mode}
                    disabled={showProgress}
                >
                    {#each modes as mode}
                        <option value={mode}>{mode}</option>
                    {/each}
                </select>
            </div>
        </div>
        <button type="submit" disabled={showProgress}>Scrape</button>
    </form>
    {#if showProgress}
        <progress />
    {/if}
</article>
