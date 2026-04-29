import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';
import Number from './comp/Number';
import Nav from './comp/Nav';
import From from './comp/form';
import Card from './comp/card';
import Mina from './comp/mina';

function App() {
  
  let btnName = '확인';
  let number = 100;

  return (
    <div className="App">

      <Nav/>
      {/* 컴퍼넌트로 값을 넘기는 방법 : props - 변수=값, 함수, 변수, 함수, useState */}
      <Number btnName={btnName} number={number}/>

      <Mina/>

      <From/>

    {/* card */}
    <Card/>


</div>

  );
}

export default App;
