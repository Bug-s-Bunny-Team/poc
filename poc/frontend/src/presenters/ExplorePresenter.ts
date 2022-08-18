import { ProfilesModel } from "../models/profilesModel";
import type { Account } from "../models";
import { writable, Writable } from "svelte/store";

export class ExplorePresenter{

    accounts: Writable<Account[]> = writable([]);

    //https://svelte.dev/tutorial/writable-stores

    constructor() {
        this.refresh = this.refresh.bind(this);
    }

    refreshAccounts() {
         fetch("/dev-api/posts")
             .then((response) => response.json())
             .then((data) => {
                 this.accounts.set(data);
             })
             .catch((err) => {
                 console.log(err);
                 this.accounts.set([]);
             });
    }
 
    refresh() {
         this.accounts.set(null);
         this.refreshAccounts();
    }
 

    handleExplore() : void {
        const profilesModel = ProfilesModel.getInstance();
        profilesModel.getMostPopularProfiles(20);
    }
}
