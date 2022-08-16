import MainLayout from "../components/MainLayout.svelte";
import Scrape from "../pages/Scrape.svelte";
import ListView from "../pages/ListView.svelte";
import ChangePsw from "../pages/ChangePsw.svelte"
import Account from "../pages/Account.svelte";
import Explore from "../pages/Explore.svelte";
import Followees from "../pages/Followees.svelte";
import Map from "../pages/Map.svelte";
import AddProfile from "../pages/AddProfile.svelte";

const ProtectedRoutes = [
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
        name: '/scrape',
        title: 'Scrape',
        component: Scrape,
        layout: MainLayout
    },
    {
        name: '/map',
        title: 'Map',
        component: Map,
        layout: MainLayout
    },
    {
        name: '/add',
        title: 'Add',
        component: AddProfile,
        layout: MainLayout
    },
    {
        name: '/explore',
        title: 'Explore',
        component: Explore,
        layout: MainLayout
    },
    {
        name: '/followees',
        title: 'Followees',
        component: Followees,
        layout: MainLayout
    },
    {
        name: '/listview',
        title: 'ListView',
        component: ListView,
        layout: MainLayout
    }
];

export { ProtectedRoutes }
