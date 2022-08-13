import { ProfilesModel } from "../models/profilesModel";

export class ExplorePresenter{

    constructor() {
        this.handleExplore = this.handleExplore.bind(this);
    }

    handleExplore() : void {
        const profilesModel = ProfilesModel.getInstance();
        profilesModel.getMostPopularProfiles(20);
    }
}
