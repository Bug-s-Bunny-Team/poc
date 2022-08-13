import { AccountModel } from "../models/accountModel";

export class AccountPresenter {
    name: string;
    email: string;
    followers: Number;
    preference: boolean;
    isLogged: boolean;

    constructor() {
        this.changePreference = this.changePreference.bind(this);
        this.handleLogout = this.handleLogout.bind(this);

        const account = AccountModel.getInstance().account;
        this.checkLogin();
        if(this.isLogged) {
            this.name = account.accountname;
            this.email = account.email;
            this.followers = account.followers;
            this.preference = account.preference;
        }
    }

    changePreference() : void {
        this.checkLogin();
        if(this.isLogged) {
            const account = AccountModel.getInstance().account;
            account.preference = this.preference;
        }
    }

    handleLogout() : void {
        this.checkLogin();
        if(this.isLogged) {
            const accModel = AccountModel.getInstance();
            accModel.logout();
            this.checkLogin();
        }
    }

    private checkLogin() {
        this.isLogged = AccountModel.getInstance().account ? true : false;
    }

}
