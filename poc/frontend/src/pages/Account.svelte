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
    
            <label for="choosePreference" class="link">Display my guide as map: </label>
            <input type="checkbox" name="preference" id="choosePreference" role="switch" on:change={presenter.changePreference} bind:checked={presenter.preference} >
    
            <strong class="link"><Navigate to="/changepsw">Change your password </Navigate></strong>
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
