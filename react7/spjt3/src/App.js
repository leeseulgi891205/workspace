import React, { useState, useRef, useEffect } from 'react';
import './App.css';
import './css/Style.css'; 

function App() {

  // =========================================================================
  // [1. 변수 선언부] 
  // 오류 수정: 변수 선언을 useEffect보다 먼저 해야 에러가 나지 않습니다.
  // =========================================================================

  // useState변수의 특징 - 1) 값이 바뀌면 리렌더링이 발생 2) 컴포넌트가 리렌더링 되면 값이 초기화되지 않고 유지됨
  const [cnt, setCnt] = useState(0); // State (상태 변수)
  const [id, setId] = useState('aaa'); // State (상태 변수)

  // useRef변수의 특징 - 1) 값이 바뀌어도 리렌더링이 발생하지 않음 2) 컴포넌트가 리렌더링 되어도 값이 유지됨
  // useRef : current키에 값을 저장 cntRef.current
  const cntRef = useRef(10); // 초기값 10
  
  let count = 0; // 일반 변수 (리렌더링 시 0으로 초기화됨)


  // =========================================================================
  // [2. useEffect] 
  // 이제 cnt가 위에서 선언되었으므로 안전하게 참조할 수 있습니다.
  // =========================================================================

  // 최초실행시 실행됨. (의존성 배열에 cnt가 있으므로 cnt 변경 시에도 실행됨)
  useEffect(
    () => {
      console.log("최초 실행시 실행");
    }, [cnt]
  );


  // =========================================================================
  // [3. 이벤트 핸들러 함수들]
  // =========================================================================

  // 1. State를 변경하는 함수
  const handleStateClick = () => {
    setCnt(cnt + 1); 
    // 주의: setCnt는 비동기로 작동하므로, 여기서 바로 console.log(cnt)를 찍으면 변경 전 값이 나옵니다.
    console.log("State(cnt) 클릭됨 - 화면 갱신 예정");
  };

  // 2. 일반 변수를 변경하는 함수
  const handleVarClick = () => {
    count++; // 변수 값 1 증가
    console.log("일반변수(count):", count);
    
    setId('bbb' + count); // 강제 리렌더링을 위해 State 변경 호출
    console.log("id", id); // 비동기라 변경 전 값 출력됨

    // 문제점: 일반 변수 값이 바뀌어도 리액트는 화면을 다시 그리지(리렌더링) 않습니다.
  };

  // 3. [추가] useRef 값을 변경하는 함수
  const handleRefClick = () => {
    cntRef.current = cntRef.current + 1; // .current 프로퍼티를 수정해야 함
    console.log("useRef(cntRef):", cntRef.current);
    // 특징: 값은 변하지만 화면은 갱신되지 않음 (콘솔 확인 필요)
  };


  // =========================================================================
  // [4. 화면 렌더링 (return)]
  // =========================================================================
  return (
    <div className="root">
      <div className='txt' id='main'>
        {/* 화면에서 비교하기 위해 Ref 값도 표시합니다 */}
        State: {cnt} / 일반변수: {count} / Ref: {cntRef.current} <br/>
        ID: {id}
      </div>
      
      <button onClick={handleStateClick}>useState확인</button>
      
      <button onClick={handleVarClick}>일반변수확인</button>
      
      <button onClick={handleRefClick}>useRef확인</button>
    </div>
  );
}

export default App;