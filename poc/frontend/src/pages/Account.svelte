,<script>
    import { Navigate } from 'svelte-router-spa'
</script>

<h2>My Account</h2>
<h3> Your personal information </h3>
<label for="email"> email: </label>
<label for="firstname"> firstname: </label>
<label for="lastname"> lastname: </label>
<strong class="link"><Navigate to="/changepsw">Change your password </Navigate></strong> <br>
<strong class="link">Choose your predefined guide </strong>
<button type="submit" name="" style="float: left;">Logout</button>
<footer>
</footer>
