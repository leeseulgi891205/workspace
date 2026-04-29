import logo from './logo.svg';
import './App.css';
import './css/Style.css';
import Nav from './compents/Nav';
import { Routes, Route } from 'react-router-dom';
import BList from './pages/BList';
import BWrite from './pages/BWrite';
import UserList from './pages/UsreList';
import Home from './pages/Home';
import BView from './pages/BView';

function App() {
  return (
    <>
      <Nav />
      <Routes>
        <Route path='/' element={<home/>} />
        <Route path='/blist' element={<BList/>} />
        <Route path='/bwrite' element={<BWrite/>} />
        <Route path='/userlist' element={<UserList/>} />

      </Routes>
    </>
  );
}

export default App;