import Scrape from "./components/Scrape.svelte";
import Results from "./components/Results.svelte";

const routes = [
    {
        name: '/',
        component: Scrape
    },
    {
        name: 'results',
        component: Results
    }
];

export default routes;
