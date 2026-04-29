import logo from './logo.svg';
import React,{useState} from 'react';
import './App.css';
import './css/Style.css'

function App() {

  const [id,setId]=useState('');
  const [txtId,setTxtId]=useState('');

  const [name, setName] = useState('');
  const [txtName, setTxtName] = useState('');

  const tBtn=()=>{alert('아이디,이름 저장.');
    setTxtId(id);
    setTxtName(name); 

    // 입력창 초기화
    setId('');
    setName(''); 
  }

  const txtKeyUp=(e)=>{
    if(e.key==='Enter'){
      tBtn();
    }
  }
  

  return (
    <div className="root">
      <div className='txtName'>{txtId}<br/>{txtName}</div>

      <input type= 'text' placeholder='아이디를 입력하세요' value={id} onKeyUp={txtKeyUp} onChange={(e)=>{setId(e.target.value)}}/><br/>
      <input type= 'text' placeholder='이름을 입력하세요' value={name} onKeyUp={txtKeyUp} onChange={(e)=>{setName(e.target.value)}}/><br/>
      
      <button onClick={tBtn}>확인</button>
      
    </div>
  );
}

export default App;