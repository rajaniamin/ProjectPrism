import React from 'react'
import "./NAV.css"
const NAV = ({setNav}) => {
    const changeNavState=(event)=>{
        setNav(event.target.innerText)
    }

  return (
    <div className="navbar">
        
      <button onClick={changeNavState}>Project Dashboard</button>
      <button onClick={changeNavState}>Project Manager</button>
      <button onClick={changeNavState}>Task Manager</button>
      <button onClick={changeNavState}>Resource Manager</button>
      <button onClick={changeNavState}>Log Out</button>
    </div>
  )
}

export default NAV