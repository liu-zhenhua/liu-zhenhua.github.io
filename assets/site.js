(() => {
  const controls = document.querySelector('.publication-tools');
  if (!controls) return;
  const buttons = [...document.querySelectorAll('[data-filter]')];
  const publications = [...document.querySelectorAll('.publication')];
  const search = document.querySelector('#publication-search');
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  let category = 'all';

  function filterPublications() {
    const terms = search.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    for (const paper of publications) {
      const matchesCategory = category === 'all' || paper.dataset.category === category;
      const haystack = paper.textContent.toLocaleLowerCase();
      paper.hidden = !(matchesCategory && terms.every(term => haystack.includes(term)));
      if (!paper.hidden) visible++;
    }
    count.textContent = `${visible} of ${publications.length} publications`;
    empty.hidden = visible !== 0;
    for (const button of buttons) {
      button.setAttribute('aria-pressed', String(button.dataset.filter === category));
    }
  }

  for (const button of buttons) {
    button.addEventListener('click', () => {
      category = button.dataset.filter;
      filterPublications();
    });
  }
  search.addEventListener('input', filterPublications);
  document.querySelector('#reset-filters').addEventListener('click', () => {
    category = 'all';
    search.value = '';
    filterPublications();
    search.focus();
  });
  controls.hidden = false;
  count.hidden = false;
  filterPublications();
})();
