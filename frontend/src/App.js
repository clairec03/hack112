// Source: https://mui.com/components/switches/#label
import React, {useState, useEffect} from 'react'
// import './App.css'
import Logo from './components/Logo'
import BasicSwitch from './components/BasicSwitch'
import TranslatorCon from './components/TranslatorCon'
import {makeStyles} from '@material-ui/core'
import Searchbar from './components/Searchbar'

const useStyles = makeStyles(theme => ({
  container: {
    display:'flex',
   flexDirection: 'column',
    justifyContent:'center',
    // justifyContent: 'center'
    margin: 20
},
topContainer:{
  display: 'flex',
  flexDirection:'row',
  alignItems:'center'

},
translatorCon:{
  
}


}) )

function App() {

  const [searchValue, setSearchValue] = useState('')

  const onChange = event => {
    setSearchValue(event.target.value)
  }

  const handleSearch = (something) =>{
    return null
  }
  
  const classes = useStyles()
  return (
    
    <div className={classes.container}>
       <Logo />
       <div className={classes.topContainer}>
       <h2>Bridging the Cultural Gap across Generations</h2>
       </div>
       <TranslatorCon className={classes.translatorCon} />
       
       {/* <div className={classes.inline}>
        <TextField
        onChange={onChange}
          id="outlined-search"
          label={'Search'}
          value={'hi'}
          variant="standard"
          color='success'
        />
        <Button onClick={onSearch}>Search</Button>
        </div> */}
       
    </div>

  )  
}

export default App;
