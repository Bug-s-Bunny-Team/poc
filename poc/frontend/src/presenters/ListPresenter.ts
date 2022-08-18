import { Filter, ResultsModel } from "../models/resultsModel";

export class ListPresenter {
    constructor() {
        this.refresh = this.refresh.bind(this);
    }

    async refresh() {
        return await ResultsModel.getInstance().getRankedList(new Filter());
    }

}
