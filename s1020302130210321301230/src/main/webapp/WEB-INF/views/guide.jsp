<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-4 md:px-6 mt-32 max-w-5xl text-white mb-32">
    
    <div class="text-center mb-16 flex flex-col items-center">
        <p class="font-orbitron text-sm md:text-base tracking-[0.5em] text-brand-cyan mb-4 font-semibold opacity-80">
            AURORA ENTERTAINMENT
        </p>
        <h1 class="font-orbitron text-4xl md:text-5xl font-black mb-6">
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-brand-cyan to-brand-pink">PRODUCER GUIDE</span>
        </h1>
        <p class="text-gray-400 text-lg">당신만의 아이돌 그룹을 데뷔시키는 3단계 완벽 가이드</p>
        <div class="h-1 w-20 bg-gradient-to-r from-brand-cyan to-brand-pink rounded-full mt-8"></div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
        
        <div class="hidden md:block absolute top-1/2 left-10 right-10 h-0.5 bg-gray-800 -z-10 transform -translate-y-1/2"></div>

        <div class="bg-gray-900/80 rounded-2xl p-8 border border-gray-700 backdrop-blur-md hover:-translate-y-2 hover:border-brand-cyan transition-all duration-300 relative group text-center shadow-lg">
            <div class="w-16 h-16 mx-auto bg-gray-800 border-2 border-brand-cyan rounded-full flex items-center justify-center text-2xl text-brand-cyan mb-6 group-hover:scale-110 group-hover:shadow-[0_0_15px_rgba(0,229,255,0.5)] transition-all">
                <i class="fas fa-users"></i>
            </div>
            <h3 class="font-orbitron text-2xl font-bold mb-2">STEP 01</h3>
            <h4 class="text-lg font-bold text-white mb-4">연습생 선발</h4>
            <p class="text-gray-400 text-sm leading-relaxed break-keep">
                오로라엔터테이먼트의 최정예 연습생 중 데뷔조에 합류할 3명의 핵심 멤버를 직접 선택하세요. 보컬과 댄스 밸런스가 중요합니다.
            </p>
        </div>

        <div class="bg-gray-900/80 rounded-2xl p-8 border border-gray-700 backdrop-blur-md hover:-translate-y-2 hover:border-brand-pink transition-all duration-300 relative group text-center shadow-lg mt-0 md:mt-10">
            <div class="w-16 h-16 mx-auto bg-gray-800 border-2 border-brand-pink rounded-full flex items-center justify-center text-2xl text-brand-pink mb-6 group-hover:scale-110 group-hover:shadow-[0_0_15px_rgba(255,0,127,0.5)] transition-all">
                <i class="fas fa-palette"></i>
            </div>
            <h3 class="font-orbitron text-2xl font-bold mb-2">STEP 02</h3>
            <h4 class="text-lg font-bold text-white mb-4">콘셉트 설정</h4>
            <p class="text-gray-400 text-sm leading-relaxed break-keep">
                청량, 걸크러쉬, 몽환 등 그룹의 정체성을 결정할 데뷔 콘셉트를 설정하세요. 선택한 콘셉트에 따라 결과 화면이 달라집니다.
            </p>
        </div>

        <div class="bg-gray-900/80 rounded-2xl p-8 border border-gray-700 backdrop-blur-md hover:-translate-y-2 hover:border-brand-purple transition-all duration-300 relative group text-center shadow-lg">
            <div class="w-16 h-16 mx-auto bg-gray-800 border-2 border-brand-purple rounded-full flex items-center justify-center text-2xl text-brand-purple mb-6 group-hover:scale-110 group-hover:shadow-[0_0_15px_rgba(112,0,255,0.5)] transition-all">
                <i class="fas fa-trophy"></i>
            </div>
            <h3 class="font-orbitron text-2xl font-bold mb-2">STEP 03</h3>
            <h4 class="text-lg font-bold text-white mb-4">최종 데뷔</h4>
            <p class="text-gray-400 text-sm leading-relaxed break-keep">
                모든 프로듀싱이 끝났습니다. 화려한 무대 위에서 당신이 직접 기획한 아이돌 그룹의 성공적인 데뷔 결과를 확인하세요!
            </p>
        </div>

    </div>

    <div class="mt-20 text-center">
        <a href="${ctx}/main" class="inline-flex items-center gap-3 px-8 py-3 rounded-full border border-gray-600 text-gray-300 hover:bg-white hover:text-black hover:border-white transition-all duration-300 font-orbitron font-bold text-lg group">
            <i class="fas fa-arrow-left group-hover:-translate-x-1 transition-transform"></i> BACK TO MAIN
        </a>
    </div>

</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />