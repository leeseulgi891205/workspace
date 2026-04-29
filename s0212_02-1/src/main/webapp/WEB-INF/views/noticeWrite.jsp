<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AURORA ENTERTAINMENT - 글쓰기</title>
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

        /* 파스텔톤 배경 그라데이션 */
        .ambient-bg {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #FFD1DF 0%, #E8CBF5 50%, #C8D9FF 100%);
        }

        /* 화사한 화이트 글래스모피즘 */
        .premium-glass {
            background: rgba(255, 255, 255, 0.5);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        /* 입력 폼 전용 화이트 유리 질감 */
        .input-glass {
            background: rgba(255, 255, 255, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.9);
            color: #121212;
            transition: all 0.3s ease;
        }

        /* 입력 폼 클릭 시 보라색 포인트 효과 */
        .input-glass:focus {
            outline: none;
            border-color: #9D00FF;
            box-shadow: 0 0 15px rgba(157, 0, 255, 0.15);
            background: rgba(255, 255, 255, 0.9);
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
<body class="pt-32 pb-20">

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

    <div class="container mx-auto px-4 max-w-4xl relative z-10">

        <div class="mb-10 text-center">
            <h1 class="font-orbitron text-3xl md:text-4xl font-bold tracking-wide text-gray-900">NOTICE <span class="text-brand-purple">WRITE</span></h1>
            <div class="h-0.5 w-12 bg-gradient-to-r from-transparent via-brand-purple to-transparent mx-auto mt-4 mb-4"></div>
            <p class="text-gray-600 font-medium tracking-wide">새로운 공지사항을 작성해주세요.</p>
        </div>

        <div class="premium-glass rounded-2xl p-8 md:p-12 border border-white shadow-lg">
            <form action="${ctx}/board/noticeWrite" method="post">

                <div class="mb-6">
                    <label for="title" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">TITLE</label>
                    <input type="text" id="title" name="title" required
                           class="input-glass w-full rounded-xl px-5 py-4 text-base font-medium placeholder-gray-400"
                           placeholder="공지사항 제목을 입력하세요">
                </div>

                <div class="mb-10">
                    <label for="content" class="block text-xs text-brand-purple tracking-widest font-bold mb-2 ml-1">CONTENT</label>
                    <textarea id="content" name="content" rows="12" required
                              class="input-glass w-full rounded-xl px-5 py-4 text-sm font-medium placeholder-gray-400 resize-none leading-relaxed"
                              placeholder="공지사항 내용을 상세히 작성해주세요"></textarea>
                </div>

                <div class="flex justify-end gap-3">
                    <button type="button" onclick="history.back()"
                            class="font-orbitron font-medium text-xs md:text-sm px-8 py-3 rounded-full border border-gray-300 text-gray-500 hover:bg-white transition-all duration-300 tracking-wide">
                        CANCEL
                    </button>
                    <button type="submit"
                            class="font-orbitron font-bold text-xs md:text-sm px-10 py-3 rounded-full bg-gradient-to-r from-brand-purple to-pastel-pink text-white hover:scale-105 shadow-[0_4px_15px_rgba(157,0,255,0.3)] transition-all duration-300 tracking-wide border-none">
                        PUBLISH
                    </button>
                </div>

            </form>
        </div>
    </div>

</body>
</html>
