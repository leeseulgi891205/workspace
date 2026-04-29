<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-6 mt-32 max-w-md">
    <h1 class="text-2xl font-bold mb-4">Login</h1>
    <form action="${ctx}/login" method="post" class="space-y-3">
        <input type="text" name="username" placeholder="Username" class="w-full p-2 rounded bg-gray-900" required />
        <input type="password" name="password" placeholder="Password" class="w-full p-2 rounded bg-gray-900" required />
        <button type="submit" class="w-full py-2 rounded bg-gradient-to-r from-brand-cyan to-brand-pink text-white">Login</button>
    </form>
    <p class="mt-4 text-sm">No account? <a href="${ctx}/auth/register" class="text-brand-cyan">Register</a></p>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />