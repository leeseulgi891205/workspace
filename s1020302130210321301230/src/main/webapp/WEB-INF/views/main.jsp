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
                        'brand-dark': '#0B0B12',
                        'brand-cyan': '#00E5FF',
                        'brand-pink': '#FF007F',
                        'brand-purple': '#7000FF'
                    },
                    fontFamily: {
                        'orbitron': ['Orbitron', 'sans-serif'],
                        'pretendard': ['Pretendard Variable', 'Pretendard', '-apple-system', 'sans-serif'],
                    }
                }
            }
        }
    </script>

    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.8/dist/web/variable/pretendardvariable.css"/>

    <style>
        body {
            font-family: 'pretendard', sans-serif;
            background: linear-gradient(
                to bottom,
                rgb(233, 176, 196) 0%,
                rgb(204, 186, 216) 50%,
                rgb(186, 198, 220) 100%
            );
            color: #1a1a1a;
            overflow-x: hidden;
            min-height: 100vh;
        }

        /* 깔끔한 텍스트 그라데이션 */
        .text-gradient-subtle {
            background: linear-gradient(to right, #4a4a4a 0%, #8b7ba8 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* 심플한 텍스트 그라데이션 */
        .text-gradient-primary {
            background: linear-gradient(135deg, #d946a6, #8b5cf6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        /* 미니멀 카드 스타일 */
        .trainee-card {
            position: relative;
            transition: all 0.3s ease;
            overflow: hidden;
            background: white;
            border: none;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        }

        .trainee-card:hover {
            transform: translateY(-4px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.12);
        }

        /* 이미지 오버레이 제거 - 깔끔한 이미지 */
        .img-overlay {
            background: linear-gradient(to bottom, transparent 60%, rgba(255, 255, 255, 0.95) 100%);
        }

        /* 선택된 카드 - 심플한 스타일 */
        .card-selected {
            border: 3px solid #d946a6 !important;
            box-shadow: 0 4px 12px rgba(217, 70, 166, 0.3) !important;
        }

        .card-selected .select-badge {
            opacity: 1;
            transform: scale(1);
        }

        .select-badge {
            opacity: 0;
            transform: scale(0.8);
            transition: all 0.3s ease;
        }

        /* 깔끔한 프로그레스 바 */
        .skill-bar {
            position: relative;
            overflow: hidden;
            transition: width 0.6s ease;
        }

        /* 하단 고정 바 - 화이트 */
        .bottom-bar {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-top: 1px solid rgba(0, 0, 0, 0.08);
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
        }

        /* 버튼 스타일 */
        .btn-primary {
            background: linear-gradient(135deg, #d946a6, #8b5cf6);
            transition: all 0.3s ease;
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(217, 70, 166, 0.4);
        }

        .btn-disabled {
            background: #e5e5e5;
            color: #999;
        }
    </style>
</head>
<body>

    <jsp:include page="/WEB-INF/views/include/header.jsp" />

    <section class="relative min-h-screen flex items-center justify-center pt-20 pb-20 px-6">
        <div class="text-center w-full max-w-4xl mx-auto">
            <p class="text-sm md:text-base tracking-[0.3em] text-gray-600 mb-8 font-medium uppercase">
                Aurora Entertainment
            </p>

            <h1 class="text-5xl sm:text-6xl md:text-7xl lg:text-8xl font-black mb-8 leading-tight">
                <span class="text-gradient-primary">THE NEXT<br/>DEBUT</span>
            </h1>

            <p class="text-gray-700 text-lg md:text-xl font-normal mb-12 max-w-2xl mx-auto leading-relaxed">
                새로운 시대를 열어갈<br/>당신만의 아이돌 그룹을 완성하세요
            </p>

            <button onclick="scrollToSelection()" class="btn-primary text-white px-12 py-4 rounded-full font-bold text-base hover:shadow-lg transition-all duration-300">
                START <i class="fas fa-arrow-right ml-2"></i>
            </button>
        </div>
    </section>
    <div class="container mx-auto px-4 md:px-6 mb-40" id="selection-section">
        <div class="flex flex-col items-center mb-16 text-center">
            <h2 class="text-4xl md:text-5xl font-bold mb-3 text-gray-900">TRAINEE ROSTER</h2>
            <p class="text-gray-600 text-base md:text-lg">데뷔조에 합류할 최정예 멤버 3명을 선발해 주세요</p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 gap-6">
            <c:forEach var="trainee" items="${traineeList}">
                <div class="trainee-card rounded-xl cursor-pointer overflow-hidden"
                     onclick="TraineeSelector.selectTrainee('${trainee.name}')"
                     data-trainee="${trainee.name}">

                    <div class="select-badge absolute top-3 right-3 z-30 bg-gradient-to-r from-pink-500 to-purple-500 text-white w-8 h-8 rounded-full flex items-center justify-center shadow-lg">
                        <i class="fas fa-check text-sm"></i>
                    </div>

                    <div class="relative">
					    <img src="${ctx}/images/${trainee.image}" alt="${trainee.name}" class="w-full h-64 object-cover">
					    <div class="absolute inset-0 img-overlay z-10"></div>

                        <div class="absolute bottom-0 left-0 right-0 p-4 z-20">
                            <p class="text-purple-600 text-xs font-semibold tracking-wider mb-1 uppercase">${trainee.genre}</p>
                            <h3 class="text-xl font-bold text-gray-900 mb-3">${trainee.name}</h3>

                            <div class="space-y-2">
                                <div>
                                    <div class="flex justify-between text-xs text-gray-700 mb-1 font-medium">
                                        <span>VOCAL</span>
                                        <span class="text-pink-500 font-semibold">${trainee.vocal}%</span>
                                    </div>
                                    <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden">
                                        <div class="skill-bar h-full bg-gradient-to-r from-pink-400 to-pink-500 rounded-full" style="width: ${trainee.vocal}%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between text-xs text-gray-700 mb-1 font-medium">
                                        <span>DANCE</span>
                                        <span class="text-purple-500 font-semibold">${trainee.dance}%</span>
                                    </div>
                                    <div class="h-1.5 bg-gray-200 rounded-full overflow-hidden">
                                        <div class="skill-bar h-full bg-gradient-to-r from-purple-400 to-purple-500 rounded-full" style="width: ${trainee.dance}%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </c:forEach>
        </div>
    </div>

    <div class="fixed bottom-0 left-0 right-0 bottom-bar z-50">
        <div class="container mx-auto px-6 h-20 flex items-center justify-between">
            <div class="flex items-center gap-6">
                <div class="flex items-baseline gap-2">
                    <span id="selected-count" class="text-4xl font-black text-gray-900">0</span>
                    <span class="text-xl text-gray-500 font-medium">/ 3</span>
                </div>
                <span class="text-sm text-gray-600 font-medium">SELECTED</span>
            </div>

            <button id="next-btn"
                    class="btn-disabled font-bold text-base px-10 py-3.5 rounded-full cursor-not-allowed transition-all duration-300 flex items-center gap-2"
                    onclick="TraineeSelector.submitSelection(this)"
                    disabled>
                <span id="btn-text">NEXT</span>
                <i class="fas fa-arrow-right text-sm"></i>
            </button>
        </div>
    </div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />

<script>
    const TraineeSelector = (() => {
        const state = { selectedTrainees: [], maxSelection: 3, isSubmitting: false };
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
                    // 세련된 방식의 알림으로 변경 가능하지만 우선 alert 유지
                    alert("데뷔조 3명이 모두 선택되었습니다.");
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
                // 숫자가 바뀔 때 살짝 커졌다 작아지는 애니메이션
                elements.selectedCount.style.transform = 'scale(1.3)';
                setTimeout(() => { elements.selectedCount.style.transform = 'scale(1)'; }, 150);
                elements.selectedCount.style.transition = 'transform 0.15s ease';
            }

            if (elements.nextButton && !state.isSubmitting) {
                const isComplete = state.selectedTrainees.length === state.maxSelection;
                elements.nextButton.disabled = !isComplete;

                if (isComplete) {
                    elements.nextButton.className = "btn-primary text-white font-bold text-base px-10 py-3.5 rounded-full hover:shadow-lg transition-all duration-300 flex items-center gap-2 cursor-pointer";
                } else {
                    elements.nextButton.className = "btn-disabled font-bold text-base px-10 py-3.5 rounded-full cursor-not-allowed transition-all duration-300 flex items-center gap-2";
                }
            }
        };

        const submitSelection = (btnElement) => {
            if (state.selectedTrainees.length !== state.maxSelection || state.isSubmitting) return;
            state.isSubmitting = true;

            if (elements.btnText) {
                elements.btnText.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
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
                const y = section.getBoundingClientRect().top + window.scrollY - 100; // 헤더 높이만큼 보정
                window.scrollTo({top: y, behavior: 'smooth'});
            }
        };

        if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
        else init();

        return { selectTrainee, submitSelection, scrollToSelection };
    })();

    function scrollToSelection() { TraineeSelector.scrollToSelection(); }
</script>
</body>
</html>
