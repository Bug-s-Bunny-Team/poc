<script>
    import { AccountPresenter } from '../presenters/AccountPresenter';
    import { Navigate } from 'svelte-router-spa'
    let presenter = new AccountPresenter();
</script>

{#if presenter.isLogged}
    <h2>My Account</h2>
    <h3> Your personal information </h3>
    <article>
        <form>
            <p> Name: { presenter.name }</p>
            <p> Email: { presenter.email }</p>
            <p> Follower: {presenter.followers} </p>

            <p>
                Choose your predefined guide:
                <label>
                    <input type=radio id="choosePreferenceM" on:change={presenter.changePreference} bind:group={presenter.preference} value={1}>
                    List
                </label>
                <label>
                    <input type=radio id="choosePreferenceL" on:change={presenter.changePreference} bind:group={presenter.preference} value={0}>
                    Map
                </label>
            </p>

            <strong class="link"><Navigate to="/changepsw">Change your password </Navigate></strong>

            <strong class="link"><Navigate to="/followees">Followees</Navigate></strong>
            <button type="submit" name="" id="followees">Show Followees</button>
            <button type="submit" name="" id="logout" on:click={presenter.handleLogout}>Logout</button>
        </form>
    </article>
{:else}
    <article>
        <p>Non sei loggato, effettua il Login:</p>
        <strong class="link"><Navigate to="/login">Login </Navigate></strong>
    </article>
{/if}

<footer>
</footer>

<style>

    #choosePreference {
        display: block;
        margin-top: 0.5em;
        margin-bottom: 1.5em;
        
    }

    strong.link {
        display: block;
        margin-bottom: 1.5em;
    }

</style>
