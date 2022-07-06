<script lang="ts">
    const modes = [
        {
            name: "username",
            label: "Username",
            placeholder: "testuser123",
        },
        {
            name: "url",
            label: "URL",
            placeholder:
                "https://www.instagram.com/p/Cek7VMLjsOa/?igshid=Ym34HBuPY=",
        },
    ];
    let mode = modes[0];
    let scrapeInput = "";
    let showProgress = false;

    function timeout(ms) {
        return new Promise((resolve) => setTimeout(resolve, ms));
    }

    async function handleSubmit() {
        let request = {
            [mode.name]: scrapeInput,
        };
        console.log(JSON.stringify(request));

        showProgress = true;
        await timeout(3000);
        showProgress = false;
    }
</script>

<article>
    <form on:submit|preventDefault={handleSubmit}>
        <div class="grid">
            <label for="scrape-input">
                {mode.label}
                <input
                    type="text"
                    id="scrape-input"
                    bind:value={scrapeInput}
                    placeholder={mode.placeholder}
                    required
                    disabled="{showProgress}"
                />
            </label>
            <div>
                <label for="mode-select">Mode</label>
                <select id="mode-select" bind:value={mode} disabled="{showProgress}">
                    {#each modes as mode}
                        <option value={mode}>{mode.label}</option>
                    {/each}
                </select>
            </div>
        </div>
        <button type="submit" disabled="{showProgress}">Scrape</button>
    </form>
    {#if showProgress}
        <progress />
    {/if}
</article>
