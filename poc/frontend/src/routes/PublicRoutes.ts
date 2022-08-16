import Login from "../pages/Login.svelte";
import Register from "../pages/Register.svelte";
import MainLayout from "../components/MainLayout.svelte";
import FirstPage from "../pages/FirstPage.svelte"

const PublicRoutes = [
    {
        name: '/',
        title: 'FirstPage',
        component: FirstPage,
        layout: MainLayout
    },
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
    }
]

export { PublicRoutes }
