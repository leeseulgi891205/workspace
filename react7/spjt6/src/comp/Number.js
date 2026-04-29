import React, { useState } from "react";


// 숫자 증가 컴퍼넌트 선언 - props 값
const Number = ({btnName, number}) => {
    const [num, setNum] = useState(0);
    const cntBtn = () => {
      setNum(num + 1);
    }
    return (
        <>
        <h4>숫자증가 컴퍼넌트 {number}</h4>
        <div>{num}</div>
        <button onClick={cntBtn}>{btnName}</button>
        </>
    )
}

export default Number;