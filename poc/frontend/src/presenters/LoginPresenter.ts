import { AccountModel } from "../models/accountModel";

export class LoginPresenter {
    username: string;
    password: string;

    constructor() {
        this.handleLogin = this.handleLogin.bind(this);
    }

    handleLogin() : void {
        const accModel = AccountModel.getInstance();
        accModel.login(this.username, this.password);
    }
}
