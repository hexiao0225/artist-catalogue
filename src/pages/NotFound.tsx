import { Link } from 'react-router-dom'

export default function NotFound() {
  return (
    <div className="wrap page-intro">
      <h1 className="display">Not found</h1>
      <p className="lede">
        Nothing hangs here. <Link to="/">Back to all artists</Link>
      </p>
    </div>
  )
}
