import { Link } from 'react-router-dom'
import { REPO_URL } from '../config'

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="wrap site-footer__inner">
        <p>
          A working catalogue kept for study. Images are credited to their rights holders and
          reproduced for reference only.
        </p>
        <p className="site-footer__links">
          <Link to="/about">How to add an artist</Link>
          <a href={REPO_URL}>Source on GitHub</a>
        </p>
      </div>
    </footer>
  )
}
