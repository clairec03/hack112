// Source: https://create-react-app.dev/docs/adding-images-fonts-and-files/
import React from 'react';
import logo from '../assets/genzlator.png'


function Logo() {
  // Import result is the URL of your image
  return <img src={logo} alt="Logo" className='logo'/>;
}

export default Logo