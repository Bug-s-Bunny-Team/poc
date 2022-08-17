<script lang="ts">
    import './style.css';

    import { Router } from "svelte-router-spa";
    import { routes } from "./routes";
</script>

<Router {routes} />

