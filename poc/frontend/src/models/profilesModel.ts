import { Account, SocialProfile } from '../models'

export class ProfilesModel {
    private static profilesModelInstance : ProfilesModel = ProfilesModel.construct_session();

    private static construct_session() : ProfilesModel {
        let result : ProfilesModel = JSON.parse(window.sessionStorage.getItem('ProfilesModel'));
        if(!result) {
            result = new ProfilesModel();
            window.sessionStorage.setItem('ProfilesModel', JSON.stringify(result));
        } else {
            result.__proto__ = ProfilesModel.prototype; // errore del compilatore don't worry
        }
        return result;
    }

    private constructor() { }

    static getInstance() : ProfilesModel {
        return this.profilesModelInstance;
    }


    getFollowees(account: Account) : SocialProfile[] {
        return [new SocialProfile()];
    }

    removeFollowee(profile: SocialProfile) : void {

        this.save_to_session();
    }

    getMostPopularProfiles(quantity: Number) : SocialProfile[] {
        return [new SocialProfile()];
    }

    getProfiles(ricerca: String) : SocialProfile[] {
        return [new SocialProfile()];
    }

    followProfile(profile: SocialProfile, self_account: Account) : void {
        
        this.save_to_session();
    }

    private save_to_session() {
        window.sessionStorage.setItem('ProfilesModel', JSON.stringify(this));
    }
}  
 
  