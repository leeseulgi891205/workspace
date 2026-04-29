<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<c:set var="ctx" value="${pageContext.request.contextPath}" />

<!-- Inject main styles/resources so pages including header.jsp share the same look -->
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
    /* shared styles copied from main.jsp */
    .text-gradient-subtle {
        background: linear-gradient(to right, #ffffff 20%, #CFFFFE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 8px rgba(0, 229, 255, 0.3));
    }

    body {
        font-family: 'pretendard', sans-serif;
        background-color: #0B0B12;
        color: #ffffff;
        overflow-x: hidden;
    }

    .ambient-bg {
        position: fixed;
        top: 0; left: 0; width: 100vw; height: 100vh;
        z-index: -1;
        background: radial-gradient(circle at 15% 50%, rgba(0, 229, 255, 0.08), transparent 25%),
                    radial-gradient(circle at 85% 30%, rgba(255, 0, 127, 0.08), transparent 25%),
                    radial-gradient(circle at 50% 80%, rgba(112, 0, 255, 0.08), transparent 25%);
        filter: blur(60px);
        animation: ambientShift 10s ease-in-out infinite alternate;
    }

    @keyframes ambientShift {
        0% { transform: scale(1) translateY(0); }
        100% { transform: scale(1.1) translateY(-20px); }
    }

    .premium-glass {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
    }

    .text-gradient-primary {
        background: linear-gradient(135deg, #00E5FF, #FF007F);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .trainee-card { position: relative; transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); overflow: hidden; }
    .trainee-card::before { content: ''; position: absolute; top: 0; left: -100%; width: 50%; height: 100%; background: linear-gradient(to right, transparent, rgba(255,255,255,0.1), transparent); transform: skewX(-25deg); transition: all 0.6s ease; z-index: 10; }
    .trainee-card:hover { transform: translateY(-8px); box-shadow: 0 15px 40px -10px rgba(0, 229, 255, 0.3); border-color: rgba(0, 229, 255, 0.5); }
    .trainee-card:hover::before { left: 200%; }

    .img-overlay { background: linear-gradient(to bottom, transparent 40%, #0B0B12 100%); }

    .card-selected { border: 2px solid #FF007F !important; box-shadow: 0 0 30px rgba(255, 0, 127, 0.2), inset 0 0 20px rgba(255, 0, 127, 0.1) !important; }
    .card-selected .select-badge { opacity: 1; transform: scale(1); }
    .select-badge { opacity: 0; transform: scale(0.8); transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275); }

    .skill-bar { position: relative; overflow: hidden; }
    .skill-bar::after { content: ''; position: absolute; top: 0; left: 0; bottom: 0; right: 0; background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent); transform: translateX(-100%); animation: shimmer 2s infinite; }
    @keyframes shimmer { 100% { transform: translateX(100%); } }

    .bottom-bar { background: rgba(11, 11, 18, 0.85); backdrop-filter: blur(20px); border-top: 1px solid rgba(255, 255, 255, 0.05); }
</style>

<nav class="premium-glass fixed top-0 left-0 right-0 z-50">
    <div class="container mx-auto px-6 h-20 flex items-center justify-between">
        <a href="${ctx}/main" class="font-orbitron text-2xl font-black tracking-wider flex items-center gap-2 group">
            <i class="fas fa-play text-brand-cyan group-hover:text-brand-pink transition-colors"></i>
            <span>NEXT <span class="text-gradient-primary">DEBUT</span></span>
        </a>

        <!-- Desktop nav -->
        <ul class="hidden lg:flex items-center gap-8 font-medium text-sm tracking-wide">
            <li><a href="${ctx}/notice" class="text-gray-400 hover:text-white transition-colors"><i class="fas fa-bullhorn mr-2"></i>Announcements</a></li>
            <li><a href="${ctx}/guide" class="text-gray-400 hover:text-white transition-colors"><i class="fas fa-book mr-2"></i>Game Guide</a></li>
            <li><a href="${ctx}/board" class="text-gray-400 hover:text-white transition-colors"><i class="fas fa-users mr-2"></i>Community</a></li>
            <li><a href="${ctx}/report" class="text-gray-400 hover:text-white transition-colors"><i class="fas fa-bug mr-2"></i>Bug / Report</a></li>
        </ul>

        <!-- Mobile hamburger -->
        <div class="lg:hidden">
            <button id="nav-toggle" class="p-2 rounded-md bg-gray-800/40">
                <i class="fas fa-bars"></i>
            </button>
        </div>

        <div id="mobile-menu" class="hidden absolute right-6 top-20 bg-black/80 p-4 rounded-md shadow-md">
            <ul class="flex flex-col gap-3">
                <li><a href="${ctx}/notice" class="text-gray-200">Announcements</a></li>
                <li><a href="${ctx}/guide" class="text-gray-200">Game Guide</a></li>
                <li><a href="${ctx}/board" class="text-gray-200">Community</a></li>
                <li><a href="${ctx}/report" class="text-gray-200">Bug / Report</a></li>
            </ul>
        </div>
    </div>
</nav>

<script>
    document.addEventListener('click', function(e){
        const toggle = document.getElementById('nav-toggle');
        const menu = document.getElementById('mobile-menu');
        if(!toggle || !menu) return;
        if(e.target.closest('#nav-toggle')){
            menu.classList.toggle('hidden');
        } else if(!e.target.closest('#mobile-menu')){
            menu.classList.add('hidden');
        }
    });
</script>