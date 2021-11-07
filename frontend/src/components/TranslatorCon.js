import React, {useState, useEffect} from 'react'
import TextForm from './TextForm'
import {Deploy} from './Deploy'
import {Button, Typography, makeStyles, Fade} from '@material-ui/core'
import DefinitionTable from './DefinitionTable'



const useStyles = makeStyles(theme => ({
    translatorContainer: {
        display:'flex',
       flexDirection: 'column',
        justifyContent:'center',
        // justifyContent: 'center'
        margin: 20
        
    },

    mainContainer: {
        display:'flex',
      
        flexDirection: 'column',
        justifyContent:'center'
        
    },

    highlightTextStyle:{
        textDecoration: 'none',
        color:'black',
        transition: "background 1.5s color 1.5s",
        "&:hover": {  
            color: "red"
          }
    },

    inline:{
        display: 'flex',
        flexDirection:'row',
        m:2
        
    },
    button:{
        marginTop:30,
        backgroundColor: "#613dc1",
        color:'White',
        transition: "background 1.5s color 1.5s",
        "&:hover": {  
            backgroundColor:'#858ae3'
          }
    }



}) )

function TranslatorCon(){
    const [input, setInput] = useState('')
    const [output, setOutput] = useState([])
    const [error, setErrorTrue] = useState(false)
    const prefix = '/api'
    const classes = useStyles()
  
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
        headers : { 
            'Content-Type': 'application/json',
            'Accept': 'application/json'
           },
        body: JSON.stringify('__1__'+ input)
      }).then(response => response.json()).then(
        data => {
            if(data !== null){
                setErrorTrue(false)
                console.log('running here')
                setOutput(data.output)
                console.log(data.output)
                console.log('success', data.output)
            }
            else{
                setErrorTrue(true)
                setOutput(null)
            }

            
        }).then(error => console.log(error))
    }

    const handleInput = (event) => {
        setInput(event.target.value)
        // console.log(event.target.value)
    }


    return (
    <div className={classes.mainContainer}>
       <div className={classes.translatorContainer}>
       <TextForm
       onChange={handleInput}
       label="Enter a sentence"
       />
       <Button variant='outlined'
       onClick={onTranslate}
       className={classes.button}
       >GENZLATE</Button>
       </div> 
       {error && 
       <div>
       <Typography variant='h6'>
       No Slang Words Detected</Typography>
       </div>
       }

        {
            output !== null && Object.keys(output).map(function(key){
                console.log('hii', key, output[key].Word)
                return (
                    // <Typography>
                    //     {output[key].Word}
                    // </Typography>
                    <DefinitionTable
                    word={output[key].Word}
                    def={output[key].Definition}
                    ex={output[key].Example}
                    pos={output[key].pos}

                />
                )
            })
        }

        </div>
      
    )
  

}

export default TranslatorCon