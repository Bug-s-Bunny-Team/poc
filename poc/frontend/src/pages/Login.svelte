<script>
    import { LoginPresenter } from '../presenters/LoginPresenter'    
    import { Navigate } from 'svelte-router-spa'
    let presenter = new LoginPresenter();
</script>

    <h2>Login</h2>
    <form>
        <div class="inputBox">
            <label for="userName">Username</label>
            <input type="text" name="userName" id="userName" placeholder="type your username" required bind:value={presenter.username}/>
        </div>
        <div class="inputBox">
            <label for="userPassword">Password</label>
            <input type="password" name="userPassword" id="userPassword" placeholder="type your password" required bind:value={presenter.password}/>
        </div>
        <div>
            <input type="checkbox" name="preference" id="remember" value="preference" on:change={presenter.RememberFields} bind:checked={presenter.remember} >
            <label for="preference" > remember </label> 
        </div>
        <div>
            <button type="submit" name="" style="float: left;" on:click={presenter.handleLogin}>Submit</button>
            <strong class="link"><Navigate to="/register">Register</Navigate></strong>

        </div>
    </form>
<footer>
</footer>
