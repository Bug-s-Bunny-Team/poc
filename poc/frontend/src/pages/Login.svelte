<script>
    let email; 
    let password; 
    
    import { Navigate } from 'svelte-router-spa'
    const handleSubmit=(e)=>{
       let loginFields={email,password};
	   console.log(loginFields)
    }
    
</script>

    <h2>Login</h2>
    <form>
        <div class="inputBox">
            <label for="userName">Username</label>
            <input type="text" name="userName" id="userName" placeholder="type your username" required/>
        </div>
        <div class="inputBox">
            <label for="userPassword">Password</label>
            <input type="password" name="userPassword" id="userPassword" placeholder="type your password"
                   required/>
        </div>
        <div>
            <button type="submit" name="" style="float: left;">Submit</button>
            <strong class="link"><Navigate to="/register">Register</Navigate></strong>
        </div>
    </form>
<footer>
</footer>
