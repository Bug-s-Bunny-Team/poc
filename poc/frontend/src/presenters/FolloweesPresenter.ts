import { ProfilesModel } from "../models/profilesModel";
import { AccountModel } from "../models/accountModel";
import type { Account, SocialProfile } from "../models";
import { writable, Writable } from "svelte/store";

export class FolloweesPresenter {

    profiles: Writable<Promise<SocialProfile[]>> = writable(null);

    constructor() {
        this.refresh = this.refresh.bind(this);
        this.removeFollowee = this.removeFollowee.bind(this);
    }

    refresh() : void {
        let promise = ProfilesModel.getInstance().getFollowees();
        this.profiles.set(promise);    
    }

    async removeFollowee(followee: SocialProfile) : Promise<void> {
        ProfilesModel.getInstance().removeFollowee(followee).then(this.refresh);
    }
}
