import { AccountModel } from "../models/accountModel";
import { PublicRoutes, ProtectedRoutes } from "../routes";

export class NavPresenter {
    routes;

    constructor() {
        if(this.isLogged()) { this.routes = ProtectedRoutes; }
        else { this.routes = PublicRoutes; }
    }

    isLogged() {
        return AccountModel.getInstance().account ? true : false;
    }
}
