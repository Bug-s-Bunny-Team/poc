import { ProfilesModel } from "../models/profilesModel";
import { AccountModel } from "../models/accountModel";
import type { Account, SocialProfile } from "src/models";

export class FolloweesPresenter {
    //Ho bisogno dei dati degli utenti che seguo:
    followees: Array<SocialProfile> = [];

    constructor() {
        this.handleFollowees = this.handleFollowees.bind(this);
    }

    handleFollowees() : void {
       
        const accModel = AccountModel.getInstance().account;
        if(accModel.followers)
        //Todo:
        //Controllo 
            this.followees = ProfilesModel.getInstance().getFollowees(accModel);
    }

    refreshFollowees() : void {
        fetch("/dev-api/posts") //Da cambiare per poter fetchare i "social profiles".
            .then((response) => response.json())
            .then((data) => {
                this.followees = data;
            })
    }

    refresh() : void {
        this.followees = null;
        this.refreshFollowees();
    }

    getFollowees() : Array<SocialProfile> {
        return this.followees;
    }
}
