import { AccountModel } from "../models/accountModel";
import { ProtectedRoutes, PublicRoutes } from "../routes";
import { writable, Writable } from "svelte/store";

export class AppPresenter {
    routes: Writable<any[]> = writable();

    constructor() {
        AccountModel.getInstance().account.subscribe(account => {
            if(account) { this.routes.set(ProtectedRoutes); }
            else { this.routes.set(PublicRoutes); }
        })
    }
}
