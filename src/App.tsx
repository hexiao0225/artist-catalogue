import { useEffect } from 'react'
import { Route, Routes, useLocation } from 'react-router-dom'
import ErrorBoundary from './components/ErrorBoundary'
import Footer from './components/Footer'
import Header from './components/Header'
import AboutPage from './pages/AboutPage'
import ArtistPage from './pages/ArtistPage'
import IndexPage from './pages/IndexPage'
import NotFound from './pages/NotFound'
import SlidesPage from './pages/SlidesPage'

export default function App() {
  const { pathname } = useLocation()
  // Block body on purpose: some browsers return a Promise from scrollTo, which React would
  // treat as a cleanup function and crash on the next navigation.
  useEffect(() => {
    window.scrollTo(0, 0)
  }, [pathname])

  if (pathname.startsWith('/slides')) {
    return (
      <ErrorBoundary key={pathname}>
        <Routes>
          <Route path="/slides" element={<SlidesPage />} />
          <Route path="/slides/:slug" element={<SlidesPage />} />
        </Routes>
      </ErrorBoundary>
    )
  }

  return (
    <>
      <Header />
      <main>
        <ErrorBoundary key={pathname}>
          <Routes>
            <Route path="/" element={<IndexPage />} />
            <Route path="/artists/:slug" element={<ArtistPage />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </ErrorBoundary>
      </main>
      <Footer />
    </>
  )
}
