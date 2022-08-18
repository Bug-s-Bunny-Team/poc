import { writable, Writable } from "svelte/store";
import { Filter, ResultsModel } from "../models/resultsModel";

export class ListPresenter {

    disableButtons: Writable<boolean> = writable(false);

    async refresh() {
        this.disableButtons.set(true);
        let promise = ResultsModel.getInstance().getRankedList(new Filter());
        promise.finally(() => {this.disableButtons.set(false)});
        return await promise;
    }

}
