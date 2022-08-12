import MainLayout from "./components/MainLayout.svelte";
import Scrape from "./pages/Scrape.svelte";
import Posts from "./pages/Posts.svelte";
import Login from "./pages/Login.svelte";
import Register from "./pages/Register.svelte";
import ChangePsw from "./pages/ChangePsw.svelte"
import Account from "./pages/Account.svelte";

const routes = [
    {
        name: '/login',
        title: 'Login',
        component: Login,
        layout: MainLayout
    },
    {
        name: '/register',
        title: 'Register',
        component: Register,
        layout: MainLayout
    },
    {
        name: '/changepsw',
        title: 'ChangePassword',
        component: ChangePsw,
        layout: MainLayout
    },
    {
        name: '/account',
        title: 'Account',
        component: Account,
        layout: MainLayout
    },
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
