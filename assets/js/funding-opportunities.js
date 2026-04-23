(function () {
  'use strict';

  var list = document.getElementById('funding-list');
  var filterInput = document.getElementById('funding-filter');
  var sortSelect = document.getElementById('funding-sort');
  var emptyMsg = document.getElementById('funding-empty');
  if (!list || !filterInput || !sortSelect) return;

  var cards = Array.prototype.slice.call(list.querySelectorAll('.funding-card'));

  var FAR_FUTURE = 8640000000000000;

  function deadlineKey(card) {
    var raw = card.getAttribute('data-deadline-sort') || '';
    if (!raw) return FAR_FUTURE;
    var t = Date.parse(raw);
    return isNaN(t) ? FAR_FUTURE : t;
  }

  function amountKey(card) {
    var raw = card.getAttribute('data-amount-sort') || '';
    var n = parseFloat(raw);
    return isNaN(n) ? -1 : n;
  }

  function stringKey(card, attr) {
    return (card.getAttribute(attr) || '').toLowerCase();
  }

  var sorters = {
    'deadline-asc': function (a, b) { return deadlineKey(a) - deadlineKey(b); },
    'amount-desc': function (a, b) { return amountKey(b) - amountKey(a); },
    'funder-asc':  function (a, b) { return stringKey(a, 'data-funder').localeCompare(stringKey(b, 'data-funder')); },
    'title-asc':   function (a, b) { return stringKey(a, 'data-title').localeCompare(stringKey(b, 'data-title')); }
  };

  function applySort() {
    var sorter = sorters[sortSelect.value] || sorters['deadline-asc'];
    cards.slice().sort(sorter).forEach(function (card) { list.appendChild(card); });
  }

  function applyFilter() {
    var q = filterInput.value.trim().toLowerCase();
    var visible = 0;
    cards.forEach(function (card) {
      var match = !q || card.textContent.toLowerCase().indexOf(q) !== -1;
      card.style.display = match ? '' : 'none';
      if (match) visible++;
    });
    if (emptyMsg) emptyMsg.style.display = visible === 0 ? '' : 'none';
  }

  var filterTimer;
  filterInput.addEventListener('input', function () {
    clearTimeout(filterTimer);
    filterTimer = setTimeout(applyFilter, 120);
  });
  sortSelect.addEventListener('change', applySort);

  applySort();
  applyFilter();
})();
