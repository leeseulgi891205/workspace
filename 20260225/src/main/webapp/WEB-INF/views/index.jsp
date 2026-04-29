<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>

<c:url var="heroImg" value="/images/hero.png"/>
<c:url var="t1" value="/images/t1.png"/>
<c:url var="t2" value="/images/t2.png"/>
<c:url var="t3" value="/images/t3.png"/>

<!doctype html>
<html lang="ko">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <meta name="color-scheme" content="dark"/>
  <title>Idol Debut Simulation</title>
</head>

<body class="app-body">
  <%@ include file="common/header.jspf" %>

  <main id="main" class="main" tabindex="-1">
    <!-- HERO (Launcher / Stage) -->
    <section class="hero hero-launcher" style="--hero-url: url('${heroImg}');" aria-label="시네마틱 히어로">
      <div class="hero-stars" aria-hidden="true"></div>

      <div class="container py-5">
        <div class="row align-items-center g-4 g-lg-5">
          <div class="col-lg-7">
            <div id="heroCarousel" class="carousel slide hero-carousel reveal" data-bs-ride="carousel" aria-label="히어로 슬라이드">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="0" class="active" aria-current="true" aria-label="슬라이드 1"></button>
                <button type="button" data-bs-target="#heroCarousel" data-bs-slide-to="1" aria-label="슬라이드 2"></button>
              </div>

              <div class="carousel-inner">
                <div class="carousel-item active">
                  <div class="hero-copy">
                    <div class="hero-kicker">
                      <span class="kicker-chip">
                        <i class="bi bi-lightning-charge-fill me-1" aria-hidden="true"></i> S1 LIVE
                      </span>
                      <span class="kicker-muted">훈련 → 팬덤 성장 → 랭킹 경쟁 → 데뷔</span>
                    </div>

                    <h1 class="hero-title mt-3">
                      당신의 연습생을 <span class="neon-accent">데뷔</span>시키세요
                    </h1>

                    <p class="hero-sub mt-3">
                      사용자가 프로듀서가 되어 선택합니다. 선택은 곧 지표(팬·매출·인기)로 반영되고,
                      최종 데뷔 점수와 리포트로 결과가 공개됩니다.
                    </p>

                    <div class="d-flex flex-wrap gap-2 mt-4">
                      <a class="btn btn-neon btn-lg" href="<c:url value='/simulation'/>" aria-label="게임 시작으로 이동">
                        <i class="bi bi-play-fill me-1" aria-hidden="true"></i> 게임시작
                      </a>
                      <a class="btn btn-ghost btn-lg" href="<c:url value='/dashboard'/>" aria-label="내 그룹 대시보드로 이동">
                        <i class="bi bi-grid-1x2-fill me-1" aria-hidden="true"></i> 내 그룹
                      </a>
                    </div>

                    <div class="hero-mini mt-4">
                      <div class="mini-stat">
                        <span class="mini-label">현재 참가자</span>
                        <span class="mini-value"><span class="countup" data-to="128403">0</span>명 · 실시간 경쟁</span>
                      </div>
                      <div class="mini-stat">
                        <span class="mini-label">오늘 보상</span>
                        <span class="mini-value"><i class="bi bi-gift me-1" aria-hidden="true"></i> +50 Fans</span>
                      </div>
                    </div>
                  </div>
                </div>

                <div class="carousel-item">
                  <div class="hero-copy">
                    <div class="hero-kicker">
                      <span class="kicker-chip">
                        <i class="bi bi-broadcast-pin me-1" aria-hidden="true"></i> LIVE EVENT
                      </span>
                      <span class="kicker-muted">AI 팬 반응(템플릿) · 지표 변동</span>
                    </div>

                    <h2 class="hero-title mt-3">
                      <span class="neon-accent">RISE TO THE TOP</span>
                    </h2>

                    <p class="hero-sub mt-3">
                      콘셉트·예산·홍보 전략에 따라 팬덤 성장률이 변하고,
                      랭킹이 실시간으로 뒤집힙니다.
                    </p>

                    <div class="d-flex flex-wrap gap-2 mt-4">
                      <a class="btn btn-neon btn-lg" href="<c:url value='/ranking'/>" aria-label="랭킹으로 이동">
                        <i class="bi bi-trophy-fill me-1" aria-hidden="true"></i> 랭킹 보러가기
                      </a>
                      <a class="btn btn-ghost btn-lg" href="<c:url value='/reports'/>" aria-label="리포트로 이동">
                        <i class="bi bi-bar-chart-fill me-1" aria-hidden="true"></i> 리포트 보기
                      </a>
                    </div>

                    <div class="hero-mini mt-4">
                      <div class="mini-stat">
                        <span class="mini-label">서버 TOP</span>
                        <span class="mini-value">NEONLUX · <span class="countup" data-to="98120">0</span></span>
                      </div>
                      <div class="mini-stat">
                        <span class="mini-label">내 시즌</span>
                        <span class="mini-value">S1 Week 3</span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              <button class="carousel-control-prev" type="button" data-bs-target="#heroCarousel" data-bs-slide="prev" aria-label="이전 슬라이드">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#heroCarousel" data-bs-slide="next" aria-label="다음 슬라이드">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
              </button>
            </div>
          </div>

          <!-- HUD -->
          <div class="col-lg-5">
            <aside class="hud reveal" aria-label="라이브 상태 HUD">
              <div class="hud-header">
                <div class="hud-title">
                  <i class="bi bi-broadcast-pin me-2" aria-hidden="true"></i>
                  LIVE STATUS
                </div>
                <div class="hud-chip" aria-label="핑 상태">
                  <span class="dot" aria-hidden="true"></span> ONLINE
                </div>
              </div>

              <div class="hud-grid mt-3">
                <div class="hud-card">
                  <div class="hud-label">오늘 이벤트</div>
                  <div class="hud-value">더블 보컬 EXP</div>
                  <div class="hud-sub">24시간 한정 · 훈련 효율 +100%</div>
                </div>

                <div class="hud-card">
                  <div class="hud-label">서버 TOP</div>
                  <div class="hud-value">NEONLUX · <span class="countup" data-to="98120">0</span></div>
                  <div class="hud-sub">이번 시즌 최고 점수</div>
                </div>

                <div class="hud-card hud-wide">
                  <div class="hud-label">내 현재 시즌</div>
                  <div class="hud-value">S1 Week 3</div>
                  <div class="hud-sub">다음 주차: 오디션(/audition) 준비</div>

                  <a class="hud-link mt-2" href="<c:url value='/audition'/>" aria-label="오디션 페이지로 이동">
                    오디션 준비하기 <i class="bi bi-arrow-right" aria-hidden="true"></i>
                  </a>
                </div>
              </div>
            </aside>
          </div>
        </div>
      </div>
    </section>

    <!-- DAILY QUEST (center title + 2x2 style) -->
    <section class="section section-chapter container py-5" aria-label="오늘의 퀘스트">
      <div class="chapter-head reveal text-center">
        <div class="chapter-kicker">📋 DAILY QUEST 📋</div>
        <h2 class="chapter-title mt-2">오늘의 미션을 완료하고 보상을 받으세요!</h2>
        <p class="chapter-desc">진행도는 HUD처럼 부드럽게 반영됩니다.</p>
      </div>

      <div class="row g-3 g-lg-4 mt-4 justify-content-center">
        <div class="col-md-6 col-lg-5">
          <div class="glass-card quest-card quest-wide reveal" data-progress="75" tabindex="0" role="group" aria-label="보컬 트레이닝 퀘스트">
            <div class="quest-top">
              <div class="quest-icon"><i class="bi bi-mic-fill" aria-hidden="true"></i></div>
              <div class="quest-meta">
                <div class="quest-title">보컬 트레이닝 3회</div>
                <div class="quest-sub">보상: +200 EXP, +30 Fans</div>
              </div>
              <span class="quest-count">3/4 완료</span>
            </div>
            <div class="progress quest-progress" role="progressbar" aria-label="보컬 트레이닝 진행도" aria-valuemin="0" aria-valuemax="100" aria-valuenow="75">
              <div class="progress-bar" style="width: 0%"></div>
            </div>
            <div class="d-flex justify-content-end mt-3">
              <a class="btn btn-sm btn-quest" href="<c:url value='/simulation'/>" aria-label="보컬 트레이닝 하러가기">
                바로 수행 <i class="bi bi-chevron-right ms-1" aria-hidden="true"></i>
              </a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-5">
          <div class="glass-card quest-card quest-wide reveal" data-progress="50" tabindex="0" role="group" aria-label="댄스 연습 퀘스트">
            <div class="quest-top">
              <div class="quest-icon"><i class="bi bi-person-walking" aria-hidden="true"></i></div>
              <div class="quest-meta">
                <div class="quest-title">댄스 연습 5회</div>
                <div class="quest-sub">보상: +300 EXP, +50 Fans</div>
              </div>
              <span class="quest-count">2/5 완료</span>
            </div>
            <div class="progress quest-progress" role="progressbar" aria-label="댄스 연습 진행도" aria-valuemin="0" aria-valuemax="100" aria-valuenow="50">
              <div class="progress-bar" style="width: 0%"></div>
            </div>
            <div class="d-flex justify-content-end mt-3">
              <a class="btn btn-sm btn-quest" href="<c:url value='/simulation'/>" aria-label="댄스 연습 하러가기">
                바로 수행 <i class="bi bi-chevron-right ms-1" aria-hidden="true"></i>
              </a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-5">
          <div class="glass-card quest-card quest-wide reveal" data-progress="100" tabindex="0" role="group" aria-label="팬 사인회 참석 퀘스트">
            <div class="quest-top">
              <div class="quest-icon"><i class="bi bi-ticket-perforated-fill" aria-hidden="true"></i></div>
              <div class="quest-meta">
                <div class="quest-title">팬 사인회 참석</div>
                <div class="quest-sub">보상: +500 EXP, +100 Fans</div>
              </div>
              <span class="quest-count done"><i class="bi bi-check2-circle me-1" aria-hidden="true"></i>완료!</span>
            </div>
            <div class="progress quest-progress" role="progressbar" aria-label="팬 사인회 진행도" aria-valuemin="0" aria-valuemax="100" aria-valuenow="100">
              <div class="progress-bar" style="width: 0%"></div>
            </div>
            <div class="d-flex justify-content-end mt-3">
              <a class="btn btn-sm btn-quest" href="<c:url value='/projects'/>" aria-label="팬덤 관련 프로젝트로 이동">
                보상 수령 <i class="bi bi-chevron-right ms-1" aria-hidden="true"></i>
              </a>
            </div>
          </div>
        </div>

        <div class="col-md-6 col-lg-5">
          <div class="glass-card quest-card quest-wide reveal" data-progress="15" tabindex="0" role="group" aria-label="뮤직비디오 촬영 퀘스트">
            <div class="quest-top">
              <div class="quest-icon"><i class="bi bi-camera-reels-fill" aria-hidden="true"></i></div>
              <div class="quest-meta">
                <div class="quest-title">뮤직비디오 촬영</div>
                <div class="quest-sub">보상: +800 EXP, +200 Fans</div>
              </div>
              <span class="quest-count">0/1 완료</span>
            </div>
            <div class="progress quest-progress" role="progressbar" aria-label="뮤직비디오 촬영 진행도" aria-valuemin="0" aria-valuemax="100" aria-valuenow="15">
              <div class="progress-bar" style="width: 0%"></div>
            </div>
            <div class="d-flex justify-content-end mt-3">
              <a class="btn btn-sm btn-quest" href="<c:url value='/projects'/>" aria-label="뮤직비디오 프로젝트로 이동">
                바로 수행 <i class="bi bi-chevron-right ms-1" aria-hidden="true"></i>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="text-center mt-4">
        <a class="btn btn-ghost btn-lg" href="<c:url value='/reports'/>" aria-label="게임 가이드 또는 리포트로 이동">
          게임 가이드 보기 <i class="bi bi-arrow-right ms-1" aria-hidden="true"></i>
        </a>
      </div>
    </section>

    <!-- CORE SYSTEM (neon icon tiles like screenshot) -->
    <section class="section section-chapter container py-5" aria-label="게임 시스템">
      <div class="chapter-head reveal text-center">
        <div class="chapter-kicker">⚡ CORE SYSTEM ⚡</div>
        <h2 class="chapter-title mt-2">아이돌 육성의 핵심 시스템을 탐험하세요</h2>
        <p class="chapter-desc">각 시스템은 바로 플레이/대시보드/랭킹으로 연결됩니다.</p>
      </div>

      <div class="row g-3 g-lg-4 mt-4">
        <div class="col-6 col-lg-3">
          <a class="neon-tile reveal" href="<c:url value='/simulation'/>" aria-label="Training 바로가기">
            <div class="tile-ico"><i class="bi bi-mic-fill" aria-hidden="true"></i></div>
            <div class="tile-title">Training</div>
            <div class="tile-desc">보컬·댄스·비주얼 능력치를 강화</div>
          </a>
        </div>
        <div class="col-6 col-lg-3">
          <a class="neon-tile reveal" href="<c:url value='/dashboard'/>" aria-label="Schedule 바로가기">
            <div class="tile-ico"><i class="bi bi-calendar2-week-fill" aria-hidden="true"></i></div>
            <div class="tile-title">Schedule</div>
            <div class="tile-desc">방송·팬미팅·콘서트 일정 관리</div>
          </a>
        </div>
        <div class="col-6 col-lg-3">
          <a class="neon-tile reveal" href="<c:url value='/reports'/>" aria-label="Fandom 바로가기">
            <div class="tile-ico"><i class="bi bi-heart-fill" aria-hidden="true"></i></div>
            <div class="tile-title">Fandom</div>
            <div class="tile-desc">팬덤 성장과 반응(댓글/지표)</div>
          </a>
        </div>
        <div class="col-6 col-lg-3">
          <a class="neon-tile reveal" href="<c:url value='/ranking'/>" aria-label="Ranking 바로가기">
            <div class="tile-ico"><i class="bi bi-trophy-fill" aria-hidden="true"></i></div>
            <div class="tile-title">Ranking</div>
            <div class="tile-desc">글로벌 랭킹에서 정상에 도전</div>
          </a>
        </div>
      </div>
    </section>

    <!-- HALL OF FAME (Top 3) -->
    <section class="section section-chapter container py-5" aria-label="이번 시즌 TOP 3 연습생">
      <div class="chapter-head reveal text-center">
        <div class="chapter-kicker">🏅 HALL OF FAME 🏅</div>
        <h2 class="chapter-title mt-2">이번 시즌 TOP 3 연습생</h2>
        <p class="chapter-desc">“랭킹 전체 보기”에서 더 많은 연습생을 확인하세요.</p>
      </div>

      <div class="row g-3 g-lg-4 mt-4 justify-content-center">
        <div class="col-md-4">
          <article class="hof-card reveal" aria-label="1위 연습생">
            <img class="hof-img" src="${t1}" alt="1위 연습생 프로필 이미지" loading="lazy">
            <div class="hof-rank">🥇 1위</div>
            <div class="hof-name">★하늘★</div>
            <div class="hof-sub">NEON UNIT · <span class="countup" data-to="98120">0</span> pts</div>
          </article>
        </div>

        <div class="col-md-4">
          <article class="hof-card reveal" aria-label="2위 연습생">
            <img class="hof-img" src="${t2}" alt="2위 연습생 프로필 이미지" loading="lazy">
            <div class="hof-rank">🥈 2위</div>
            <div class="hof-name">루나</div>
            <div class="hof-sub">CYAN LINE · <span class="countup" data-to="92740">0</span> pts</div>
          </article>
        </div>

        <div class="col-md-4">
          <article class="hof-card reveal" aria-label="3위 연습생">
            <img class="hof-img" src="${t3}" alt="3위 연습생 프로필 이미지" loading="lazy">
            <div class="hof-rank">🥉 3위</div>
            <div class="hof-name">소라</div>
            <div class="hof-sub">PINK WAVE · <span class="countup" data-to="88910">0</span> pts</div>
          </article>
        </div>
      </div>

      <div class="text-center mt-4">
        <a class="btn btn-neon btn-lg" href="<c:url value='/ranking'/>" aria-label="랭킹 전체 보기">
          랭킹 전체 보기 <i class="bi bi-arrow-right ms-1" aria-hidden="true"></i>
        </a>
      </div>
    </section>
  </main>

  <%@ include file="common/footer.jspf" %>
</body>
</html>
