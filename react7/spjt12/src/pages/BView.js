import React, { useState, useEffect } from "react";
import { useParams, useNavigate } from "react-router-dom";
import axios from "axios";

const BView = () => {
    const { id } = useParams();
    const navigate = useNavigate();
    const [board, setBoard] = useState({});
    console.log("넘어온 id : ", id);

    useEffect(() => {
        axios.get(`https://jsonplaceholder.typicode.com/posts/${id}`)
            .then(res => {
                console.log("BView", res.data);
                setBoard(res.data);
            });
    }, [id]);

    const handleEdit = () => {
        alert('수정 기능은 준비 중입니다.');
        // navigate(`/board/bEdit/${id}`); // 실제 수정 페이지가 있으면 이 주석 해제
    };

    const handleDelete = () => {
        if (window.confirm(`${id}번 게시글을 삭제하시겠습니까?`)) {
            console.log(`게시글 ${id} 삭제됨`);
            navigate('/board/bList');
        }
    };

    const handleList = () => {
        navigate('/board/bList');
    };



    return (
        <>
            <div className="root">
                <h2>BView 상세보기</h2>
                <div className="card">
                    <img src="/images/우는짤.jpg" className="card-img-top" alt="..." />
                    <div className="card-body">
                        <h5 className="card-title">제목 : {board.title}</h5>
                        <p className="card-text">내용 : {board.body}</p>
                    </div>
                </div>
                <div>
                    <button type="button" className="btn btn-primary" onClick={handleEdit}>수정</button>
                    <button type="button" className="btn btn-secondary" onClick={handleDelete} >삭제</button>
                    <button type="button" className="btn btn-success" onClick={()=>navigate('/board/bList')} >목록</button>
                </div>
            </div>
        </>
    )
}

export default BView;