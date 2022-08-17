import { get, writable, Writable } from 'svelte/store';
import { Location, Position } from '../models'

export class Filter {
    globale: boolean;
    posizione: Position;
    n_risultati: Number;
    raggio: Number;
    min_rating: Number;
}

export class ResultsModel {
    private static resultsModelInstance : ResultsModel = ResultsModel.construct_session();

    private static construct_session() : ResultsModel {
        let rankedList: Location[] = [];
        let str = window.sessionStorage.getItem('ResultsModel.rankedList');
        if(str) {
            rankedList = JSON.parse(str);
            if(rankedList) rankedList.forEach( location => { location.__proto__ = Location.prototype; location.position.__proto__ = Position.prototype; }) // errore del compilatore don't worry
        }

        let result = new ResultsModel();
        result.rankedList.set(rankedList);
        return result;
    }

    private constructor() { 
        this.rankedList.subscribe(rankedList => {
            if(rankedList) window.sessionStorage.setItem('ResultsModel.rankedList', JSON.stringify(rankedList));
            else window.sessionStorage.removeItem('ResultsModel.rankedList');
        })
    }

    static getInstance() : ResultsModel {
        return this.resultsModelInstance;
    }

    rankedList: Writable<Location[]> = writable([]);
    private lastFilter: Filter = null;
    
    // TODO add writable fields and update singleton pattern as per accountModel

    async requestRankedList(filter: Filter) : Promise<Location[]> {
        const response = await fetch('dev-api/results');
        this.rankedList.set(await response.json());
        return get(this.rankedList);
        new Location(0, );
    }

    async getRankedList(filter: Filter) : Promise<Location[]> {
        if(filter != this.lastFilter) {
            this.lastFilter = filter;
            return await this.requestRankedList(this.lastFilter);
        } else {
            return get(this.rankedList);
        }
    }
}
