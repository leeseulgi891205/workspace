<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-4 md:px-6 mt-32">
    <div class="mb-6 flex items-center justify-between">
        <h1 class="text-3xl font-bold">${notice.title}</h1>
        <div class="text-sm text-gray-400">ID: ${notice.id} · ${notice.createdAt}</div>
    </div>

    <div class="p-6 rounded-lg bg-gray-900">
        <p>${notice.content}</p>
    </div>

    <div class="mt-6 flex gap-3">
        <a href="${ctx}/notice" class="px-4 py-2 rounded bg-gray-700 text-white">Back</a>
        <a href="${ctx}/notice/${notice.id}/edit" class="px-4 py-2 rounded bg-gray-700 text-white">Edit</a>
        <form action="${ctx}/notice/${notice.id}/delete" method="post" onsubmit="return confirm('Delete this announcement?');">
            <button type="submit" class="px-4 py-2 rounded bg-red-600 text-white">Delete</button>
        </form>
    </div>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />
