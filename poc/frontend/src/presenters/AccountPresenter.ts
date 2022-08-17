import { AccountModel } from "../models/accountModel";

export class AccountPresenter {
    name: string;
    email: string;
    followers: Number;
    preference: Number;

    constructor() {
        this.changePreference = this.changePreference.bind(this);
        this.handleLogout = this.handleLogout.bind(this);

        const account = AccountModel.getInstance().account;
        if(this.isLogged()) {
            this.name = account.accountname;
            this.email = account.email;
            this.followers = account.followers;
            this.preference = Number(account.preference);
        }
    }

    changePreference() : void {
        if(this.isLogged()) {
            const accModel = AccountModel.getInstance();
            accModel.cambiaPreferenza(Boolean(!this.preference));
        }
    }

    handleLogout() : void {
        if(this.isLogged()) {
            const accModel = AccountModel.getInstance();
            accModel.logout();
        }
    }

    isLogged() {
        return AccountModel.getInstance().account ? true : false;
    }

}
