<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>회원 가입</title>
</head>
<body>
	<!-- Header -->
	<div style="display: flex; justify-content: space-between; align-items: center; padding: 0 40px; height: 60px; border-bottom: 1px solid #f0f0f0;">
		<h2 style="margin: 0; color: #035fe0;">VLAST Shop</h2>
		<div style="display: flex; gap: 15px; font-size: 13px;">
			<a href="login.do" style="text-decoration: none; color: #636363;">로그인</a> |
			<a href="main.do" style="text-decoration: none; color: #636363;">HOME</a>
		</div>
	</div>

	<!-- Container -->
	<div style="width: 100%; max-width: 720px; margin: 0 auto; box-sizing: border-box;">
		<div style="text-align: center; padding: 70px 0; font-size: 30px; font-weight: bold; color: #035fe0;">
			회원가입
		</div>
		
		<div style="text-align: center; padding-bottom: 20px; margin-bottom: 10px; border-bottom: 1px solid #1a1a1a;">
			<div style="display: flex; justify-content: center; gap: 40px;">
				<div style="display: inline-block; font-size: 14px;">1. 약관동의</div>
				<div style="display: inline-block; font-size: 14px; color: #035fe0; font-weight: 700;">2. 정보입력</div>
				<div style="display: inline-block; font-size: 14px;">3. 가입완료</div>
			</div>
		</div>

		<form action="domembership.do" method="post" onsubmit="return validateForm();">
			<div style="margin: 0 auto; max-width: 720px; box-sizing: border-box; padding: 10px 30px;">
				<table style="width: 100%; border-collapse: collapse;">
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">아이디 <span style="color:red">*</span></td>
						<td style="padding: 4px 0 12px;">
							<div style="display: flex; align-items: center; gap: 12px;">
								<input type="text" id="id" name="id" placeholder="영문소문자/숫자, 4~16자" style="flex: 1; padding: 15px; font-size: 15px; height: 45px; border: 1px solid #ccc; box-sizing: border-box;" required>
								<button type="button" onclick="checkId();" style="width: 110px; height: 45px; border: 1px solid #035fe0; background-color: #035fe0; color: #fff; cursor: pointer; font-size: 15px; font-weight: 500;">중복확인</button>
							</div>
						</td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">비밀번호 <span style="color:red">*</span></td>
						<td style="padding: 4px 0 12px;"><input type="password" id="pw" name="pw" placeholder="영문 대소문자/숫자/특수문자 중 2가지 이상 조합, 8자~16자" style="width: 100%; padding: 15px; font-size: 15px; height: 45px; border: 1px solid #ccc; box-sizing: border-box;" required></td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">비밀번호 확인 <span style="color:red">*</span></td>
						<td style="padding: 4px 0 12px;"><input type="password" id="pw_confirm" name="pw_confirm" style="width: 100%; padding: 15px; font-size: 15px; height: 45px; border: 1px solid #ccc; box-sizing: border-box;" required></td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">이름</td>
						<td style="padding: 4px 0 12px;"><input type="text" id="name" name="name" style="width: 100%; padding: 15px; font-size: 15px; height: 45px; border: 1px solid #ccc; box-sizing: border-box;"></td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">휴대전화 <span style="color:red">*</span></td>
						<td style="padding: 4px 0 12px;">
							<div style="display: flex; align-items: center; gap: 5px;">
								<select name="phone1" style="flex: 1; height: 45px; font-size: 15px; border: 1px solid #ccc; background: white; padding: 0 10px; box-sizing: border-box;" required>
									<option value="">선택</option>
									<option value="010">010</option>
									<option value="011">011</option>
									<option value="016">016</option>
									<option value="017">017</option>
									<option value="018">018</option>
									<option value="019">019</option>
								</select>
								<span style="width: 15px; text-align: center;">-</span>
								<input type="text" name="phone2" id="phone2" maxlength="4" placeholder="0000" style="flex: 1; height: 45px; font-size: 15px; border: 1px solid #ccc; background: white; padding: 0 10px; box-sizing: border-box;" required>
								<span style="width: 15px; text-align: center;">-</span>
								<input type="text" name="phone3" id="phone3" maxlength="4" placeholder="0000" style="flex: 1; height: 45px; font-size: 15px; border: 1px solid #ccc; background: white; padding: 0 10px; box-sizing: border-box;" required>
							</div>
						</td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">성별</td>
						<td style="padding: 4px 0 12px;">
							<div style="display: flex; gap: 20px;">
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="radio" name="gender" value="M" checked> 남자
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="radio" name="gender" value="F"> 여자
								</label>
							</div>
						</td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">취미</td>
						<td style="padding: 4px 0 12px;">
							<div style="display: flex; gap: 15px; flex-wrap: wrap;">
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="게임"> 게임
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="골프"> 골프
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="수영"> 수영
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="독서"> 독서
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="운동"> 운동
								</label>
								<label style="display: flex; align-items: center; gap: 8px; margin: 0; font-weight: normal;">
									<input type="checkbox" name="hobby" value="드라이브"> 드라이브
								</label>
							</div>
						</td>
					</tr>
					<tr>
						<td style="padding: 4px 0 12px; width: 140px; font-weight: 700; color: #1a1a1a;">이메일 <span style="color:red">*</span></td>
						<td style="padding: 4px 0 12px;">
							<div style="display: flex; align-items: center; gap: 12px;">
								<input type="email" id="email" name="email" placeholder="example@domain.com" style="flex: 1; padding: 15px; font-size: 15px; height: 45px; border: 1px solid #ccc; box-sizing: border-box;" required>
								<button type="button" onclick="sendEmailCode();" style="width: 110px; height: 45px; border: 1px solid #035fe0; background-color: #035fe0; color: #fff; cursor: pointer; font-size: 15px; font-weight: 500;">인증</button>
							</div>
						</td>
					</tr>

				</table>
			</div>

			<div style="display: flex; justify-content: center; gap: 15px; padding: 50px 0; margin: 0;">
				<button type="button" onclick="location.href='main.do';" style="width: 160px; height: 50px; font-size: 15px; font-weight: 400; border: 1px solid #ccc; background-color: white; color: #1a1a1a; cursor: pointer; box-sizing: border-box; margin: 0;">취소</button>
				<button type="submit" style="width: 160px; height: 50px; font-size: 15px; font-weight: 400; border: 1px solid #035fe0; background-color: #035fe0; color: #fff; cursor: pointer; box-sizing: border-box; margin: 0;">확인</button>
			</div>
		</form>
	</div>

	<!-- Footer -->
	<footer style="border-top: 1px solid #ccc; padding: 30px; text-align: center; font-size: 13px; color: #A0A0A0; margin-top: 50px;">
		Copyright © VLAST Shop. All rights reserved.
	</footer>

	<script>
		function validateForm() {
			const id = document.getElementById('id').value;
			const pw = document.getElementById('pw').value;
			const pw_confirm = document.getElementById('pw_confirm').value;
			const email = document.getElementById('email').value;
			
			if (id.length < 4 || id.length > 16) {
				alert('아이디는 4자 이상 16자 이하여야 합니다.');
				return false;
			}
			
			if (pw.length < 8 || pw.length > 16) {
				alert('비밀번호는 8자 이상 16자 이하여야 합니다.');
				return false;
			}
			
			if (pw !== pw_confirm) {
				alert('비밀번호가 일치하지 않습니다.');
				return false;
			}
			
			if (!email.match(/^[^\s@]+@[^\s@]+\.[^\s@]+$/)) {
				alert('올바른 이메일 형식을 입력해주세요.');
				return false;
			}
			
			// 폼 제출 성공
			return true;
		}
		
		function checkId() {
			const id = document.getElementById('id').value;
			if (id === '') {
				alert('아이디를 입력해주세요.');
				return;
			}
			if (id.length < 4 || id.length > 16) {
				alert('아이디는 4자 이상 16자 이하여야 합니다.');
				return;
			}
			alert('사용 가능한 아이디입니다!');
		}
		
		function sendEmailCode() {
			const email = document.getElementById('email').value;
			if (email === '') {
				alert('이메일을 입력해주세요.');
				return;
			}
			alert('인증번호가 ' + email + '로 전송되었습니다.');
		}
		
		function verifyEmailCode() {
			const code = document.getElementById('email_code').value;
			if (code === '') {
				alert('인증번호를 입력해주세요.');
				return;
			}
			alert('이메일 인증이 완료되었습니다!');
		}
	</script>
</body>
</html>
