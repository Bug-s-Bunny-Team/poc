import { Location } from '../models'

export class Filter {
    globale: boolean;
    luogo: Location;
    n_risultati: Number;
    raggio: Number;
    min_rating: Number;
}

export class ResultsModel {
    private static resultsModelInstance : ResultsModel = ResultsModel.construct_session();

    private static construct_session() : ResultsModel {
        let result : ResultsModel = JSON.parse(window.sessionStorage.getItem('ResultsModel'));
        if(!result) {
            result = new ResultsModel();
            window.sessionStorage.setItem('ResultsModel', JSON.stringify(result));
        }
        return result;
    }

    private constructor() { }

    static getInstance() : ResultsModel {
        return this.resultsModelInstance;
    }

    rankedList: Location[];
    
    getRankedList(filter: Filter) : Location[] {
        let result: Location[] = [new Location()];
        this.rankedList = result;
        return this.rankedList;
    }

    private save_to_session() {
        window.sessionStorage.setItem('ResultsModel', JSON.stringify(this));
    }
}
