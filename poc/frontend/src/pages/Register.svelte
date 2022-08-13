<script lang="ts">

    import { RegistrationPresenter } from '../presenters/RegistrationPresenter';
    import { Navigate } from 'svelte-router-spa'
	
    let email;
    let password;
    let firstName;
    let lastName;
    let loading;
    let presenter = new RegistrationPresenter();

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
            <label for="firstName">First name</label>
            <input type="text" name="firstName" id="firstName" placeholder="type your first name" required on:click={presenter.handleRegister}/>
        </div>
        <div class="inputBox">
            <label for="lastName">Last name</label>
            <input type="text" name="lastName" id="lastName" placeholder="type your last name" required on:click={presenter.handleRegister}/>
        </div>
        <div class="inputBox">
            <label for="userName">Username</label>
            <input type="text" name="userName" id="userName" placeholder="type your username" required on:click={presenter.handleRegister}/>
        </div>
        <div class="inputBox">
            <label for="userEmail">Email</label>
            <input type="email" name="userEmail" id="userEmail" placeholder="type your email"
                   required on:click={presenter.handleRegister}/>
        </div>
        <div class="inputBox">
            <label for="userPassword">Password</label>
            <input type="password" name="userPassword" id="userPassword" placeholder="type your password"
                   required on:click={presenter.handleRegister}/>
        </div>
        <div class="inputBox">
            <label for="userConfirmPassword">Confirm Password</label>
            <input type="password" name="userPassword" id="userConfirmPassword" placeholder="confirm your password"
                   required on:click={presenter.handleRegister}/>
        </div>
        <button type="submit" name="" style="float: left;">Submit</button>
        <strong class="link"><Navigate to="/login">Login</Navigate></strong>
    </form>
<footer>
</footer>
