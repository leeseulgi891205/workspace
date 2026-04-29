import './css/Style.css';
import down from './다운로드 (3).jpg';


function App() {

  // css문법을 내부링크 방식 (잘 안함)
  // css문법 외부링크 방식을 선호함.
  // - 문법 구조가 틀림, style={title1} 변수를 입력적용
  // var : 예전버전의 변수선언
  // let : 최근버전의 변수선언
  // const : 최근버전의 상수선언(변하지 않는 값)
  const title1 = {
    // textAlign: 'center',
    // backgroundColor: 'yellow',
    // fontSize: '40px',

  }


  return (
    <>  
    <div className="App">
    <div></div>
    <h2 className='main' style={title1}>메인페이지</h2>
    <img src={down} />
    <img src='/images/images (1).jpg' />
    </div>
    </>
  );
}

export default App;
