<script>

    import { Navigate } from 'svelte-router-spa'
	let email;
    let password;
    let firstName;
    let lastName;
    let loading;


    export let sdkoptions;

    const handleSubmit=()=>{
        const signupFields={
            "FirstName": firstName,
            "LastName": lastName,
            "Email": [
                {
                "Type": "Primary",
                "Value": email
                }
            ],
            "Password": password
     }
     console.log(signupFields)
   }

</script>
 
 <h2>Register</h2>
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
        <div class="inputBox">
            <label for="userConfirmPassword">Confirm Password</label>
            <input type="password" name="userPassword" id="userConfirmPassword" placeholder="confirm your password"
                   required/>
        </div>
        <button type="submit" name="" style="float: left;">Submit</button>
        <strong class="link"><Navigate to="/login">Login</Navigate></strong>
    </form>
<footer>
</footer>
