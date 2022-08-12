<script>
    //import { LoginPresenter } from '../presenters/ChangePswPresenter'    
    //let presenter = new ChangePresenter();
    //import { Navigate } from 'svelte-router-spa'

    let new_password;
    let repeat_password;
    let loading;

    const handleSubmit=()=>{
        const changepswFields={
            "NewPsw": new_password,
            "RepeatPsw": repeat_password,
     }
     console.log(changepswFields)
   }

</script>

    <h2>Change your password</h2>
    <form>
        <div class="inputBox">
            <label for="userPassword">Actual Password</label>
            <input type="password" name="userPassword" id="userPassword" placeholder="type your actual password" required/> 
        </div>
        <div class="inputBox">
            <label for="newuserPassword">New Password</label>
            <input type="password" name="userPassword" id="newuserPassword" placeholder="type your new password" required/> 
        </div>
        <div class="inputBox">
            <label for="reapuserPassword">Confirm Password</label>
            <input type="password" name="userPassword" id="reapuserPassword" placeholder="type your new password again" required/> 
        </div>
            <button type="submit" name="" style="float: left;">Submit</button>
    </form>
<footer>
</footer>
