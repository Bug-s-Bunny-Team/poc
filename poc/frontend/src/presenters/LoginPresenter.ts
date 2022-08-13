//import { Account } from "src/models";
import { AccountModel } from "../models/accountModel";

export class LoginPresenter {
    username: string;
    password: string;
    remember: boolean;

    constructor() {
        this.RememberFields = this.RememberFields.bind(this);
        this.handleLogin = this.handleLogin.bind(this);
    }

    RememberFields() : void {
        const login = AccountModel.getInstance().account;
        if(login) login.remember = this.remember;
    } 

    handleLogin() : void {
        const accModel = AccountModel.getInstance();
        if(this.handleUsername() && this.handlePassword())
        //Todo:
        //Controllo se username esiste ok altrimenti errore username, 
        //se la password non corrisponde allora errore psw
            accModel.login(this.username, this.password, this.remember);
    }

    handleUsername() : boolean {
        if(this.username) return true;
        //Todo:
        //controllo se username non esiste nel db
    }

    handlePassword() : boolean {
        if(this.password) return true;
    }
}
