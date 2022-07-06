import Scrape from "./components/Scrape.svelte";
import Posts from "./components/Posts.svelte";

const routes = [
    {
        name: '/',
        component: Scrape
    },
    {
        name: 'posts',
        component: Posts
    }
];

export default routes;
