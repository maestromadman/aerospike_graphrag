// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

const Person = () => {
  return (
    <>
    <h1> Name: Pablo</h1>
    <h2> Last Name: Escobar</h2>
    <h2> Age: 30</h2>
    </>
  )
}

function App() {
  return (
    <> 
      <div className= "App">  
        <Person />
     
      </div>
    </>
  )
}

export default App
