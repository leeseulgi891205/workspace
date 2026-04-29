<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AURORA ENTERTAINMENT - SIGN UP</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        'pastel-pink': '#FFD1DF',
                        'pastel-purple': '#E8CBF5',
                        'pastel-blue': '#C8D9FF',
                        'brand-purple': '#9D00FF'
                    },
                    fontFamily: {
                        'orbitron': ['Orbitron', 'sans-serif'],
                        'pretendard': ['Pretendard Variable', 'Pretendard', '-apple-system', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        body {
            font-family: 'pretendard', sans-serif;
            background-color: #fdf4f8;
            color: #121212;
            min-height: 100vh;
        }
        .ambient-bg {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #FFD1DF 0%, #E8CBF5 50%, #C8D9FF 100%);
        }
        .premium-glass {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }
        .input-glass {
            background: rgba(255, 255, 255, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.9);
            color: #121212;
            transition: all 0.3s ease;
        }
        .input-glass:focus {
            outline: none;
            border-color: #9D00FF;
            box-shadow: 0 0 15px rgba(157, 0, 255, 0.15);
            background: rgba(255, 255, 255, 0.9);
        }
        .nav-subpage {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        }
    </style>
</head>
<body class="pt-24 pb-20">

    <div class="ambient-bg"></div>

    <nav class="nav-subpage fixed top-0 left-0 right-0 z-50 py-3">
        <div class="container mx-auto px-6 h-12 flex items-center justify-between">
            <a href="${ctx}/main" class="font-orbitron text-base font-black tracking-wider flex items-center gap-2 group text-gray-900">
                <i class="fas fa-play text-brand-purple group-hover:text-gray-900 transition-colors text-xs"></i>
                <span>NEXT DEBUT</span>
            </a>

            <ul class="hidden lg:flex items-center gap-6 font-medium text-xs tracking-wide">
                <li><a href="${ctx}/main" class="text-gray-600 hover:text-brand-purple transition-colors">연습생 선택</a></li>
                <li><a href="${ctx}/board/notice" class="text-gray-600 hover:text-brand-purple transition-colors">공지사항</a></li>
                <li><a href="${ctx}/board/free" class="text-gray-600 hover:text-brand-purple transition-colors">자유게시판</a></li>
                <li><a href="${ctx}/member/signup" class="text-brand-purple font-bold drop-shadow-[0_0_8px_rgba(157,0,255,0.3)]">회원가입</a></li>
                <li><a href="${ctx}/member/login" class="text-gray-600 hover:text-brand-purple transition-colors">로그인</a></li>
            </ul>
        </div>
    </nav>

    <div class="container mx-auto px-4 max-w-2xl relative z-10">

        <div class="mb-8 text-center mt-6">
            <h1 class="font-orbitron text-3xl md:text-4xl font-bold tracking-wide text-gray-900">SIGN <span class="text-brand-purple">UP</span></h1>
            <div class="h-0.5 w-12 bg-gradient-to-r from-transparent via-brand-purple to-transparent mx-auto mt-4 mb-3"></div>
            <p class="text-gray-600 font-medium tracking-wide">오로라 엔터테인먼트의 프로듀서가 되어주세요.</p>
        </div>

        <div class="premium-glass rounded-3xl p-8 md:p-10 border border-white shadow-xl">
            <form action="${ctx}/member/signup" method="post" id="signupForm" class="space-y-6">

                <div>
                    <label for="id" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">ID *</label>
                    <input type="text" id="id" name="id" required
                           class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                           placeholder="사용하실 아이디를 입력하세요">
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="password" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">PASSWORD *</label>
                        <input type="password" id="password" name="password" required onkeyup="checkPasswordMatch()"
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="비밀번호">
                    </div>
                    <div>
                        <label for="password_confirm" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">PASSWORD CONFIRM *</label>
                        <input type="password" id="password_confirm" required onkeyup="checkPasswordMatch()"
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="비밀번호 확인">
                        <p id="pw_msg" class="text-xs font-bold mt-2 ml-1 hidden"></p>
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="name" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">NAME *</label>
                        <input type="text" id="name" name="name" required
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="이름을 입력하세요">
                    </div>
                    <div>
                        <label for="favorite_idol" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">FAVORITE IDOL</label>
                        <input type="text" id="favorite_idol" name="favorite_idol"
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="가장 좋아하는 아이돌 (선택)">
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div>
                        <label for="email" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">E-MAIL *</label>
                        <input type="email" id="email" name="email" required
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="이메일 주소">
                    </div>
                    <div>
                        <label for="phone" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">PHONE NUMBER *</label>
                        <input type="tel" id="phone" name="phone" required
                               class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                               placeholder="010-0000-0000">
                    </div>
                </div>

                <div>
                    <label for="address" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">ADDRESS</label>
                    <input type="text" id="address" name="address"
                           class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                           placeholder="주소를 입력하세요 (선택)">
                </div>

                <div class="pt-6">
                    <button type="submit" id="submit-btn"
                            class="w-full font-orbitron font-bold text-sm md:text-base px-10 py-4 rounded-full bg-gradient-to-r from-brand-purple to-pastel-pink text-white hover:scale-[1.02] shadow-[0_4px_15px_rgba(157,0,255,0.3)] transition-all duration-300 tracking-wide border-none">
                        JOIN AURORA ENT
                    </button>
                </div>

                <div class="text-center mt-6">
                    <p class="text-xs text-gray-500 font-medium">이미 프로듀서로 등록하셨나요? <a href="${ctx}/member/login" class="text-brand-purple font-bold hover:underline ml-1">로그인</a></p>
                </div>
            </form>
        </div>
    </div>

<script>
    // 비밀번호 일치 검사 자바스크립트
    function checkPasswordMatch() {
        const password = document.getElementById('password').value;
        const confirm = document.getElementById('password_confirm').value;
        const msg = document.getElementById('pw_msg');
        const submitBtn = document.getElementById('submit-btn');

        // 확인란이 비어있으면 메시지 숨김
        if (confirm === '') {
            msg.classList.add('hidden');
            return;
        }

        msg.classList.remove('hidden');

        if (password !== confirm) {
            msg.textContent = '비밀번호가 일치하지 않습니다.';
            msg.className = 'text-xs font-bold mt-2 ml-1 text-red-500';

            // 제출 버튼 비활성화
            submitBtn.disabled = true;
            submitBtn.classList.add('opacity-50', 'cursor-not-allowed');
            submitBtn.classList.remove('hover:scale-[1.02]', 'shadow-[0_4px_15px_rgba(157,0,255,0.3)]');
        } else {
            msg.textContent = '비밀번호가 일치합니다.';
            msg.className = 'text-xs font-bold mt-2 ml-1 text-brand-purple';

            // 제출 버튼 활성화
            submitBtn.disabled = false;
            submitBtn.classList.remove('opacity-50', 'cursor-not-allowed');
            submitBtn.classList.add('hover:scale-[1.02]', 'shadow-[0_4px_15px_rgba(157,0,255,0.3)]');
        }
    }
</script>
</body>
</html>
