// import { useState } from 'react'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const name = 'Pablo Escobar';
  return (
    <>
      <div className= "App">
        <h1> Hello, {2 + 2}!</h1>
        {name ? (
          <> 
            test
          </>
        ) : (
          <>
          <h1>test</h1>
          <h2>There is no name</h2>
          </>
        )}

      </div>
    </>
  )
}

export default App
