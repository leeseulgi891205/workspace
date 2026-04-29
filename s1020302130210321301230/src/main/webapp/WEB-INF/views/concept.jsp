<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NEXT DEBUT - 콘셉트 설정</title>
    
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background: #050505;
        }
        
        .font-orbitron {
            font-family: 'Orbitron', sans-serif;
        }
        
        .gradient-text {
            background: linear-gradient(45deg, #00ffff, #ff00ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }
        
        .neon-text-cyan {
            color: #00ffff;
            text-shadow: 
                0 0 10px rgba(0, 255, 255, 0.8),
                0 0 20px rgba(0, 255, 255, 0.5);
        }
    </style>
</head>
<body class="min-h-screen bg-gradient-to-br from-purple-900 via-black to-blue-900 text-white flex items-center justify-center px-6">
    <div class="max-w-4xl mx-auto text-center">
        <h1 class="font-orbitron text-5xl md:text-6xl font-black gradient-text mb-8">
            <i class="fas fa-palette"></i> 콘셉트 설정
        </h1>
        
        <div class="bg-white/5 backdrop-blur-lg rounded-2xl p-8 mb-8 border border-cyan-500/20">
            <h2 class="font-orbitron text-3xl font-bold neon-text-cyan mb-6">
                선택된 연습생
            </h2>
            <div class="flex flex-wrap justify-center gap-4 mb-8">
                <c:forEach var="trainee" items="${selectedTrainees}">
                    <div class="bg-gradient-to-r from-cyan-500/20 to-pink-500/20 px-6 py-3 rounded-full border border-cyan-500/50">
                        <span class="font-bold text-xl"><i class="fas fa-star"></i> ${trainee}</span>
                    </div>
                </c:forEach>
            </div>
            
            <p class="text-gray-300 text-lg mb-6">
                축하합니다! 멋진 멤버들을 선택하셨네요. 🎉
            </p>
            
            <div class="text-yellow-300 text-xl font-bold">
                콘셉트 설정 기능은 준비 중입니다...
            </div>
        </div>
        
        <a href="/main" class="inline-block bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 px-8 py-4 rounded-full font-bold text-lg transition-all duration-300 shadow-lg hover:shadow-cyan-500/50">
            <i class="fas fa-arrow-left"></i> 메인으로 돌아가기
        </a>
    </div>
</body>
</html>
