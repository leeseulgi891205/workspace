import { useState } from 'react';
import './App.css';
import './css/Style.css';

function App() {
  const [movieList, setMovieList] = useState([]);
  const [targetDate, setTargetDate] = useState(''); 
  const [isLoading, setIsLoading] = useState(false);
  const [selectedMovie, setSelectedMovie] = useState(null);
  const [peopleLists, setPeopleLists] = useState([]);
  const [expandedMovieCd, setExpandedMovieCd] = useState(null);
  const [selectedPerson, setSelectedPerson] = useState(null);
  
  // 1. 페이지네이션을 위한 상태 추가
  const [currentPage, setCurrentPage] = useState(1); // 현재 페이지 번호
  const itemsPerPage = 4; // 한 페이지당 보여줄 아이템 개수

  // 사용자의 실제 API 키
  const API_KEY = 'c3010f63ec81e3e1b75c3c94ce850ef7'; 

  const handleDateChange = (e) => {
    setTargetDate(e.target.value);
  };

  const handleSearch = async (e) => {
    e.preventDefault();

    if (!targetDate) {
      alert("날짜를 선택해주세요.");
      return;
    }

    const formattedDate = targetDate.replaceAll('-', '');
    setIsLoading(true); 

    try {
      const url = `https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=${API_KEY}&targetDt=${formattedDate}`;
      const response = await fetch(url);
      
      if (!response.ok) throw new Error(`통신 오류! 상태 코드: ${response.status}`);

      const data = await response.json();
      const dailyBoxOfficeList = data.boxOfficeResult?.dailyBoxOfficeList;

      if (dailyBoxOfficeList) {
        const formattedList = dailyBoxOfficeList.map((item) => ({
          no: item.rank,
          movieCd: item.movieCd,
          title: item.movieNm,
          year: item.openDt,
          audiAcc: item.audiAcc
        }));
        setMovieList(formattedList);
        setCurrentPage(1); // 2. 새로운 검색 시 1페이지로 초기화
      } else {
        alert("데이터가 없습니다.");
        setMovieList([]);
      }

    } catch (error) {
      console.error("에러 발생:", error);
      alert(`오류가 발생했습니다: ${error.message}`);
    } finally {
      setIsLoading(false); 
    }
  };

  const handleResetList = () => {
    setMovieList([]);
    setTargetDate('');
    setCurrentPage(1); // 초기화 시 페이지도 1로
  };

  // 영화 클릭 시 영화인 정보 조회
  const handleMovieClick = async (movieCd, movieNm) => {
    // 이미 펼쳐져 있으면 닫기
    if (expandedMovieCd === movieCd) {
      setExpandedMovieCd(null);
      return;
    }

    setSelectedMovie({ cd: movieCd, nm: movieNm });
    setExpandedMovieCd(movieCd);
    setIsLoading(true);

    try {
      // 영화 상세정보 조회로 영화인 정보 가져오기
      const url = `https://kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key=${API_KEY}&movieCd=${movieCd}`;
      const response = await fetch(url);
      
      if (!response.ok) throw new Error(`통신 오류! 상태 코드: ${response.status}`);

      const data = await response.json();
      const movieInfo = data.movieInfoResult?.movieInfo;

      if (movieInfo) {
        // 감독과 배우 정보 모두 추출
        let allPeople = [];
        
        if (movieInfo.directors && movieInfo.directors.length > 0) {
          const directors = movieInfo.directors.map(director => ({
            peopleNm: director.peopleNm,
            peopleNmEn: director.peopleNmEn || '',
            cast: director.cast || '감독',
            filmoNames: director.filmoNames || []
          }));
          allPeople = [...allPeople, ...directors];
        }
        
        if (movieInfo.actors && movieInfo.actors.length > 0) {
          const actors = movieInfo.actors.map(actor => ({
            peopleNm: actor.peopleNm,
            peopleNmEn: actor.peopleNmEn || '',
            cast: actor.cast || '배우',
            filmoNames: actor.filmoNames || []
          }));
          allPeople = [...allPeople, ...actors];
        }
        
        setPeopleLists(allPeople);
      } else {
        setPeopleLists([]);
      }
    } catch (error) {
      console.error("영화인 정보 조회 오류:", error);
      alert(`영화인 정보 조회 오류: ${error.message}`);
      setPeopleLists([]);
    } finally {
      setIsLoading(false);
    }
  };

  // 3. 현재 페이지에 해당하는 데이터 계산 로직
  const indexOfLastItem = currentPage * itemsPerPage; // 마지막 아이템 인덱스 (1*4 = 4)
  const indexOfFirstItem = indexOfLastItem - itemsPerPage; // 첫 아이템 인덱스 (4-4 = 0)
  const currentMovies = movieList.slice(indexOfFirstItem, indexOfLastItem); // 0~4번까지 자름

  // 4. 페이지 번호 클릭 핸들러
  const handlePageChange = (pageNumber) => {
    setCurrentPage(pageNumber);
  };

  // 총 페이지 수 계산 (예: 10개 데이터 / 4개씩 = 3페이지)
  const totalPages = Math.ceil(movieList.length / itemsPerPage);

  return (
    <div className="root container mt-4">
      <h3 className="mb-4 text-center">일별 박스오피스 검색</h3>
      
      <form onSubmit={handleSearch} className="mb-5 border p-4 rounded shadow-sm bg-light">
        <div className="d-flex justify-content-center align-items-center gap-3">
          <label htmlFor="dateInput" className="col-form-label fw-bold text-nowrap">
            날짜 선택 :
          </label>
          <input 
            type="date" className="form-control" id="dateInput" style={{ width: 'auto' }}
            value={targetDate} onChange={handleDateChange} 
          />
          <button type="submit" className="btn btn-primary text-nowrap" disabled={isLoading}>
            {isLoading ? '로딩중...' : '검색'}
          </button>
        </div>
        <div className="form-text text-center mt-2">
          * <strong>어제 날짜</strong>를 선택해야 데이터가 정확하게 나옵니다.
        </div>
      </form>

      <hr />

      <div className="d-flex justify-content-between align-items-center mb-3">
        <h4>검색 결과 {movieList.length > 0 && `(${movieList.length}건)`}</h4>
        <button type="button" className="btn btn-outline-danger btn-sm" onClick={handleResetList}>
          목록 초기화
        </button>
      </div>
      
      {/* 5. movieList 대신 currentMovies(잘린 데이터)를 보여줌 */}
      {currentMovies.length === 0 ? (
        <div className="text-center p-5 bg-light rounded text-muted">
          날짜를 선택하고 검색 버튼을 눌러주세요.
        </div>
      ) : (
        <>
          <div className="row">
            {currentMovies.map((movie) => (
              <div className="col-md-6 mb-4" key={movie.no}>
                <div 
                  className="card h-100 shadow-sm border-0 bg-white"
                  style={{ cursor: 'pointer' }}
                >
                  <div className="card-header bg-transparent border-bottom d-flex justify-content-between">
                    <span className="badge bg-danger rounded-pill">Rank {movie.no}</span>
                    <small className="text-muted">{movie.year} 개봉</small>
                  </div>
                  <div className="card-body">
                    <h5 className="card-title fw-bold">{movie.title}</h5>
                    <p className="card-text text-secondary mt-2">
                      누적 관객: {Number(movie.audiAcc).toLocaleString()}명
                    </p>
                    <button 
                      type="button"
                      className={`btn btn-sm ${expandedMovieCd === movie.movieCd ? 'btn-danger' : 'btn-outline-primary'}`}
                      onClick={() => handleMovieClick(movie.movieCd, movie.title)}
                      disabled={isLoading}
                    >
                      {expandedMovieCd === movie.movieCd ? '영화인 정보 닫기' : '영화인 정보 보기'}
                    </button>
                    
                    {/* 선택된 영화일 때 영화인 정보 표시 */}
                    {expandedMovieCd === movie.movieCd && peopleLists.length > 0 && (
                      <div className="mt-3 pt-3 border-top">
                        <h6 className="fw-bold mb-3">영화인 정보</h6>
                        {peopleLists.map((person, idx) => (
                          <div className="mb-3 p-2 bg-light rounded" key={idx}>
                            <div className="d-flex justify-content-between align-items-start mb-1">
                              <div 
                                style={{ cursor: 'pointer' }}
                                onClick={() => setSelectedPerson(person)}
                              >
                                <p className="mb-1 fw-bold text-primary" style={{ textDecoration: 'underline' }}>
                                  {person.peopleNm}
                                </p>
                                {person.peopleNmEn && (
                                  <small className="text-muted d-block">{person.peopleNmEn}</small>
                                )}
                              </div>
                              <span className="badge bg-info text-dark">{person.cast}</span>
                            </div>
                            {Array.isArray(person.filmoNames) && person.filmoNames.length > 0 && (
                              <div className="mt-2">
                                <small className="text-muted d-block mb-1"><strong>출연 작품:</strong></small>
                                <ul className="list-unstyled mb-0">
                                  {person.filmoNames.slice(0, 3).map((filmo, filmoIdx) => (
                                    <li key={filmoIdx} className="text-muted small">
                                      • {filmo.characterName || filmo.name || '정보 없음'}
                                    </li>
                                  ))}
                                </ul>
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              </div>
            ))}
          </div>

          {/* 6. 페이지네이션 버튼 UI */}
          <nav aria-label="Page navigation" className="mt-4">
            <ul className="pagination justify-content-center">
              
              {/* 이전 버튼 */}
              <li className={`page-item ${currentPage === 1 ? 'disabled' : ''}`}>
                <button 
                  className="page-link" 
                  onClick={() => handlePageChange(currentPage - 1)}
                  disabled={currentPage === 1}
                >
                  &lt;
                </button>
              </li>

              {/* 페이지 번호들 (배열 생성 후 map) */}
              {Array.from({ length: totalPages }, (_, i) => i + 1).map((number) => (
                <li key={number} className={`page-item ${currentPage === number ? 'active' : ''}`}>
                  <button 
                    className="page-link" 
                    onClick={() => handlePageChange(number)}
                  >
                    {number}
                  </button>
                </li>
              ))}

              {/* 다음 버튼 */}
              <li className={`page-item ${currentPage === totalPages ? 'disabled' : ''}`}>
                <button 
                  className="page-link" 
                  onClick={() => handlePageChange(currentPage + 1)}
                  disabled={currentPage === totalPages}
                >
                  &gt;
                </button>
              </li>
            </ul>
          </nav>
        </>
      )}

      {/* 영화인 전체 필모그래피 모달 */}
      {selectedPerson && (
        <div className="mt-5 p-4 border rounded bg-white shadow-sm">
          <div className="d-flex justify-content-between align-items-center mb-3">
            <div>
              <h5 className="mb-1 fw-bold text-primary">{selectedPerson.peopleNm}</h5>
              {selectedPerson.peopleNmEn && (
                <small className="text-muted">{selectedPerson.peopleNmEn}</small>
              )}
              <span className="badge bg-info ms-2">{selectedPerson.cast}</span>
            </div>
            <button 
              type="button"
              className="btn btn-sm btn-outline-secondary"
              onClick={() => setSelectedPerson(null)}
            >
              닫기
            </button>
          </div>
          
          <hr />
          
          <div>
            <h6 className="fw-bold mb-3">전체 필모그래피 ({selectedPerson.filmoNames?.length || 0})</h6>
            {Array.isArray(selectedPerson.filmoNames) && selectedPerson.filmoNames.length > 0 ? (
              <div className="row">
                {selectedPerson.filmoNames.map((filmo, idx) => (
                  <div className="col-md-6 mb-2" key={idx}>
                    <div className="p-2 border rounded bg-light">
                      <small className="d-block"><strong>{filmo.characterName || filmo.name || '정보 없음'}</strong></small>
                      {filmo.moviePartNm && <small className="text-muted d-block">{filmo.moviePartNm}</small>}
                    </div>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-muted">필모그래피 정보가 없습니다</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
}

export default App;