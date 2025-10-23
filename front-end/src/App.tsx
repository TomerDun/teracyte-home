import { useEffect } from 'react'
import './App.css'
import HomePage from './pages/HomePage'
import { loginUser } from './services/authService'
import Routing from './Routing'

function App() {  
  useEffect(() => {
    const token = localStorage.getItem('apiToken');
    if (!token) {
      loginUser('tomer', 'Tomer123');
    }
  }, [])
  return (
    <>
      <Routing />
    </>
  )
}

export default App
