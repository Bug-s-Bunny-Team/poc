import { Filter, ResultsModel } from "../models/resultsModel";

export class ListPresenter {

    async refresh() {
        return await ResultsModel.getInstance().getRankedList(new Filter());
    }

}
