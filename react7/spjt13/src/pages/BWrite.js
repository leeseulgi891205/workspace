import React, { useState, useEffect } from "react";

const BWrite = () => {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [userId, setUserId] = useState("1");
  const [editingId, setEditingId] = useState(null);
  const [loading, setLoading] = useState(true);

  // 초기 데이터 로드
  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/posts?_limit=10");
        const data = await response.json();
        setPosts(data);
        setLoading(false);
      } catch (err) {
        console.error("데이터 로드 실패:", err);
        setLoading(false);
      }
    };
    fetchPosts();
  }, []);

  // 게시물 작성
  const handleCreate = async () => {
    if (!title || !body) {
      alert("제목과 내용을 입력해주세요");
      return;
    }

    try {
      const response = await fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, body, userId: parseInt(userId) }),
      });
      const newPost = await response.json();
      setPosts([newPost, ...posts]);
      setTitle("");
      setBody("");
      alert("게시물이 작성되었습니다");
    } catch (err) {
      console.error("작성 실패:", err);
    }
  };

  // 게시물 수정
  const handleUpdate = async () => {
    if (!title || !body) {
      alert("제목과 내용을 입력해주세요");
      return;
    }

    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/posts/${editingId}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, body, userId: parseInt(userId) }),
      });
      const updatedPost = await response.json();
      setPosts(posts.map((post) => (post.id === editingId ? updatedPost : post)));
      setTitle("");
      setBody("");
      setEditingId(null);
      alert("게시물이 수정되었습니다");
    } catch (err) {
      console.error("수정 실패:", err);
    }
  };

  // 게시물 삭제
  const handleDelete = async (id) => {
    if (!window.confirm("정말 삭제하시겠습니까?")) return;

    try {
      await fetch(`https://jsonplaceholder.typicode.com/posts/${id}`, {
        method: "DELETE",
      });
      setPosts(posts.filter((post) => post.id !== id));
      alert("게시물이 삭제되었습니다");
    } catch (err) {
      console.error("삭제 실패:", err);
    }
  };

  // 수정 모드로 진입
  const handleEdit = (post) => {
    setEditingId(post.id);
    setTitle(post.title);
    setBody(post.body);
    setUserId(post.userId);
  };

  // 작성 취소
  const handleCancel = () => {
    setTitle("");
    setBody("");
    setEditingId(null);
  };

  if (loading) return <div className="page-container"><p>로딩 중...</p></div>;

  return (
    <div className="page-container">
      <h2>{editingId ? "게시물 수정" : "게시물 작성"}</h2>

      {/* 작성/수정 폼 */}
      <div className="mb-4 p-3 border rounded">
        <div className="mb-3">
          <label htmlFor="emailInput" className="form-label">이메일 주소</label>
          <input
            type="email"
            className="form-control"
            id="emailInput"
            placeholder="name@example.com"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
          />
        </div>

        <div className="mb-3">
          <label htmlFor="textareaInput" className="form-label">게시물 내용</label>
          <textarea
            className="form-control"
            id="textareaInput"
            rows="3"
            value={body}
            onChange={(e) => setBody(e.target.value)}
          ></textarea>
        </div>
        

        <div>
          {editingId ? (
            <>
              <button className="btn btn-primary me-2" onClick={handleUpdate}>
                수정 완료
              </button>
              <button className="btn btn-secondary" onClick={handleCancel}>
                취소
              </button>
            </>
          ) : (
            <button className="btn btn-primary" onClick={handleCreate}>
              작성하기
            </button>
          )}
        </div>
      </div>

      {/* 게시물 목록 */}
      <h3>내 게시물</h3>
      <div className="list-group">
        {posts.length === 0 ? (
          <p>게시물이 없습니다</p>
        ) : (
          posts.map((post) => (
            <div key={post.id} className="list-group-item">
              <div className="d-flex justify-content-between align-items-start">
                <div>
                  <h5 className="mb-1">[{post.id}] {post.title}</h5>
                  <p className="mb-1">{post.body.substring(0, 100)}...</p>
                  <small className="text-muted">사용자 ID: {post.userId}</small>
                </div>
                <div>
                  <button
                    className="btn btn-sm btn-primary me-2"
                    onClick={() => handleEdit(post)}
                  >
                    수정
                  </button>
                  <button
                    className="btn btn-sm btn-primary"
                    onClick={() => handleDelete(post.id)}
                  >
                    삭제
                  </button>
                </div>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default BWrite;