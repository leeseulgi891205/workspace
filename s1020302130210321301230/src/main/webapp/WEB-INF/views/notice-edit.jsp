<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-4 md:px-6 mt-32 max-w-2xl">
    <h1 class="text-3xl font-bold mb-4">Edit Announcement</h1>
    <form action="${ctx}/notice/${notice.id}/edit" method="post" class="space-y-3">
        <input type="text" name="title" value="${notice.title}" class="w-full p-2 rounded bg-gray-900" required />
        <textarea name="content" rows="6" class="w-full p-2 rounded bg-gray-900" required>${notice.content}</textarea>
        <div class="flex gap-3">
            <button type="submit" class="px-4 py-2 rounded bg-gradient-to-r from-brand-cyan to-brand-pink text-white">Save</button>
            <a href="${ctx}/notice/${notice.id}" class="px-4 py-2 rounded bg-gray-700 text-white">Cancel</a>
        </div>
    </form>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />
