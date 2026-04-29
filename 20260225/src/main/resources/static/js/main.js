(() => {
  const prefersReduced = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // -------- Reveal on scroll (lightweight) --------
  const revealEls = Array.from(document.querySelectorAll('.reveal'));

  const makeVisible = (el) => el.classList.add('is-visible');

  if (prefersReduced || !('IntersectionObserver' in window)) {
    revealEls.forEach(makeVisible);
  } else {
    const io = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          makeVisible(e.target);
          io.unobserve(e.target);
        }
      }
    }, { threshold: 0.12 });

    revealEls.forEach(el => io.observe(el));
  }

  // -------- Progress bars (quests) --------
  const questCards = Array.from(document.querySelectorAll('.quest-card'));
  const animateProgress = (card) => {
    const p = Math.max(0, Math.min(100, Number(card.dataset.progress || 0)));
    const bar = card.querySelector('.progress-bar');
    const wrap = card.querySelector('[role="progressbar"]');

    if (wrap) wrap.setAttribute('aria-valuenow', String(p));
    if (!bar) return;

    if (prefersReduced) {
      bar.style.width = `${p}%`;
      return;
    }

    // animate width using rAF (no heavy timers)
    bar.style.width = '0%';
    const start = performance.now();
    const dur = 520;

    const step = (t) => {
      const k = Math.min(1, (t - start) / dur);
      const eased = 1 - Math.pow(1 - k, 3); // easeOutCubic
      bar.style.width = `${(p * eased).toFixed(2)}%`;
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  // start when visible to avoid work on mobile
  if (prefersReduced || !('IntersectionObserver' in window)) {
    questCards.forEach(animateProgress);
  } else {
    const qio = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          animateProgress(e.target);
          qio.unobserve(e.target);
        }
      }
    }, { threshold: 0.2 });
    questCards.forEach(el => qio.observe(el));
  }

  // -------- Count up numbers (HUD + mini stats + TOP3) --------
  const countEls = Array.from(document.querySelectorAll('.countup'));
  const formatNumber = (n) => n.toLocaleString('ko-KR');

  const runCount = (el) => {
    const to = Number(el.dataset.to || 0);
    const from = 0;

    if (prefersReduced) {
      el.textContent = formatNumber(to);
      return;
    }

    const start = performance.now();
    const dur = 720;

    const step = (t) => {
      const k = Math.min(1, (t - start) / dur);
      const eased = 1 - Math.pow(1 - k, 3);
      const val = Math.round(from + (to - from) * eased);
      el.textContent = formatNumber(val);
      if (k < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };

  if (prefersReduced || !('IntersectionObserver' in window)) {
    countEls.forEach(runCount);
  } else {
    const cio = new IntersectionObserver((entries) => {
      for (const e of entries) {
        if (e.isIntersecting) {
          runCount(e.target);
          cio.unobserve(e.target);
        }
      }
    }, { threshold: 0.18 });
    countEls.forEach(el => cio.observe(el));
  }
})();
