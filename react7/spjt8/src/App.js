import logo from './logo.svg';
import './App.css';
import './css/Style.css';
import { useState,useEffect,useRef } from 'react';

function App() {

  //useState변수
  const noInputRef = useRef();
  const [no,setNo] = useState('');
  const [title,setTitle] = useState('');
  const [year,setYear] = useState('');

  const [movies,setMovies] = useState(
    // 서버api로 가져옴. - Django Json호출
    // ajax,fetch,axios
    [
    {no:1,title:'해리포터1',year:'2022'},
    {no:2,title:'아이언맨1',year:'2023'},
    {no:3,title:'해리포터2',year:'2024'},
    {no:4,title:'아이언맨2',year:'2025'},
  ]
  )
  // 추가
  const handleAdd = () => {
    const maxNo = Math.max(...movies.map(m => m.no), 0);
    setMovies([...movies,{no: maxNo + 1, title, year}])
  }

  // 삭제
  const handleDelete = (deleteNo) => {
    alert(deleteNo+'번 영화가 삭제됩니다.')
    setMovies(movies.filter((movie) => movie.no !== deleteNo))
  }

  const saveBtn = () => {
    if(title.trim() ===''){
      alert('영화제목은 필수입니다.')
      noInputRef.current.focus();
      return;
    }
    handleAdd();
    console.log("넘어온 데이터 :"+no+", 제목:"+title+", 년도:"+year);
    alert('영화를 저장합니다.')
    // input박스 리셋
    setNo('');
    setTitle('');
    setYear('');

    noInputRef.current.focus();
  }




  //리스트를 map()함수 실행방법
  //for문을 사용할수 없음.
  const movie_list = movies.map(// 함수실행
     (movie) =>{
      return(
        <div className="card" key={movie.no}>
          <h5 className="card-header">번호 : {movie.no}</h5>
          <div className="card-body">
            <h5 className="card-title">제목 : {movie.title}</h5>
            <p className="card-text">{movie.year}</p>
            <button className="btn btn-primary">수정</button>
            <button className="btn btn-primary" onClick={() => handleDelete(movie.no)}>삭제</button>
          </div>
        </div>
      )
     }
  )



  return (
    <div className="root">
      {/* 입력부분 */}
      <h3>영화입력</h3>
      <form>
        <div className="row mb-3">
          <label htmlFor="inputEmail3" className="col-sm-2 col-form-label">번호</label>
          <div className="col-sm-10">
            <input type="text" ref={noInputRef} value={no} onChange={(e)=>setNo(e.target.value)} className="form-control" id="inputEmail3" />
          </div>
        </div>
        <div className="row mb-3">
          <label htmlFor="inputEmail4" className="col-sm-2 col-form-label">제목</label>
          <div className="col-sm-10">
            <input type="text" value={title} onChange={(e)=>setTitle(e.target.value)} className="form-control" id="inputEmail4" />
          </div>
        </div>
        <div className="row mb-3">
          <label htmlFor="inputPassword3" className="col-sm-2 col-form-label">년도</label>
          <div className="col-sm-10">
            <input type="text" value={year} onChange={(e)=>setYear(e.target.value)} className="form-control" id="inputPassword3" />
          </div>
        </div>
        <button type="button" onClick={saveBtn} className="btn btn-primary ">저장</button>
        <button type="button" className="btn btn-primary">취소</button>
      </form>
      {/* 출력부분 */}
      <h3>영화리스트</h3>
      {movie_list}

    </div>
  );
}

export default App;