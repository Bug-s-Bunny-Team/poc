import { ProfilesModel } from "../models/profilesModel";
import { Writable, writable } from "svelte/store";


export class AddProfilesPresenter {

    searchText: string;
    disableButtons: Writable<boolean> = writable(false);

    async search() {
        this.disableButtons.set(true);
        let promise = ProfilesModel.getInstance().getProfiles(this.searchText);
        promise.finally(() => {this.disableButtons.set(false)});
        return await promise;
    }
}
