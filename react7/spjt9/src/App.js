import './css/Style.css';
import Movies from './comp/Movies.js'
import {useState,useEffect} from 'react';

function App() {

  const [movies, setMovies] = useState(
    [
    ]
  );

  const [title, setTitle] = useState('');
  const [year, setYear] = useState('');
  const [searchKeyword, setSearchKeyword] = useState('');
  const [selectedDate, setSelectedDate] = useState('');
  const [apiKey, setApiKey] = useState('82ca741a2844c5c180a208137bb92bd7');

  const TMDB_API_KEY = 'c3010f63ec81e3e1b75c3c94ce850ef7';

    // 2. 데이터 삭제 : filter()
    // 삭제할 pk키 - no를 받아서 전달함.
  const delMovie = (no) => {
    //결과를 충족한 데이터만 return 전달됨.
    // == 삭제할 no와 다른 데이터만 걸러서 새로운 배열 생성
    // != 삭제할 no와 같은 데이터는 걸러짐.
    setMovies(movies.filter( (movie) =>{ return(movie.no != no )}));
  };

  // 리스트 출력 : 반복문 map()
  // map()함수는 배열에 있는 데이터를 1개씩 가져와 함수를 적용시켜줌.
  // (조건)?참:거짓
  const renderMovies = 
  movies.length?
  movies.map( (movie)=>{
    return(<Movies movie={movie} delMovie={delMovie} key={movie.no}/>
    )
  })
  :
      <> <div className="card">
            <div className="card-header"></div>
            <div className="card-body">
            <h5 className="card-title">데이터가 없습니다.</h5>
          </div>?
      </div></>



  // 3. 데이터 추가 : [...배열, 새데이터], {'no':4, 'title':'아바타1', 'year':2022},
  const addMovie = (e) => {
    e.preventDefault();
    if(!title.trim() || !year.trim()) {
      alert('제목과 연도를 입력해주세요');
      return;
    }
    const newNo = movies.length > 0 ? Math.max(...movies.map(m => m.no)) + 1 : 1;
    const newMovie = {'no': newNo, 'title': title, 'year': parseInt(year)};
    setMovies([newMovie, ...movies]);
    setTitle('');
    setYear('');
  };

  // 4. API를 이용한 영화 검색
  const searchMovie = async (e) => {
    e.preventDefault();
    if(!searchKeyword.trim()) {
      alert('검색어를 입력해주세요');
      return;
    }
    
    try {
      const response = await fetch(
        `https://api.themoviedb.org/3/search/movie?api_key=${TMDB_API_KEY}&query=${searchKeyword}&language=ko-KR`
      );
      const data = await response.json();
      
      if(data.results && data.results.length > 0) {
        // 검색된 영화들을 리스트에 추가
        const searchedMovies = data.results.map((movie, index) => ({
          'no': Date.now() + index,
          'title': movie.title,
          'year': new Date(movie.release_date).getFullYear()
        }));
        setMovies([...searchedMovies, ...movies]);
        setSearchKeyword('');
      } else {
        alert('검색 결과가 없습니다');
      }
    } catch(error) {
      console.error('검색 오류:', error);
      alert('검색 중 오류가 발생했습니다');
    }
  };

  // 5. KOBIS 날짜별 박스오피스 조회
  const searchByDate = async (e) => {
    e.preventDefault();
    if(!selectedDate) {
      alert('날짜를 선택해주세요');
      return;
    }

    if(!apiKey.trim()) {
      alert('KOBIS API 키를 입력해주세요');
      return;
    }
    
    try {
      // 날짜 포맷: YYYY-MM-DD를 YYYYMMDD로 변환
      const dateStr = selectedDate.replace(/-/g, '');
      const response = await fetch(
        `http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=${apiKey}&targetDt=${dateStr}`
      );
      const data = await response.json();
      
      if(data.boxOfficeResult && data.boxOfficeResult.dailyBoxOfficeList && data.boxOfficeResult.dailyBoxOfficeList.length > 0) {
        // KOBIS 박스오피스 데이터를 리스트에 추가
        const boxofficeMovies = data.boxOfficeResult.dailyBoxOfficeList.map((movie) => ({
          'no': parseInt(movie.movieCd),
          'title': movie.movieNm,
          'rank': movie.rank,
          'audiCnt': movie.audiCnt,
          'salesAmt': movie.salesAmt
        }));
        setMovies([...boxofficeMovies, ...movies]);
        setSelectedDate('');
      } else {
        alert('해당 날짜의 박스오피스 데이터가 없습니다');
      }
    } catch(error) {
      console.error('박스오피스 조회 오류:', error);
      alert('박스오피스 조회 중 오류가 발생했습니다. API 키를 확인해주세요.');
    }
  };



  return (
        <div className="root">
          <h2>영화검색</h2>
          
          {/* 수동 추가 폼 */}
          <h4>영화 수동 추가</h4>
          <form onSubmit={addMovie}>
            <div className="mb-3">
              <label htmlFor="movieTitle" className="form-label">영화 제목</label>
              <input type="text" className="form-control" id="movieTitle" 
             value={title} onChange={(e) => setTitle(e.target.value)} 
             placeholder="영화 제목을 입력하세요"/>
            </div>
            <div className="mb-3">
              <label htmlFor="movieYear" className="form-label">개봉 연도</label>
              <input type="number" className="form-control" id="movieYear" 
                    value={year} onChange={(e) => setYear(e.target.value)}
                    placeholder="개봉 연도를 입력하세요"/>
              </div>
              <button type="submit" className="btn btn-primary">추가</button>
          </form>

          {/* API 검색 폼 */}
          <h4>영화 검색</h4>
          <form onSubmit={searchMovie}>
            <div className="mb-3">
              <label htmlFor="searchKeyword" className="form-label">영화 검색</label>
              <input type="text" className="form-control" id="searchKeyword" 
             value={searchKeyword} onChange={(e) => setSearchKeyword(e.target.value)} 
             placeholder="검색할 영화 제목을 입력하세요"/>
            </div>
            <button type="submit" className="btn btn-success">검색</button>
          </form>

          {/* 날짜별 영화 순위 조회 폼 */}
          <h4>날짜별 박스오피스</h4>
          <form onSubmit={searchByDate}>
            <div className="mb-3">
              <label htmlFor="apiKey" className="form-label">KOBIS API 키</label>
              <input type="text" className="form-control" id="apiKey" 
             value={apiKey} onChange={(e) => setApiKey(e.target.value)}
             placeholder="KOBIS API 키를 입력하세요"/>
              <small className="form-text text-muted">
                <a href="https://www.kobis.or.kr/kobisopenapi/homepg/apikey/ckUser/findApikeyList.do" target="_blank" rel="noopener noreferrer">
                  KOBIS API 키 발급받기
                </a>
              </small>
            </div>
            <div className="mb-3">
              <label htmlFor="selectedDate" className="form-label">날짜 선택</label>
              <input type="date" className="form-control" id="selectedDate" 
             value={selectedDate} onChange={(e) => setSelectedDate(e.target.value)}/>
            </div>
            <button type="submit" className="btn btn-info">박스오피스 조회</button>
          </form>

      {/* 영화리스트 */}
      <h2>영화리스트</h2>
      {renderMovies}

    </div>
  );
}

export default App;