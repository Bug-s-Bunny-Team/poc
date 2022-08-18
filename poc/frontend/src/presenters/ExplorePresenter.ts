import { writable, Writable } from "svelte/store";
import { ProfilesModel } from "../models/profilesModel";

export class ExplorePresenter{

    disableButtons: Writable<boolean> = writable(false);

    async refresh() {
        this.disableButtons.set(true);
        let promise = ProfilesModel.getInstance().getMostPopularProfiles(20);
        promise.finally(() => {this.disableButtons.set(false)});
        return await promise;   
    }
}
