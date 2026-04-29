import logo from './logo.svg';
import './App.css';
import './css/Style.css';
import Nav from './comp/Nav';
import { BrowserRouter,Routes,Route } from 'react-router-dom';
import Home from './pages/Home';
import BList from './pages/BList';
import BWrite from './pages/BWrite';
import UList from './pages/UList';

function App() {
  return (
    <>
    <BrowserRouter>
    <Nav/>
      <div className="root">
        <Routes>
          <Route path='/' element={<Home/>}></Route>
          <Route path='/blist' element={<BList/>}></Route>
          <Route path='/bwrite' element={<BWrite/>}></Route>
          <Route path='/ulist' element={<UList/>}></Route>
        </Routes>
      </div>
      </BrowserRouter>
    </>
  );
}

export default App;
