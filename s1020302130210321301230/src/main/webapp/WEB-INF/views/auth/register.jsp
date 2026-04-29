<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-6 mt-32 max-w-md">
    <h1 class="text-2xl font-bold mb-4">Register</h1>
    <p>This demo does not implement real registration. Use username: <strong>user</strong> / password: <strong>password</strong> to log in.</p>
    <p class="mt-4"><a href="${ctx}/auth/login" class="text-brand-cyan">Back to Login</a></p>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />