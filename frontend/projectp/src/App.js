import MAINPAGE2 from './components/MAINPAGE2';
import { ToastContainer } from 'react-toastify';
import HOME from './components/HOME';
import 'react-toastify/dist/ReactToastify.css';
import { base }  from './Utils/post';


import './App.css';

function App() {
  return (
    <div className="App">
      <HOME />
      <MAINPAGE2/>
      <ToastContainer />
    </div>
  );
}

export default App;