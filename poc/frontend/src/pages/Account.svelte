<script>
    import { AccountPresenter } from '../presenters/AccountPresenter';
    import { Navigate } from 'svelte-router-spa'
    let presenter = new AccountPresenter();
</script>

<h2>My Account</h2>
<h3> Your personal information </h3>
    <p> Name: { presenter.name }</p>
    <p> Email: { presenter.email }</p>

    <label for="choosePreference" class="link">Choose your predefined guide: </label>
    <input type="checkbox" name="preference" id="choosePreference" on:change={presenter.changePreference} bind:checked={presenter.preference} >

    <strong class="link"><Navigate to="/changepsw">Change your password </Navigate></strong> <br>
    <button type="submit" name="" style="float: left;">Logout</button>
<footer>
</footer>
