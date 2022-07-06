import MainLayout from "./components/MainLayout.svelte";
import Scrape from "./components/Scrape.svelte";
import Posts from "./components/Posts.svelte";

const routes = [
    {
        name: '/',
        title: 'Scrape',
        component: Scrape,
        layout: MainLayout
    },
    {
        name: '/posts',
        title: 'Posts',
        component: Posts,
        layout: MainLayout
    }
];

export default routes;
