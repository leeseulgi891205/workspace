import { useState } from 'react';
import './css/Style.css';

function App() {

  //자바스크립트 변수선언
  let id = 'aaaa';

  // useState변수 선언
  // 변수가 2개지정 , 1개는 변수, 1개는 값을 변경할때 쓰는 변수
  const [userId, setUserId] = useState('abc');
  console.log("abc 변수 값 : ",userId);
  

  // 내부함수선언 하는 위치
  const loginBtn1 = () => {
    alert('변수의 값 변경!!');
    // id = 'bbbb';
    // console.log("aaaa 변수 값 변경 : ",id);
    setUserId('bbbb');
    console.log("abc 변수 값 변경 : ",userId);
    

    


    
    
  }

 // 함수선언 방법 3가지
  const loginBtn2 = function() {
    alert('loginBtn2 클릭되었습니다.');
    
  }
  // 함수선언 방법 3가지
  function loginBtn3() {
    alert('loginBtn3 클릭되었습니다.');
    
  }


  return (
    <div className="App">
      <h2>메인페이지입니다.</h2>
      <div className='txt'>{userId}님 환영합니다.</div>
      <input type="text" placeholder='아이디를 입력하세요.'/>
      <br />
      <button onClick={loginBtn1}>로그인</button>
    </div>
  );
}

export default App;
