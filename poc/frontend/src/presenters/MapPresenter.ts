import { Filter, ResultsModel } from "../models/resultsModel";
import { writable, Writable } from "svelte/store";
import type { Location } from "../models"

export class MapPresenter {
    rankedList: Writable<Promise<Location[]>> = writable(null);

    constructor() {
        this.rankedList.set(ResultsModel.getInstance().getRankedList(new Filter()));
    }


}
