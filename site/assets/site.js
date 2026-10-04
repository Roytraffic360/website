// Mobile menu and work filter. No tracking, no dependencies.
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var chips = document.querySelectorAll('[data-filter]');
  var cases = document.querySelectorAll('[data-service]');
  chips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      var f = chip.getAttribute('data-filter');
      chips.forEach(function (c) { c.setAttribute('aria-pressed', c === chip ? 'true' : 'false'); });
      cases.forEach(function (el) {
        var show = f === 'all' || el.getAttribute('data-service').split(' ').indexOf(f) !== -1;
        el.hidden = !show;
      });
    });
  });
})();
