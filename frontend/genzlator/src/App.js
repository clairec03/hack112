import React, {useState, useEffect} from 'react'
// import './App.css'
// import TextForm from './components/TextForm'
import {Button} from '@material-ui/core'
import {Deploy} from './components/Deploy'

function App() {
  const [msg, setMsg] = useState('hii')
  

  useEffect(() => {
    fetch('/api', {
      body: JSON.stringify(msg),
    }).then(response => {
      if(response.status === 200){
        return response.json()
      }  
    }).then(data => {
      console.log(data)
      setMsg(data)})
    .then(error => console.log(error))
  }, [])

  const onTranslate = () => {
    fetch('/api')
  }

  return (
    <div className="app">
      <h1 className='heading'>Welcome to Genzlator!</h1>
       <div className='translationContainer'>
       {/* <TextForm
       />
       
       <TextForm 
       disabled={true}/> */}

       <Button onClick={onTranslate}>TRANSLATE</Button>
       <Deploy data={msg.slang} />
       </div> 
        
    </div>

  )
  
}

export default App;
