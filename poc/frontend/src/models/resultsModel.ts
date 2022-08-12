import { Location } from '../models'

export class Filter {
    globale: boolean;
    luogo: Location;
    n_risultati: Number;
    raggio: Number;
    min_rating: Number;
}

export class ResultsModel {

    private static resultModelInstance = new ResultsModel();

    private constructor() {}

    static getInstance() : ResultsModel {
        return this.resultModelInstance;
    }

    rankedList: Location[];
    
    getRankedList(filter: Filter) : Location[] {
        let result: Location[] = [new Location()];
        this.rankedList = result;
        return this.rankedList;
    }

}
