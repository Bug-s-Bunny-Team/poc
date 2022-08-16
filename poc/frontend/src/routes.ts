import { PublicRoutes } from './routes/PublicRoutes'
import { ProtectedRoutes } from './routes/ProtectedRoutes'

const routes = [...PublicRoutes, ...ProtectedRoutes]

export default routes;
