import type { Account, SocialProfile } from '../models'

export class ProfilesModel {
    private static profilesModelInstance : ProfilesModel = ProfilesModel.construct_session();

    private static construct_session() : ProfilesModel {
        let result = new ProfilesModel();
        return result;
    }

    private constructor() { 
    }

    static getInstance() : ProfilesModel {
        return this.profilesModelInstance;
    }

    async getFollowees() {
        const response = await fetch('dev-api/profiles');
        return await response.json();
    }

    removeFollowee(profile: SocialProfile) : void {
    }

    getMostPopularProfiles(quantity: number) : SocialProfile[] {
        return [];
    }

    async getProfiles(ricerca: String) : Promise<SocialProfile[]> {
        const response = await fetch('dev-api/profiles');
        return await response.json();
    }

    followProfile(profile: SocialProfile, self_account: Account) : void {
    }
}  
 
  