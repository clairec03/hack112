import React, {useState, useEffect} from 'react'
import TextForm from './TextForm'
import {Deploy} from './Deploy'
import {Button, Typography, useStyles} from '@material-ui/core'
import HoverableText from './components/Hover.js'

const useStyles = makeStyles(theme => ({
    translatorContainer: {
        
    }


}) )

function TranslatorCon(){
    const [input, setInput] = useState('')
    const [output, setOutput] = useState('')
    const prefix = '/api'
  
    // useEffect(() => {
    //   fetch(prefix).then(response => {
    //     if(response.status === 200){
    //       return response.json()
    //     }  
    //   }).then(data => {
    //     console.log(data)
    //     setInput(data)})
    //   .then(error => console.log(error))
    // }, [])
  
    const onTranslate = () => {
        console.log(input)
      fetch(prefix, {
        method:'POST',
        headers:{
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(input)
      }).then(response => response.json()).then(
        data => {
            setOutput(data)
            console.log('success', output)}
      )
    }

    const createOutput  = (string) => 
    {
        return "You typed " + string + " you absolute cunt"
    }

    const handleInput = (event) => {
        setInput(event.target.value)
        console.log(event.target.value)
    }

    return (
    <div>
       <h2 className='heading'>Bridging the Cultural Gap across Generations</h2>
       <div className='translationContainer'>
       <TextForm
       onChange={handleInput}
       label="Enter a sentence"
       />
       <Typography variant='h2'>
       {createOutput(output)} 
       
       </Typography>

       <Button variant='outlined'
       onClick={onTranslate}
       >GENZLATE</Button>
       <Deploy data={input.slang} />
       </div> 
        </div>
      
    )
  

}

export default TranslatorCon