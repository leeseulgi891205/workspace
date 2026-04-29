<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8">
		<title>회원수정</title>
	</head>
	<body>
		<h2>회원수정</h2>
		<form action="mUpdate" method="post">
			<input type="text" name="id" value="${member.id}" readonly></input><br>
			<input type="password" name="pw" value="${member.pw}" placeholder="비밀번호를 입력하세요"></input><br>
			<input type="text" name="name" value="${member.name}" placeholder="이름을 입력하세요"></input><br>
			<input type="text" name="email" value="${member.email}" placeholder="이메일을 입력하세요"></input><br>
			<input type="text" name="phone" value="${member.phone}" placeholder="전화번호를 입력하세요"></input><br>
			<label>성별</label><br>
			<input type="radio" id="male" name="gender" value="남자" ${member.gender == '남자' ? 'checked' : ''}>
			<c:if test="${fn:contains(member.gender,'남자') }">checked</c:if>
            <label for="male">남자</label>
            <input type="radio" id="female" name="gender" value="여자" ${member.gender == '여자' ? 'checked' : ''}>
            <c:if test="${fn:contains(member.gender,'여자') }">checked</c:if>
            <label for="female">여자</label>
            <br>
            <label>취미</label><br>
            <input type="checkbox" id="game" name="hobby" value="게임" ${fn:contains(fn:join(member.hobby,','),'게임') ? 'checked' : ''}>
            <c:if test="${fn:contains(fn:join(member.hobby,','),'게임') }">checked</c:if>
            <label for="game">게임</label>
            <input type="checkbox" id="movie" name="hobby" value="영화" ${fn:contains(fn:join(member.hobby,','),'영화') ? 'checked' : ''}>
            <c:if test="${fn:contains(fn:join(member.hobby,','),'영화') }">checked</c:if>
            <label for="movie">영화</label>
            <input type="checkbox" id="music" name="hobby" value="음악" ${fn:contains(fn:join(member.hobby,','),'음악') ? 'checked' : ''}>
            <c:if test="${fn:contains(fn:join(member.hobby,','),'음악') }">checked</c:if>
            <label for="music">음악</label>
            <input type="checkbox" id="sports" name="hobby" value="운동" ${fn:contains(fn:join(member.hobby,','),'운동') ? 'checked' : ''}>
            <c:if test="${fn:contains(fn:join(member.hobby,','),'운동') }">checked</c:if>
            <label for="sports">운동</label>
            <input type="checkbox" id="travel" name="hobby" value="여행" ${fn:contains(fn:join(member.hobby,','),'여행') ? 'checked' : ''}>
            <c:if test="${fn:contains(fn:join(member.hobby,','),'여행') }">checked</c:if>
            <label for="travel">여행</label>
			<input type="submit" value="수정"></input>
		</form>
        <ul>
            <li><a href="/">홈으로</a></li>
            <li><a href="/login">로그인</a></li>
        </ul>
	</body>
</html>