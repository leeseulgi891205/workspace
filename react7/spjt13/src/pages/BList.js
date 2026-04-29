import React, { useState, useEffect } from "react";

const BList = () => {
  const [posts, setPosts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts");
        if (!response.ok) {
          throw new Error("데이터를 가져올 수 없습니다");
        }
        const data = await response.json();
        setPosts(data);
        setLoading(false);
      } catch (err) {
        setError(err.message);
        setLoading(false);
      }
    };

    fetchPosts();
  }, []);

  if (loading) return <div className="page-container"><p>로딩 중...</p></div>;
  if (error) return <div className="page-container"><p>에러: {error}</p></div>;

  return (
    <div className="page-container">
      <h2>게시물 목록</h2>
      <table className="table table-striped">
        <thead>
          <tr>
            <th>ID</th>
            <th>제목</th>
            <th>내용</th>
          </tr>
        </thead>
        <tbody>
          {posts.map((post) => (
            <tr key={post.id}>
              <td>{post.id}</td>
              <td>{post.title}</td>
              <td>{post.body.substring(0, 50)}...</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default BList;