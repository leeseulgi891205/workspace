<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />
<jsp:include page="/WEB-INF/views/include/header.jsp" />

<div class="container mx-auto px-6 mt-32">
    <h1 class="text-3xl font-bold mb-4">Bug / Report</h1>
    <p>Report bugs or issues here.</p>
</div>

<jsp:include page="/WEB-INF/views/include/footer.jsp" />