// Source: https://mui.com/components/switches/#label
import React, {useState, useEffect} from 'react'
// import './App.css'
import Logo from './components/Logo'
import BasicSwitch from './components/BasicSwitch'
import TranslatorCon from './components/TranslatorCon'
import {Button} from '@material-ui/core'
import HoverableText from './components/Hover.js'

function App() {
  
  return (
    
    <div className="app">
       <Logo />
       <TranslatorCon />
       <BasicSwitch defaultChecked />
    </div>

  )  
}

export default App;
