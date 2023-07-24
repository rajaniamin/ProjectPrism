import React from 'react'
import {Routes,Route} from "react-router-dom"
import Homepage from './HOMEPAGE'
import SIGNUP from './SIGNUP.jsx'

const MAINPAGE2 = () => {
    return (
        <Routes>
            <Route path='/' element={<SignupForm/>}/>
            <Route path='/home' element={<Homepage/>}/>
        </Routes>
      )
}

export default MAINPAGE2