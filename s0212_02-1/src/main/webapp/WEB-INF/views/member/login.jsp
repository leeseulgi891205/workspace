<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AURORA ENTERTAINMENT - LOGIN</title>
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
        body { font-family: 'pretendard', sans-serif; background-color: #fdf4f8; color: #121212; min-height: 100vh; }
        .ambient-bg { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; z-index: -1; background: linear-gradient(135deg, #FFD1DF 0%, #E8CBF5 50%, #C8D9FF 100%); }
        .premium-glass { background: rgba(255, 255, 255, 0.5); backdrop-filter: blur(24px); -webkit-backdrop-filter: blur(24px); border: 1px solid rgba(255, 255, 255, 0.8); box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); }
        .input-glass { background: rgba(255, 255, 255, 0.6); border: 1px solid rgba(255, 255, 255, 0.9); color: #121212; transition: all 0.3s ease; }
        .input-glass:focus { outline: none; border-color: #9D00FF; box-shadow: 0 0 15px rgba(157, 0, 255, 0.15); background: rgba(255, 255, 255, 0.9); }
        .nav-subpage { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid rgba(255, 255, 255, 0.6); box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03); }
    </style>
</head>
<body class="flex items-center justify-center pt-16">

    <div class="ambient-bg"></div>

    <nav class="nav-subpage fixed top-0 left-0 right-0 z-50 py-3">
        <div class="container mx-auto px-6 h-12 flex items-center justify-between">
            <a href="${ctx}/main" class="font-orbitron text-base font-black tracking-wider flex items-center gap-2 group text-gray-900">
                <i class="fas fa-play text-brand-purple transition-colors text-xs"></i>
                <span>NEXT DEBUT</span>
            </a>
            <ul class="hidden lg:flex items-center gap-6 font-medium text-xs tracking-wide">
                <li><a href="${ctx}/main" class="text-gray-600 hover:text-brand-purple transition-colors">연습생 선택</a></li>
                <li><a href="${ctx}/board/notice" class="text-gray-600 hover:text-brand-purple transition-colors">공지사항</a></li>
                <li><a href="${ctx}/member/signup" class="text-gray-600 hover:text-brand-purple transition-colors">회원가입</a></li>
                <li><a href="${ctx}/member/login" class="text-brand-purple font-bold drop-shadow-[0_0_8px_rgba(157,0,255,0.3)]">로그인</a></li>
            </ul>
        </div>
    </nav>

    <div class="w-full max-w-md px-4 relative z-10">
        <div class="mb-8 text-center mt-6">
            <h1 class="font-orbitron text-3xl md:text-4xl font-bold tracking-wide text-gray-900">LOG <span class="text-brand-purple">IN</span></h1>
            <div class="h-0.5 w-12 bg-gradient-to-r from-transparent via-brand-purple to-transparent mx-auto mt-4 mb-3"></div>
            <p class="text-gray-600 font-medium tracking-wide text-sm">오로라 엔터테인먼트에 접속합니다.</p>
        </div>

        <div class="premium-glass rounded-3xl p-8 md:p-10 border border-white shadow-xl">
            <c:if test="${not empty loginError}">
                <div class="mb-6 p-3 rounded-lg bg-red-100 border border-red-200 text-red-600 text-xs font-bold text-center">
                    <i class="fas fa-exclamation-circle mr-1"></i> ${loginError}
                </div>
            </c:if>

            <form action="${ctx}/member/login" method="post" class="space-y-6">
                <div>
                    <label for="id" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">ID</label>
                    <input type="text" id="id" name="id" required
                           class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                           placeholder="아이디를 입력하세요">
                </div>

                <div>
                    <label for="password" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">PASSWORD</label>
                    <input type="password" id="password" name="password" required
                           class="input-glass w-full rounded-xl px-5 py-3.5 text-sm font-medium placeholder-gray-400"
                           placeholder="비밀번호를 입력하세요">
                </div>

                <div class="pt-4">
                    <button type="submit"
                            class="w-full font-orbitron font-bold text-sm md:text-base px-10 py-4 rounded-full bg-gradient-to-r from-brand-purple to-pastel-pink text-white hover:scale-[1.02] shadow-[0_4px_15px_rgba(157,0,255,0.3)] transition-all duration-300 tracking-wide border-none">
                        ENTER
                    </button>
                </div>

                <div class="text-center mt-6">
                    <p class="text-xs text-gray-500 font-medium">아직 프로듀서가 아니신가요? <a href="${ctx}/member/signup" class="text-brand-purple font-bold hover:underline ml-1">회원가입</a></p>
                </div>
            </form>
        </div>
    </div>

</body>
</html>
