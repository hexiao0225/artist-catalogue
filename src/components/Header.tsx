import { Link, NavLink } from 'react-router-dom'

export default function Header() {
  return (
    <header className="site-header">
      <div className="wrap site-header__inner">
        <Link to="/" className="wordmark" aria-label="Artist Catalogue, home">
          <span className="wordmark__main">Catalogue</span>
          <span className="wordmark__sub">of artists to study</span>
        </Link>
        <nav className="site-nav" aria-label="Main">
          <NavLink to="/" end>
            Artists
          </NavLink>
          <Link to="/slides">Slides</Link>
          <NavLink to="/about">How to add</NavLink>
        </nav>
      </div>
    </header>
  )
}
