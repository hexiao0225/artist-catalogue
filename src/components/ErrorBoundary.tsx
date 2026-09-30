import { Component, type ReactNode } from 'react'
import { Link } from 'react-router-dom'

interface State {
  error: Error | null
}

/** Shows a message instead of a blank page if a view crashes. Keyed on the route so navigating recovers. */
export default class ErrorBoundary extends Component<{ children: ReactNode }, State> {
  state: State = { error: null }

  static getDerivedStateFromError(error: Error): State {
    return { error }
  }

  render() {
    if (!this.state.error) return this.props.children
    return (
      <div className="wrap page-intro">
        <h1 className="display">Something went wrong</h1>
        <p className="lede">
          This page failed to load. <Link to="/">Back to all artists</Link>
        </p>
      </div>
    )
  }
}
