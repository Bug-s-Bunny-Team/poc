import { ProfilesModel } from "../models/profilesModel";

export class FolloweesPresenter {
    //Ho bisogno dei dati degli utenti che seguo:
    id: number;
    username: string;

    accountname: string;
    email: string;
    password: string;
    preference: boolean;
    followers: number;
}
