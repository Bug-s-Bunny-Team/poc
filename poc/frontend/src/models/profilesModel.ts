import { get, writable, Writable } from 'svelte/store';
import { Account, SocialProfile } from '../models'

export class ProfilesModel {
    private static profilesModelInstance : ProfilesModel = ProfilesModel.construct_session();

    private static construct_session() : ProfilesModel {
        let following: SocialProfile[] = [];
        let str = window.sessionStorage.getItem('ProfilesModel.following');
        if(str) {
            following = JSON.parse(str);
            if(following) following.forEach( followee => { followee.__proto__ = SocialProfile.prototype; }) // errore del compilatore don't worry
        }

        let result = new ProfilesModel();
        result.following.set(following);
        return result;
    }

    private constructor() { 
        this.following.subscribe(following => {
            if(following) window.sessionStorage.setItem('ProfilesModel.following', JSON.stringify(following));
            else window.sessionStorage.removeItem('ProfilesModel.following');
        })
    }

    static getInstance() : ProfilesModel {
        return this.profilesModelInstance;
    }

    following: Writable<SocialProfile[]> = writable([]);

    // TODO add writable fields and update session singleton pattern

    async getFollowers() : Promise<number> {
        return this.getFollowees().length;
    }

    async requestFollowees(account: Account) : Promise<SocialProfile[]> {
        const response = await fetch('dev-api/profiles');
        this.following.set(await response.json());
        return get(this.following);
    }

    removeFollowee(profile: SocialProfile) : void {
        this.following.update(following => { following.splice(following.findIndex(soc_prof => { return soc_prof.id == profile.id}), 1); return following; })
    }

    getMostPopularProfiles(quantity: Number) : SocialProfile[] {
        return [];
    }

    getProfiles(ricerca: String) : SocialProfile[] {
        return [];
    }

    followProfile(profile: SocialProfile, self_account: Account) : void {
        this.following.update(following => { following.push(profile); return following; });
    }

    getFollowees() {
        return get(this.following);
    }
}  
 
  