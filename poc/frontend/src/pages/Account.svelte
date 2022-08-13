<script>
    import { AccountPresenter } from '../presenters/AccountPresenter';
    import { Navigate } from 'svelte-router-spa'
import Login from './Login.svelte';
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
  
    <label for="choosePreference" class="link">Choose your predefined guide: </label>
    <ul>
        <li> 
            <input type="checkbox" name="preferenceM" id="choosePreferenceM" on:change={presenter.changePreference} bind:checked={presenter.preference} value="map" >
            <label for="map"> Map </label>
        </li>
        <li> 
            <input type="checkbox" name="preferenceL" id="choosePreferenceL" on:change={presenter.changePreference} bind:checked={presenter.preference} value="list">
            <label for="list"> List </label>
        </li>
    </ul>

    <strong class="link"><Navigate to="/changepsw">Change your password </Navigate></strong> <br>
    <a href="login"> <button class="link" type="submit" > Logout</button></a>
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
