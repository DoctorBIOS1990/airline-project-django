// ScrollRelveal Effect Transition for Index page
ScrollReveal({
    reset: true,
    distance: '80px',
    duration: 2000,
    delay: 200
  });
  
  ScrollReveal().reveal('#block_about', { origin: 'left' });
  ScrollReveal().reveal('marquee', { origin: 'right' });
  ScrollReveal().reveal('#s1', { origin: 'top' });
  ScrollReveal().reveal('#s2', { origin: 'bottom' });
  ScrollReveal().reveal('#codewrite', { origin: 'left' });

  ScrollReveal().reveal('.contact-text h2, .contact-text h4, .contact-text p ', { origin: 'top' });
  ScrollReveal().reveal(' .contact-form', { origin: 'left' });
  ScrollReveal().reveal('.contact-text', { origin: 'left' });
  ScrollReveal().reveal('#indexCard', { origin: 'left' });
  ScrollReveal().reveal('#indexCard2', { origin: 'right' });