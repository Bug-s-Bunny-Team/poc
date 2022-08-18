import { ProfilesModel } from "../models/profilesModel";
import type { Account, SocialProfile } from "../models";


export class AddProfilesPresenter {

    searchText: string;

    constructor() {
    }

    async search() {
        return await ProfilesModel.getInstance().getProfiles(this.searchText);
    }
}
