import { ProfilesModel } from "../models/profilesModel";

export class ExplorePresenter{

    async refresh() {
        return await ProfilesModel.getInstance().getMostPopularProfiles(20);
    }
}
