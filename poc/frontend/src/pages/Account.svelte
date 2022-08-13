<script>
    import { AccountPresenter } from '../presenters/AccountPresenter';
    import { Navigate } from 'svelte-router-spa'
import Login from './Login.svelte';
    let presenter = new AccountPresenter();
</script>

<h2>My Account</h2>
<h3> Your personal information </h3>
    <p> Name: { presenter.name }</p>
    <p> Email: { presenter.email }</p>
    <p> Follower: {presenter.follower} </p>

    <!-- SISTEMARE CHE SE PREMO SU UNO L'ALTRO DEVE ESSERE PER FORZA BIANCO-->
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
