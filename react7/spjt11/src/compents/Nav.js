import React from 'react';
import { Link } from 'react-router-dom';



const Nav = () => {
    return (
        <>
    {/* 네비게이션 */}
      <nav className="navbar navbar-expand-lg bg-body-tertiary">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">HOME</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item">
                <Link className="nav-link active" aria-current="page" to="/BList">게시판리스트</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/BWrite">게시판글쓰기</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to="/BView">상세보기</Link>
              </li>
              <li className="nav-item">
                <Link className="nav-link" to='/UserList'>회원리스트</Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </>
    )
}

export default Nav;