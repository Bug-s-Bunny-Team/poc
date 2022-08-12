import { AccountModel } from "../models/accountModel";

export class AccountPresenter {
    firstname: string;
    lastname: string;
    username: string;
    email: string;

    constructor() {
        this.handleAccount = this.handleAccount.bind(this);
    }

    handleAccount() : void {
        const accModel = AccountModel.getInstance();
     
    }

}
