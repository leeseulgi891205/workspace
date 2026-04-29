<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pages - Login</title>
  <link href="https://fonts.googleapis.com/css?family=Noto+Sans+KR:400,500,700,900&display=swap&subset=korean" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/login.css">
</head>

<body>
  <header>
    <ul>
      <li>?뚯썝媛??/li> <span>|</span>
      <li>濡쒓렇??/li> <span>|</span>
      <li>怨좉컼?됰났?쇳꽣</li> <span>|</span>
      <li>諛곗넚吏?????/li> <span>|</span>
      <li>湲고봽?몄뭅???깅줉</li>
    </ul>
  </header>

  <nav>
    <div class="logo"></div>

    <div id="search">
      <div class="search"></div><br>
      <span>硫붾돱李얘린</span>
    </div>

    <div id="cart">
      <div class="cart"></div><br>
      <span>?λ컮援щ땲</span>
    </div>

    <div class="nav-menu">
      <ul>
        <li>COOKIT?뚭컻</li>
        <li>COOKIT 硫붾돱</li>
        <li>由щ럭</li>
        <li>?대깽??/li>
        <li>MY荑≫궥</li>
      </ul>  
    </div>
  </nav>

  <section>
    <h1>濡쒓렇??/h1>

    <article id="category">
      <ul>
        <li class="selected">?뚯썝 濡쒓렇??/li>
        <li>鍮꾪쉶??二쇰Ц議고쉶</li>
      </ul>  
    </article>

    <form action="/login" name="login" method="post">
      <div class="id">
        <input type="text" name="id" size="30" placeholder="CJ ONE ?듯빀?꾩씠??6~20??>
      </div>
      <div class="pw">
        <input type="text" name="pw" size="45" placeholder="鍮꾨?踰덊샇 ?곷Ц, ?뱀닔臾몄옄, ?レ옄?쇳빀 8~12??>
      </div>

      <div id="save">
        <div class="save"></div>
        <span>?꾩씠?????/span>
      </div>
  
      <div id="find">
        <span>?꾩씠??李얘린</span> <span class="separator">|</span> <span>鍮꾨?踰덊샇 李얘린</span>
      </div>

      <button type="submit">濡쒓렇??/button>
    </form>

    <ul class="login-icons">
      <li class="phone"></li>
      <li class="kakao"></li>
      <li class="naver"></li>
      <li class="facebook"></li>
    </ul>

    <div class="sign-up-info">
      <h3>CJ ONE ?듯빀?뚯썝???꾨땲?좉???</h3>
      <p>CJ ONE ?듯빀?뚯썝?쇰줈 媛?낇븯?쒕㈃ CJ?쒖씪?쒕떦???ㅼ뼇???쒕퉬??COOKIT, CJ THE MARKET, CJ?쒖씪?쒕떦 ?덊럹?댁?)瑜??댁슜?섏떎 ???덉뒿?덈떎.</p>
      <div class="sign-up">CJ ONE ?듯빀?뚯썝 ?좉퇋媛?낇븯湲?<div class="arrow">&emsp;</div></div>
    </div>
  </section>

  <footer>
    <div class="wrapper">
      <div class="footer-left">
        <div class="footer-logo"></div>
        <div class="copyright">짤 COOKIT ALL RIGHTS RESERVED</div>
      </div>
  
      <div class="footer-center">
        <ul class="footer-nav">
          <li class="first-list">?댁슜?쎄?</li>
          <li class="green">媛쒖씤?뺣낫泥섎━ 諛⑹묠</li>
          <li>踰뺤쟻怨좎?</li>
          <li>?ъ뾽?먯젙蹂??뺤씤</li>
        </ul>
  
        <ul class="footer-info">
          <li class="first-list">?⑥젣?댁젣?쇱젣??二?</li>
          <li>??쒖씠??: ?먭꼍??媛뺤떊???좏쁽??/li>
          <li>?ъ뾽?먮벑濡앸쾲??: 104-86-09535</li>
          <li class="first-list">二쇱냼 : ?쒖슱 以묎뎄 ?숉샇濡?330 CJ?쒖씪?쒕떦 ?쇳꽣 (?? 04560</li>
          <li>?듭떊?먮ℓ?낆떊怨?以묎뎄 ??07767??/li>
          <li class="first-list">媛쒖씤?뺣낫蹂댄샇梨낆엫??: 議곗쁺誘?/li>
          <li>?대찓??: cjon@cj.net</li>
          <li>?몄뒪?낆젣怨듭옄 : CJ?щ━釉뚮꽕?몄썚?ㅳ닚</li>
        </ul>
  
        <div id="check">怨좉컼?섏? ?덉쟾嫄곕옒瑜??꾪빐 ?꾧툑?깆쑝濡?寃곗젣??LG U+ ?꾩옄 寃곗젣??留ㅻℓ蹂댄샇(?먯뒪?щ줈) ?쒕퉬?ㅻ? ?댁슜?섏떎 ???덉뒿?덈떎. <span class="check">媛???ъ떎 ?뺤씤</span></div>
      </div>
  
      <div class="footer-right">
        <div id="shortcut">
          <span>CJ洹몃９怨꾩뿴??諛붾줈媛湲?/span>
          <div class="shortcut"></div>
        </div>
  
        <div class="call">怨좉컼?됰났?쇳꽣 1668-1920</div>
        <div class="inquery">1:1 臾몄쓽</div>
      </div>
  
    </div>
  </footer>
</body>
</html>
