import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
function App() {
  const [message, setMessage] = useState('Loading...')

  useEffect(() => {
    fetch('http://0.0.0.0:8000/')
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage('Failed to load message'))
  }, [])

  return (
    <div style={{ textAlign: 'center', marginTop: '2rem' }}>
      <h1>Hello from React</h1>
      <p>Backend says: {message}</p>
    </div>
  )
}

export default App