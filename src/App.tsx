import { useEffect } from 'react'
import { Route, Routes, useLocation } from 'react-router-dom'
import Footer from './components/Footer'
import Header from './components/Header'
import AboutPage from './pages/AboutPage'
import ArtistPage from './pages/ArtistPage'
import IndexPage from './pages/IndexPage'
import NotFound from './pages/NotFound'
import SlidesPage from './pages/SlidesPage'

export default function App() {
  const { pathname } = useLocation()
  useEffect(() => window.scrollTo(0, 0), [pathname])

  if (pathname.startsWith('/slides')) {
    return (
      <Routes>
        <Route path="/slides" element={<SlidesPage />} />
        <Route path="/slides/:slug" element={<SlidesPage />} />
      </Routes>
    )
  }

  return (
    <>
      <Header />
      <main>
        <Routes>
          <Route path="/" element={<IndexPage />} />
          <Route path="/artists/:slug" element={<ArtistPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </main>
      <Footer />
    </>
  )
}
