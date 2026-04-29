import React, { useState, useEffect } from "react";

const UList = () => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/users");
        if (!response.ok) {
          throw new Error("데이터를 가져올 수 없습니다");
        }
        const data = await response.json();
        setUsers(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchUsers();
  }, []);

  if (loading) return <div className="page-container"><p>로딩 중...</p></div>;
  if (error) return <div className="page-container"><p>에러: {error}</p></div>;

  return (
    <div className="page-container">
      <h2>사용자 목록</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>이름</th>
            <th>사용자명</th>
            <th>이메일</th>
            <th>전화</th>
            <th>회사</th>
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
              <td>@{user.username}</td>
              <td>{user.email}</td>
              <td>{user.phone}</td>
              <td>{user.company.name}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default UList;