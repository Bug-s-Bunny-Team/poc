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
        await new Promise(r => setTimeout(r, 500))
        const response = await fetch('dev-api/profiles');
        return await response.json();
    }

    async removeFollowee(profile: SocialProfile) : Promise<void> {
        await new Promise(r => setTimeout(r, 500))
    }

    async getMostPopularProfiles(quantity: number) : Promise<SocialProfile[]> {
        await new Promise(r => setTimeout(r, 500))
        const response = await fetch('dev-api/profiles');
        return await response.json();
    }

    async getProfiles(ricerca: String) : Promise<SocialProfile[]> {
        await new Promise(r => setTimeout(r, 500))
        const response = await fetch('dev-api/profiles');
        return await response.json();
    }

    async followProfile(profile: SocialProfile) : Promise<void> {
        await new Promise(r => setTimeout(r, 500))
    }
}  
 
  