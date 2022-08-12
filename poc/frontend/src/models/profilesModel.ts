import { Account, SocialProfile } from '../models'

export class ProfilesModel {
    private static profilesModelInstance = new ProfilesModel();

    private constructor() {}

    static getInstance() : ProfilesModel {
        return this.profilesModelInstance;
    }


    getFollowees(account: Account) : SocialProfile[] {
        return [new SocialProfile()];
    }

    removeFollowee(profile: SocialProfile) : void {

    }

    getMostPopularProfiles(quantity: Number) : SocialProfile[] {
        return [new SocialProfile()];
    }

    getProfiles(ricerca: String) : SocialProfile[] {
        return [new SocialProfile()];
    }

    followProfile(profile: SocialProfile, self_account: Account) : void {
        
    }
}  
 
  