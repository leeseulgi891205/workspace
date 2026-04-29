import logo from './logo.svg';
import './App.css';
import './css/Style.css'; 
// 1. useRef를 import 목록에 추가해야 합니다.
import React, {useState, useRef} from 'react';

function App() {

  const [count, setCount] = useState(0);
  const [inputText, setInputText] = useState('');
  
  // 2. 에러가 났던 부분 수정 (count -> const)
  const numRef = useRef(0); 
  
  // --- 기존 코드 내용 ---
  const countBtn = () => setCount(count + 1);

  const addInputVal = () => {
    const num = Number(inputText);
    if (isNaN(num)) {
      alert("숫자만 입력해주세요!");
      // 포커스 이동
      numRef.current.focus();
      setInputText('');
      return;
    }
    setCount(count + num);
    setInputText(''); 
  }

  const activeEnter = (e) => {
    if(e.key === "Enter") addInputVal();
  }

  // --- 로그인 기능 ---
  const [inputId, setInputId] = useState('');
  const [inputPw, setInputPw] = useState('');

  const [showId, setShowId] = useState('');
  const [showPw, setShowPw] = useState('');

  const loginBtn = () => {
    setShowId(inputId);
    setShowPw(inputPw);
    alert("로그인되었습니다");
  }

  const loginEnter = (e) => {
    if(e.key === "Enter") {
      loginBtn();
    }
  }

  return (
    <div className="root">
      <h2>메인페이지</h2>
      <div className='txt'>현재 숫자 : {count}</div>
      <input ref={numRef}
        type='text' 
        placeholder='숫자를 입력하고 엔터' 
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        onKeyDown={activeEnter}
      /><br/>
      <button onClick={countBtn}>1 증가</button>
      <button onClick={addInputVal}>입력값 더하기</button>
      
      <hr/>

      <h2>로그인</h2>
      
      <div className='txt'>아이디 : {showId}</div>
      <input 
        type='text' 
        placeholder='아이디를 입력하세요'
        value={inputId}
        onChange={(e) => setInputId(e.target.value)}
        onKeyDown={loginEnter} 
      /><br/>
      
      <div className='txt'>비밀번호 : {showPw}</div>
      <input 
        type='password' 
        placeholder='비밀번호를 입력하세요'
        value={inputPw}
        onChange={(e) => setInputPw(e.target.value)}
        onKeyDown={loginEnter}
      /><br/>
      
      <button onClick={loginBtn}>로그인</button>

    </div>
  );
}

export default App;