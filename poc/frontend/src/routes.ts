import MainLayout from "./components/MainLayout.svelte";
import Scrape from "./pages/Scrape.svelte";
import Posts from "./pages/Posts.svelte";

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
