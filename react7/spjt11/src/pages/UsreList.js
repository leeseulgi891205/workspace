import React, { useEffect, useState } from "react";


const UsreList = () => {

    const [users, setUsers] = useState([]);
    const [editUser, setEditUser] = useState(null);
    const [editData, setEditData] = useState({});
    const [currentPage, setCurrentPage] = useState(1);
    const itemsPerPage = 5;


    //fetch로 회원리스트 가져오기
    useEffect(() => {
        fetch('https://jsonplaceholder.typicode.com/users')
            .then((response) => response.json())
            .then((data) => {
                console.log(data);
                setUsers(data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }, []);

    // 삭제 함수
    const handleDelete = (id) => {
        if (window.confirm('정말 삭제하시겠습니까?')) {
            setUsers(users.filter((user) => user.id !== id));
        }
    };

    // 수정 모드 시작
    const handleEditStart = (user) => {
        setEditUser(user.id);
        setEditData({
            name: user.name,
            email: user.email,
            city: user.address.city
        });
    };

    // 수정 취소
    const handleEditCancel = () => {
        setEditUser(null);
        setEditData({});
    };

    // 수정 저장
    const handleEditSave = (id) => {
        setUsers(users.map((user) =>
            user.id === id
                ? {
                    ...user,
                    name: editData.name,
                    email: editData.email,
                    address: { ...user.address, city: editData.city }
                }
                : user
        ));
        setEditUser(null);
        setEditData({});
    };

    // 입력값 변경
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setEditData({ ...editData, [name]: value });
    };

    // 페이지네이션 계산
    const totalPages = Math.ceil(users.length / itemsPerPage);
    const startIndex = (currentPage - 1) * itemsPerPage;
    const endIndex = startIndex + itemsPerPage;
    const currentUsers = users.slice(startIndex, endIndex);

    // 페이지 변경
    const handlePageChange = (pageNumber) => {
        if (pageNumber >= 1 && pageNumber <= totalPages) {
            setCurrentPage(pageNumber);
        }
    };

    return (
        <>
            <div className="root">
                <h2>회원리스트</h2>
                <div className="users-container">
                    {currentUsers.map((user) => (
                        <div key={user.id} className="card">
                            <div className="card-body">
                                {editUser === user.id ? (
                                    <>
                                        <div className="form-group">
                                            <label>이름: </label>
                                            <input
                                                type="text"
                                                name="name"
                                                value={editData.name}
                                                onChange={handleInputChange}
                                                className="form-control"
                                            />
                                        </div>
                                        <div className="form-group">
                                            <label>이메일: </label>
                                            <input
                                                type="email"
                                                name="email"
                                                value={editData.email}
                                                onChange={handleInputChange}
                                                className="form-control"
                                            />
                                        </div>
                                        <div className="form-group">
                                            <label>도시: </label>
                                            <input
                                                type="text"
                                                name="city"
                                                value={editData.city}
                                                onChange={handleInputChange}
                                                className="form-control"
                                            />
                                        </div>
                                        <button
                                            onClick={() => handleEditSave(user.id)}
                                            className="btn btn-success btn-sm btn-margin"
                                        >
                                            저장
                                        </button>
                                        <button
                                            onClick={handleEditCancel}
                                            className="btn btn-secondary btn-sm"
                                        >
                                            취소
                                        </button>
                                    </>
                                ) : (
                                    <>
                                        <h5 className="card-title">이름: {user.name}</h5>
                                        <p className="card-text">주소: {user.address.city}</p>
                                        <p className="card-text">이메일: {user.email}</p>
                                        <button
                                            onClick={() => handleEditStart(user)}
                                            className="btn btn-primary btn-sm btn-margin"
                                        >
                                            수정
                                        </button>
                                        <button
                                            onClick={() => handleDelete(user.id)}
                                            className="btn btn-danger btn-sm"
                                        >
                                            삭제
                                        </button>
                                    </>
                                )}
                            </div>
                        </div>
                    ))}
                </div>
                <div className="pagination">
                    <button
                        onClick={() => handlePageChange(currentPage - 1)}
                        disabled={currentPage === 1}
                        className="btn btn-outline-primary btn-sm"
                    >
                        이전
                    </button>
                    {Array.from({ length: totalPages }, (_, index) => (
                        <button
                            key={index + 1}
                            onClick={() => handlePageChange(index + 1)}
                            className={`btn btn-sm ${currentPage === index + 1 ? 'btn-primary' : 'btn-outline-primary'}`}
                            style={{ margin: '0 2px' }}
                        >
                            {index + 1}
                        </button>
                    ))}
                    <button
                        onClick={() => handlePageChange(currentPage + 1)}
                        disabled={currentPage === totalPages}
                        className="btn btn-outline-primary btn-sm"
                    >
                        다음
                    </button>
                </div>
            </div>
        </>
    );
};

export default UsreList;