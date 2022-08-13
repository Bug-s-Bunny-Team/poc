import { AccountModel } from "../models/accountModel";

export class AccountPresenter {
    name: string;
    email: string;
    preference: boolean;

    constructor() {
        this.changePreference = this.changePreference.bind(this);
        this.handleLogout = this.handleLogout.bind(this);

        const account = AccountModel.getInstance().account;
        if(account) {
            this.name = account.accountname;
            this.email = account.email;
            this.preference = account.preference;
        }
    }

    changePreference() : void {
        const account = AccountModel.getInstance().account;
        if(account) account.preference = this.preference;
    }

    handleLogout() : void {
        const accModel = AccountModel.getInstance();
        accModel.logout();
    }

}
