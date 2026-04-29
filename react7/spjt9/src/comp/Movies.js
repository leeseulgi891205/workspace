import React from "react";

const Movies = ({movie,delMovie}) => {

    const delBtn = (no) => {
        if(window.confirm(no+"번 데이터를 삭제하시겠습니까?")){
            delMovie(no);
        }
    }

    return (
        <>
            <div className="card">
                <div className="card-header">번호 : {movie.no}</div>
                <div className="card-body">
                <h5 className="card-title">제목 :{movie.title}</h5>
                <p className="card-text">년도 :{movie.year}</p>
                <button href="#" className="btn btn-primary">수정</button>
                <button onClick={()=>delBtn(movie.no)} className="btn btn-primary">삭제</button>
                </div>
            </div>
        </>
    )
}
export default Movies;