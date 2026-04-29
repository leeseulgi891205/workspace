<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXT DEBUT - 연습생 선택</title>

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

    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/variable/pretendardvariable.css"/>

    <style>
        body {
            font-family: 'pretendard', sans-serif;
            background-color: #fdf4f8;
            color: #121212;
            overflow-x: hidden;
        }

        /* 솜사탕 파스텔톤 배경 그라데이션 (스크롤 내렸을 때 보임) */
        .ambient-bg {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            z-index: -1;
            background: linear-gradient(135deg, #FFD1DF 0%, #E8CBF5 50%, #C8D9FF 100%);
        }

        /* 연습생 카드: 화이트 글래스모피즘 */
        .premium-glass {
            background: rgba(255, 255, 255, 0.4);
            backdrop-filter: blur(24px);
            -webkit-backdrop-filter: blur(24px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
        }

        .trainee-card {
            position: relative;
            transition: all 0.5s cubic-bezier(0.165, 0.84, 0.44, 1);
            overflow: hidden;
        }

        .trainee-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(232, 203, 245, 0.8);
            border-color: #ffffff;
            background: rgba(255, 255, 255, 0.6);
        }

        .img-overlay {
            background: linear-gradient(to bottom, transparent 20%, rgba(255,255,255,0.95) 100%);
        }

        .card-selected {
            border: 2px solid #9D00FF !important;
            box-shadow: 0 0 25px rgba(157, 0, 255, 0.2), inset 0 0 15px rgba(255, 255, 255, 0.5) !important;
            background: rgba(255, 255, 255, 0.8) !important;
        }

        .card-selected .select-badge {
            opacity: 1;
            transform: scale(1);
        }

        .select-badge {
            opacity: 0;
            transform: scale(0.8);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        /* 프로그레스 바 파스텔톤 적용 */
        .skill-bar-vocal { background: linear-gradient(90deg, #FFD1DF, #E8CBF5); }
        .skill-bar-dance { background: linear-gradient(90deg, #C8D9FF, #E8CBF5); }

        .skill-bar {
            position: relative;
            overflow: hidden;
        }
        .skill-bar::after {
            content: '';
            position: absolute;
            top: 0; left: 0; bottom: 0; right: 0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.6), transparent);
            transform: translateX(-100%);
            animation: shimmer 2s infinite;
        }
        @keyframes shimmer {
            100% { transform: translateX(100%); }
        }

        /* 하단 고정 바 (화이트 유리) */
        .bottom-bar {
            background: rgba(255, 255, 255, 0.8);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(255, 255, 255, 0.5);
            box-shadow: 0 -5px 20px rgba(0,0,0,0.03);
        }

        /* 스크롤 다운 네비게이션 바 (투명한 하얀색) */
        .nav-scrolled {
            background: rgba(255, 255, 255, 0.85) !important;
            backdrop-filter: blur(24px) !important;
            -webkit-backdrop-filter: blur(24px) !important;
            border-bottom: 1px solid rgba(255, 255, 255, 0.5) !important;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05) !important;
        }
    </style>
</head>
<body>

    <div class="ambient-bg"></div>

    <nav id="navbar" class="fixed top-0 left-0 right-0 z-50 transition-all duration-500 bg-transparent py-4">
        <div class="container mx-auto px-6 flex items-center justify-between">
            <a href="${ctx}/main" id="nav-logo" class="font-orbitron text-base font-black tracking-wider flex items-center gap-2 text-white transition-colors">
                <i class="fas fa-play text-brand-purple text-xs"></i>
                <span>NEXT DEBUT</span>
            </a>

            <ul class="hidden lg:flex items-center gap-6 font-medium text-xs tracking-wide">
                <li><a href="${ctx}/main" class="nav-link text-brand-purple">연습생 선택</a></li>
                <li><a href="${ctx}/board/notice" class="nav-link text-gray-300 hover:text-white transition-colors">공지사항</a></li>
                <li><a href="${ctx}/board/free" class="nav-link text-gray-300 hover:text-white transition-colors">자유게시판</a></li>
                <li><a href="${ctx}/member/signup" class="nav-link text-gray-300 hover:text-white transition-colors">회원가입</a></li>
                <li><a href="${ctx}/member/login" class="nav-link text-gray-300 hover:text-white transition-colors">로그인</a></li>
            </ul>
        </div>
    </nav>

    <section class="relative h-screen flex items-center justify-center bg-cover bg-center bg-no-repeat"
         style="background-image: url('${ctx}/images/1234.jpg');">

        <div class="absolute inset-0 bg-black/80 z-0"></div>

        <div class="text-center px-6 z-10 w-full max-w-5xl mx-auto relative mt-10">
            <p class="font-orbitron text-xs md:text-sm tracking-[0.5em] text-gray-400 mb-4 font-semibold opacity-90">
                AURORA ENTERTAINMENT PRESENTS
            </p>

            <h1 class="font-orbitron text-5xl sm:text-6xl md:text-8xl font-black mb-6 whitespace-nowrap leading-none tracking-tight text-white drop-shadow-lg">
                THE NEXT DEBUT
            </h1>

            <p class="text-base md:text-lg font-light mb-12 tracking-wide text-gray-300">
                새로운 시대를 열어갈 당신만의 아이돌 그룹을 완성하세요.
            </p>

            <button onclick="scrollToSelection()" class="px-8 py-2.5 font-orbitron font-medium text-xs md:text-sm rounded-full border border-gray-400 bg-transparent hover:bg-white hover:text-black transition-colors duration-300 text-white flex items-center gap-3 mx-auto backdrop-blur-sm">
                ENTER THE STAGE <i class="fas fa-arrow-down"></i>
            </button>
        </div>
    </section>

    <div class="container mx-auto px-4 md:px-6 mb-40 relative z-10 pt-16" id="selection-section">
        <div class="flex flex-col items-center mb-16">
            <h2 class="font-orbitron text-3xl md:text-4xl font-bold mb-4 tracking-wide text-gray-900">TRAINEE <span class="text-brand-purple">ROSTER</span></h2>
            <div class="h-0.5 w-16 bg-gradient-to-r from-transparent via-brand-purple to-transparent mb-4"></div>
            <p class="text-gray-600 font-medium tracking-wide">데뷔조에 합류할 최정예 멤버 4명을 선발해 주세요.</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-4 md:gap-6">
            <c:forEach var="trainee" items="${traineeList}">
                <div class="trainee-card premium-glass rounded-xl cursor-pointer"
                     onclick="TraineeSelector.selectTrainee('${trainee.name}')"
                     data-trainee="${trainee.name}">

                    <div class="select-badge absolute top-3 right-3 z-20 bg-gradient-to-r from-pastel-pink to-brand-purple text-white w-7 h-7 rounded-full flex items-center justify-center shadow-[0_0_10px_rgba(157,0,255,0.3)]">
                        <i class="fas fa-check text-xs"></i>
                    </div>

                    <div class="relative h-72 w-full">
					    <img src="${ctx}/images/${trainee.image}" alt="${trainee.name}" class="w-full h-full object-contain">
					    <div class="absolute inset-0 img-overlay z-10"></div>

                        <div class="absolute bottom-0 left-0 right-0 p-4 z-20">
                            <p class="text-brand-purple text-[10px] font-bold tracking-widest mb-1 uppercase">${trainee.genre}</p>
                            <h3 class="font-orbitron text-xl font-black text-gray-900 mb-3 tracking-wide">${trainee.name}</h3>

                            <div class="space-y-2">
                                <div>
                                    <div class="flex justify-between text-[10px] text-gray-600 mb-1 font-medium tracking-wider">
                                        <span>VOCAL</span>
                                        <span class="font-orbitron text-gray-900 font-bold">${trainee.vocal}%</span>
                                    </div>
                                    <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden">
                                        <div class="skill-bar skill-bar-vocal h-full rounded-full" style="width: ${trainee.vocal}%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-[10px] text-gray-600 mb-1 font-medium tracking-wider">
                                        <span>DANCE</span>
                                        <span class="font-orbitron text-gray-900 font-bold">${trainee.dance}%</span>
                                    </div>
                                    <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden">
                                        <div class="skill-bar skill-bar-dance h-full rounded-full" style="width: ${trainee.dance}%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </c:forEach>
        </div>
    </div>

    <div class="fixed bottom-0 left-0 right-0 bottom-bar h-16 flex items-center z-50">
        <div class="container mx-auto px-6 flex items-center justify-between">

            <div class="flex flex-col">
                <span class="text-gray-500 text-[10px] tracking-widest font-bold mb-0.5 uppercase">SELECTED TRAINEES</span>
                <div class="flex items-center gap-2 font-orbitron text-gray-600 text-sm">
                    <span id="selected-count" class="bg-brand-purple text-white font-bold px-2 py-0.5 text-sm rounded-md shadow-sm">0</span>
                    <span class="font-medium">/ 4</span>
                </div>
            </div>

            <button id="next-btn"
                    class="font-orbitron font-medium text-xs md:text-sm px-6 py-2 rounded-full border border-gray-300 text-gray-400 bg-gray-100/50 cursor-not-allowed transition-all duration-300 flex items-center gap-2 tracking-wide"
                    onclick="TraineeSelector.submitSelection(this)"
                    disabled>
                <span id="btn-text">CONFIRM LINEUP</span> <i class="fas fa-chevron-right text-[10px]"></i>
            </button>
        </div>
    </div>

<script>
    const TraineeSelector = (() => {
        const state = { selectedTrainees: [], maxSelection: 4, isSubmitting: false };
        const elements = {
            selectedCount: null, nextButton: null, btnText: null, traineeCards: null
        };

        const init = () => {
            elements.selectedCount = document.getElementById('selected-count');
            elements.nextButton = document.getElementById('next-btn');
            elements.btnText = document.getElementById('btn-text');
            elements.traineeCards = document.querySelectorAll('[data-trainee]');
        };

        const selectTrainee = (name) => {
            if (state.isSubmitting) return;
            const card = Array.from(elements.traineeCards).find(c => c.getAttribute('data-trainee') === name);
            if (!card) return;

            if (state.selectedTrainees.includes(name)) {
                state.selectedTrainees = state.selectedTrainees.filter(n => n !== name);
                card.classList.remove('card-selected');
            } else {
                if (state.selectedTrainees.length >= state.maxSelection) {
                    alert("데뷔조 4명이 모두 선택되었습니다.");
                    return;
                }
                state.selectedTrainees.push(name);
                card.classList.add('card-selected');
            }
            updateUI();
        };

        const updateUI = () => {
            if (elements.selectedCount) {
                elements.selectedCount.textContent = state.selectedTrainees.length;
            }

            if (elements.nextButton && !state.isSubmitting) {
                const isComplete = state.selectedTrainees.length === state.maxSelection;
                elements.nextButton.disabled = !isComplete;

                if (isComplete) {
                    elements.nextButton.className = "font-orbitron font-bold text-xs md:text-sm px-6 py-2 rounded-full bg-gradient-to-r from-brand-purple to-pastel-pink text-white hover:scale-105 transition-all duration-300 flex items-center gap-2 tracking-wide cursor-pointer shadow-[0_4px_15px_rgba(157,0,255,0.3)] border-none";
                } else {
                    elements.nextButton.className = "font-orbitron font-medium text-xs md:text-sm px-6 py-2 rounded-full border border-gray-300 text-gray-400 bg-gray-100/50 cursor-not-allowed transition-all duration-300 flex items-center gap-2 tracking-wide";
                }
            }
        };

        const submitSelection = (btnElement) => {
            if (state.selectedTrainees.length !== state.maxSelection || state.isSubmitting) return;
            state.isSubmitting = true;

            if (elements.btnText) {
                elements.btnText.innerHTML = '<i class="fas fa-circle-notch fa-spin mr-2"></i> PROCESSING';
            }
            btnElement.classList.add('opacity-80', 'cursor-wait');

            const form = document.createElement('form');
            form.method = 'POST';
            form.action = '${ctx}/concept/selection';

            state.selectedTrainees.forEach((name, index) => {
                const input = document.createElement('input');
                input.type = 'hidden';
                input.name = `trainees[\${index}]`;
                input.value = name;
                form.appendChild(input);
            });

            document.body.appendChild(form);
            form.submit();
        };

        const scrollToSelection = () => {
            const section = document.getElementById('selection-section');
            if (section) {
                const y = section.getBoundingClientRect().top + window.scrollY - 100;
                window.scrollTo({top: y, behavior: 'smooth'});
            }
        };

        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
        else init();

        return { selectTrainee, submitSelection, scrollToSelection };
    })();

    function scrollToSelection() { TraineeSelector.scrollToSelection(); }

    // 스크롤 시 네비게이션 디자인 변경 로직
    window.addEventListener('scroll', () => {
        const navbar = document.getElementById('navbar');
        const navLogo = document.getElementById('nav-logo');
        const navLinks = document.querySelectorAll('.nav-link');

        if (navbar) {
            // 스크롤을 내려서 파스텔 배경 구역으로 왔을 때
            if (window.scrollY > 50) {
                navbar.classList.add('nav-scrolled');
                navbar.classList.remove('bg-transparent');

                // 네비게이션 텍스트 어둡게 (가독성 확보)
                navLogo.classList.replace('text-white', 'text-gray-900');
                navLinks.forEach(link => {
                    if(!link.classList.contains('text-brand-purple')) {
                        link.classList.replace('text-gray-300', 'text-gray-600');
                        link.classList.replace('hover:text-white', 'hover:text-brand-purple');
                    }
                });
            } else {
                // 맨 위(마이크 사진 있는 다크 구역)로 올라왔을 때
                navbar.classList.remove('nav-scrolled');
                navbar.classList.add('bg-transparent');

                // 텍스트를 다시 하얗게 복구
                navLogo.classList.replace('text-gray-900', 'text-white');
                navLinks.forEach(link => {
                    if(!link.classList.contains('text-brand-purple')) {
                        link.classList.replace('text-gray-600', 'text-gray-300');
                        link.classList.replace('hover:text-brand-purple', 'hover:text-white');
                    }
                });
            }
        }
    });
</script>
</body>
</html>
