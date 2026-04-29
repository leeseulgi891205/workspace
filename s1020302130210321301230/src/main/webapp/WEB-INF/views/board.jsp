<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-4 md:px-6 mt-32 max-w-5xl text-white mb-20">
    
    <div class="flex justify-between items-end mb-8 border-b border-gray-700 pb-4">
        <div>
            <h1 class="font-orbitron text-3xl md:text-4xl font-bold">PRODUCER <span class="text-brand-purple">LOUNGE</span></h1>
            <p class="text-gray-400 mt-2 text-sm md:text-base">오로라 엔터테인먼트 프로듀서들의 자유로운 소통 공간입니다.</p>
        </div>
        
        <a href="${ctx}/board/write" class="px-5 py-2.5 rounded-full bg-gradient-to-r from-brand-purple to-brand-cyan text-white font-bold hover:scale-105 transition-transform flex items-center gap-2 shadow-[0_0_15px_rgba(112,0,255,0.3)]">
            <i class="fas fa-pen"></i> <span class="hidden md:inline">글쓰기</span>
        </a>
    </div>

    <div class="space-y-4">
        <c:choose>
            <c:when test="${not empty posts}">
                <c:forEach var="p" items="${posts}">
                    <div class="bg-gray-900/50 rounded-2xl p-6 border border-gray-800 backdrop-blur-md hover:border-brand-purple hover:-translate-y-1 transition-all duration-300 group shadow-lg">
                        <div class="flex justify-between items-start mb-4">
                            <div>
                                <h3 class="text-xl font-bold text-gray-200 group-hover:text-brand-cyan transition-colors line-clamp-1">
                                    <a href="${ctx}/board/${p.id}">${p.title}</a>
                                </h3>
                                <div class="text-sm text-gray-500 mt-2 font-orbitron flex items-center gap-3">
                                    <span><i class="fas fa-user-circle"></i> 익명 프로듀서</span>
                                    <span><i class="far fa-clock"></i> ${p.createdAt}</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="text-gray-400 text-sm leading-relaxed line-clamp-3 cursor-pointer" onclick="location.href='${ctx}/board/${p.id}'">
                            ${p.content}
                        </div>
                    </div>
                </c:forEach>
            </c:when>
            
            <c:otherwise>
                <div class="flex flex-col items-center justify-center py-20 text-gray-500 bg-gray-900/30 rounded-2xl border border-gray-800 backdrop-blur-md">
                    <i class="fas fa-comments text-4xl mb-4 opacity-50"></i>
                    <p>아직 등록된 게시글이 없습니다. 첫 번째 글을 남겨보세요!</p>
                </div>
            </c:otherwise>
        </c:choose>
    </div>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />