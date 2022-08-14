import { ProfilesModel } from "../models/profilesModel";
import type { Account } from "src/models";

export class ExplorePresenter{

    accounts: Array<Account> = [];

    constructor() {
        this.handleExplore = this.handleExplore.bind(this);
    }
    
    refreshAccounts() {
        fetch("/dev-api/post") //Fetch per ACCOUNT della piattaforma!!
            .then((response) => response.json())
            .then((data) => {
                this.accounts = data;
            })
            .catch((err) => {
                console.log(err);
                this.accounts = [];
            });
    }

    refresh() {
        this.accounts = null;
        this.refreshAccounts();
    }

    handleExplore() : void {
        const profilesModel = ProfilesModel.getInstance();
        profilesModel.getMostPopularProfiles(20);
    }
}
