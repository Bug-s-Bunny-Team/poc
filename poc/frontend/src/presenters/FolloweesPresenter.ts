import { ProfilesModel } from "../models/profilesModel";
import { AccountModel } from "../models/accountModel";
import type { Account, SocialProfile } from "../models";
import { writable, Writable } from "svelte/store";


export class FolloweesPresenter {
    //Ho bisogno dei dati degli utenti che seguo:
    followees: Writable<SocialProfile[]> = writable([]);

    constructor() {
        this.refresh = this.refresh.bind(this);
        // this.handleFollowees = this.handleFollowees.bind(this);
    }

   /* handleFollowees() : void {
       
        const accModel = AccountModel.getInstance().account;
        if(accModel.followers)
        //Todo:
        //Controllo 
            ;
    }*/

    refreshFollowees() {
        fetch("/dev-api/posts")
            .then((response) => response.json())
            .then((data) => {
                this.followees.set(data);
            })
            .catch((err) => {
                console.log(err);
                this.followees.set([]);
            });
    }

    refresh() {
        this.followees.set(null);
        this.refreshFollowees();
    }
}
