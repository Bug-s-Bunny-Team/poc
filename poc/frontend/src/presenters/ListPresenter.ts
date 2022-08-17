import type { Location } from "../models";
import type { Writable } from "svelte/store";
import { Filter, ResultsModel } from "../models/resultsModel";

export class ListPresenter {
    constructor() {
        this.refresh = this.refresh.bind(this);
        ResultsModel.getInstance().requestRankedList(new Filter());
    }

    public get locations() : Writable<Location[]> {
        return ResultsModel.getInstance().rankedList;
    }

    refresh() {
        ResultsModel.getInstance().requestRankedList(new Filter());
    }

}
