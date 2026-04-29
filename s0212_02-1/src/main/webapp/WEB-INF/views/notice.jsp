<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AURORA ENTERTAINMENT - NOTICE</title>
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

        /* 메인과 동일한 솜사탕 파스텔톤 배경 그라데이션 */
        .ambient-bg {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #FFD1DF 0%, #E8CBF5 50%, #C8D9FF 100%);
        }

        /* 화사하고 투명한 화이트 글래스모피즘 */
        .premium-glass {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        /* 서브페이지 전용 하얀색 네비게이션 바 */
        .nav-subpage {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.6);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        }
    </style>
</head>
<body>

    <div class="ambient-bg"></div>

    <nav class="nav-subpage fixed top-0 left-0 right-0 z-50 py-3">
        <div class="container mx-auto px-6 h-12 flex items-center justify-between">
            <a href="${ctx}/main" class="font-orbitron text-base font-black tracking-wider flex items-center gap-2 group text-gray-900">
                <i class="fas fa-play text-brand-purple group-hover:text-gray-900 transition-colors text-xs"></i>
                <span>NEXT DEBUT</span>
            </a>

            <ul class="hidden lg:flex items-center gap-6 font-medium text-xs tracking-wide">
                <li><a href="${ctx}/main" class="text-gray-600 hover:text-brand-purple transition-colors">연습생 선택</a></li>
                <li><a href="${ctx}/board/notice" class="text-brand-purple font-bold drop-shadow-[0_0_8px_rgba(157,0,255,0.3)]">공지사항</a></li>
                <li><a href="${ctx}/board/free" class="text-gray-600 hover:text-brand-purple transition-colors">자유게시판</a></li>
                <li><a href="${ctx}/member/signup" class="text-gray-600 hover:text-brand-purple transition-colors">회원가입</a></li>
                <li><a href="${ctx}/member/login" class="text-gray-600 hover:text-brand-purple transition-colors">로그인</a></li>
            </ul>
        </div>
    </nav>

    <div class="container mx-auto px-4 md:px-6 pt-32 pb-20 max-w-5xl relative z-10">

        <div class="flex justify-between items-end mb-8 border-b border-white/60 pb-4">
            <div>
                <h1 class="font-orbitron text-3xl md:text-4xl font-bold tracking-wide text-gray-900">NOTICE <span class="text-brand-purple">BOARD</span></h1>
                <div class="h-0.5 w-16 bg-gradient-to-r from-transparent via-brand-purple to-transparent mb-4 mt-2"></div>
                <p class="text-gray-600 font-medium tracking-wide">오로라 엔터테인먼트의 주요 소식을 확인하세요.</p>
            </div>

            <a href="${ctx}/board/noticeWrite" class="px-6 py-2.5 rounded-full bg-gradient-to-r from-brand-purple to-pastel-pink text-white font-bold text-sm hover:scale-105 transition-transform flex items-center gap-2 shadow-[0_4px_15px_rgba(157,0,255,0.3)] border-none">
                <i class="fas fa-pen text-xs"></i> 글쓰기
            </a>
        </div>

        <div class="premium-glass rounded-2xl overflow-hidden shadow-lg border border-white">

            <div class="hidden md:flex bg-white/60 p-4 border-b border-white/80 text-gray-600 font-bold text-xs tracking-widest text-center">
                <div class="w-20">NO</div>
                <div class="flex-1 text-left px-4">TITLE</div>
                <div class="w-32">DATE</div>
            </div>

            <div class="flex flex-col md:flex-row md:items-center border-b border-white/40 p-5 hover:bg-white/80 transition-colors group cursor-pointer" onclick="location.href='#'">
                <div class="text-brand-purple w-20 text-center font-orbitron font-bold hidden md:block">1</div>
                <div class="flex-1 text-left md:px-4">
                    <span class="inline-block bg-pastel-pink text-brand-purple text-[10px] font-bold px-2 py-0.5 rounded mr-2 mb-1 md:mb-0">안내</span>
                    <a href="#" class="text-base font-bold text-gray-800 group-hover:text-brand-purple transition-colors">오로라 엔터테인먼트 신규 연습생 프로필 공개 안내</a>
                </div>
                <div class="text-gray-500 w-32 text-center text-sm hidden md:block font-orbitron font-medium mt-2 md:mt-0">2026-02-27</div>
            </div>

            <div class="flex flex-col md:flex-row md:items-center border-b border-white/40 p-5 hover:bg-white/80 transition-colors group cursor-pointer" onclick="location.href='#'">
                <div class="text-brand-purple w-20 text-center font-orbitron font-bold hidden md:block">2</div>
                <div class="flex-1 text-left md:px-4">
                    <span class="inline-block bg-pastel-blue text-brand-purple text-[10px] font-bold px-2 py-0.5 rounded mr-2 mb-1 md:mb-0">이벤트</span>
                    <a href="#" class="text-base font-bold text-gray-800 group-hover:text-brand-purple transition-colors">NEXT DEBUT 최종 데뷔조 투표 참여 가이드</a>
                </div>
                <div class="text-gray-500 w-32 text-center text-sm hidden md:block font-orbitron font-medium mt-2 md:mt-0">2026-02-26</div>
            </div>

        </div>

        <div class="flex justify-center mt-10 gap-2 font-orbitron">
            <button class="w-8 h-8 rounded-full border border-brand-purple bg-brand-purple text-white font-bold shadow-md">1</button>
            <button class="w-8 h-8 rounded-full border border-white bg-white/50 text-gray-600 hover:bg-white transition-colors">2</button>
            <button class="w-8 h-8 rounded-full border border-white bg-white/50 text-gray-600 hover:bg-white transition-colors">3</button>
        </div>

    </div>

</body>
</html>
