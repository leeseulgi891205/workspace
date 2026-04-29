<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-4 md:px-6 mt-32 max-w-5xl text-white mb-20">
    
    <div class="flex justify-between items-end mb-6 border-b border-gray-700 pb-4">
        <div>
            <h1 class="font-orbitron text-3xl md:text-4xl font-bold">NOTICE <span class="text-brand-pink">BOARD</span></h1>
            <p class="text-gray-400 mt-2 text-sm md:text-base">오로라 엔터테인먼트의 주요 소식을 확인하세요.</p>
        </div>
        
        <a href="${ctx}/notice/write" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-brand-cyan to-brand-pink text-white font-bold hover:scale-105 transition-transform flex items-center gap-2 shadow-[0_0_15px_rgba(0,229,255,0.3)]">
            <i class="fas fa-pen"></i> <span class="hidden md:inline">글쓰기</span>
        </a>
    </div>

    <div class="bg-gray-900/50 rounded-lg border border-gray-800 backdrop-blur-md overflow-hidden">
        
        <div class="hidden md:flex bg-gray-800/80 p-4 border-b border-gray-700 text-gray-400 font-semibold text-sm text-center">
            <div class="w-20">NO</div>
            <div class="flex-1 text-left px-4">제목</div>
            <div class="w-32">등록일</div>
            <div class="w-32">관리</div>
        </div>

        <c:choose>
            <c:when test="${not empty notices}">
                <c:forEach var="n" items="${notices}">
                    <div class="flex flex-col md:flex-row md:items-center border-b border-gray-800/50 p-4 hover:bg-gray-800/40 transition-colors group">
                        
                        <div class="text-gray-500 w-20 text-center font-orbitron hidden md:block">${n.id}</div>
                        
                        <div class="flex-1 text-left md:px-4 mb-2 md:mb-0">
                            <a href="${ctx}/notice/${n.id}" class="text-lg font-medium text-gray-200 group-hover:text-brand-cyan transition-colors line-clamp-1">
                                ${n.title}
                            </a>
                            <div class="text-xs text-gray-500 md:hidden mt-2 font-orbitron">
                                NO. ${n.id} &nbsp;|&nbsp; ${n.createdAt}
                            </div>
                        </div>
                        
                        <div class="text-gray-400 w-32 text-center text-sm hidden md:block font-orbitron">
                            ${n.createdAt}
                        </div>
                        
                        <div class="w-full md:w-32 flex gap-2 justify-end md:justify-center mt-3 md:mt-0">
                            <a href="${ctx}/notice/${n.id}/edit" class="text-xs px-3 py-1.5 rounded border border-gray-600 text-gray-400 hover:text-white hover:border-brand-cyan transition-colors">수정</a>
                            <form action="${ctx}/notice/${n.id}/delete" method="post" class="inline" onsubmit="return confirm('이 공지사항을 정말 삭제하시겠습니까?');">
                                <button type="submit" class="text-xs px-3 py-1.5 rounded border border-red-900/50 text-red-400 bg-red-900/20 hover:bg-red-600 hover:text-white transition-colors">삭제</button>
                            </form>
                        </div>
                        
                    </div>
                </c:forEach>
            </c:when>
            
            <c:otherwise>
                <div class="flex flex-col items-center justify-center py-20 text-gray-500">
                    <i class="fas fa-inbox text-4xl mb-4 opacity-50"></i>
                    <p>등록된 공지사항이 없습니다.</p>
                </div>
            </c:otherwise>
        </c:choose>
    </div>
    
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />