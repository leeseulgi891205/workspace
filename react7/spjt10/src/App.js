import logo from './logo.svg';
import './App.css';
import './css/Style.css';
import axios from 'axios';
import { useEffect, useState } from 'react';

function App() {

  // 자바스크립트 일반변수 - 변수값을 변경할수 있지만, html에 반영이 안됨. 리로딩되면 값이 리셋됨.
  // const uuuser = 'aaa';

  //useState변수 - 데이터가 변경이 되면 html페이지에 반영을 해주는 변수
  const [users,setUsers] = useState([]);
  
  // react가 리로딩이 되면 실행되는 함수, 최초 한번만 실행
  // axios를 이용하여 외부 json데이터를 가져와서 users변수에 저장
  // post방식으로 잔송

  useEffect(() => {
    axios.get('http://localhost:8000/member/userInsert/',{ id: 'aaa', name: '홍길자'}).then((res) => {
      console.log('json 데이터 : ', res);
      setUsers(res.data.arr);
    });
  }, []);


  // useEffect(() => {
  //   axios
  //     .get('https://jsonplaceholder.typicode.com/users')
  //     .then((res) => {
  //       console.log('성공');
  //       setUsers(
  //         res.data.map((u) => ({
  //           id: String(u.id),
  //           name: u.name,
  //           address: u.address?.city || '',
  //         })),
  //       );
  //     })
  //     .catch((error) => {
  //       console.log('실패', error);
  //     });
  // }, []);



  const user_list = users.map((user, index) => (
    <div className="card" key={user.id}>
      <h5 className="card-header">번호 : {user.id}</h5>
      <div className="card-body">
        <h5 className="card-title">이름 : {user.name}</h5>
        <p className="card-text">주소 : {user.phone}</p>
        <button className="btn btn-primary">수정</button>
        <button className="btn btn-primary">삭제</button>
      </div>
    </div>
  ));


  return (
    <div className="root">
      <h2>회원리스트</h2>
        {user_list}
    </div>
  );
}

export default App;
