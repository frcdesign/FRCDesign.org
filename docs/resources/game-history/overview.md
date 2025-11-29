---
title: Game History
description: An in-depth look at the history of FRC games.
---

# Game History

<div id="game-widget">
  <!-- Filters row -->
  <div id="game-filters">
    <input id="search" placeholder="Search...">

    <button id="year-sort" title="Toggle Year Order">
      <svg id="sort-arrow" width="30" height="30" viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg" fill="#4CAE4F">
        <path d="M14.83,9.5,12.69,6.38a.82.82,0,0,0-1.38,0L9.17,9.5A1,1,0,0,0,9.86,11H11v6a1,1,0,0,0,2,0V11h1.14A1,1,0,0,0,14.83,9.5Z"
              style="fill:#4CAE4F; transform: scale(2); transform-origin: center;"></path>
      </svg>
    </button>

    <button id="reset-filters" title="Reset Filters">
      <svg viewBox="0 0 21 21" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" focusable="false" role="img">
        <g transform="matrix(0 1 1 0 2.5 2.5)" fill="none" fill-rule="evenodd" stroke="#4CAE4F" stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5">
          <path d="m3.98652376 1.07807068c-2.38377179 1.38514556-3.98652376 3.96636605-3.98652376 6.92192932 0 4.418278 3.581722 8 8 8s8-3.581722 8-8-3.581722-8-8-8"></path>
          <path d="m4 1v4h-4" transform="matrix(1 0 0 -1 0 6)"></path>
        </g>
      </svg>
    </button>

    <label id="desc-toggle-label">
      <input type="checkbox" id="desc-toggle">
      Show Descriptions
    </label>
  </div>

  <!-- Game list -->
  <ul id="games-list"></ul>

  <!-- Pages -->
  <div id="pages"></div>
</div>

<script>
  function initGameWidget() {
    let games = [];
    let yearAscending = false;
    let currentPage = 1;

    const CARDS_PER_PAGE = 5;

    const searchInput = document.getElementById("search");
    const list = document.getElementById("games-list");
    const sortArrow = document.getElementById("sort-arrow");
    const yearSortButton = document.getElementById("year-sort");
    const resetButton = document.getElementById("reset-filters");
    const descToggleCheckbox = document.getElementById("desc-toggle");

    if (!searchInput) return;

    const typeButton = document.createElement('button');
    typeButton.textContent = "Filter by Type";
    typeButton.className = 'filter-btn';
    const typePopup = document.createElement('div');
    typePopup.className = 'filter-popup';
    typePopup.style.display = 'none';
    typeButton.appendChild(typePopup);

    const tagsButton = document.createElement('button');
    tagsButton.textContent = "Filter by Tags";
    tagsButton.className = 'filter-btn';
    const tagsPopup = document.createElement('div');
    tagsPopup.className = 'filter-popup';
    tagsPopup.style.display = 'none';
    tagsButton.appendChild(tagsPopup);

    const filtersContainer = document.getElementById("game-filters");
    filtersContainer.appendChild(typeButton);
    filtersContainer.appendChild(tagsButton);

    let showDescriptions = descToggleCheckbox.checked;

    descToggleCheckbox.addEventListener('change', () => {
      showDescriptions = descToggleCheckbox.checked;
      document.querySelectorAll('.card-desc').forEach(d => {
        d.style.display = showDescriptions ? 'block' : 'none';
      });
    });

    const resultsTitle = document.createElement("div");
    resultsTitle.id = "results-title";
    resultsTitle.style.margin = "8px 0";
    resultsTitle.style.fontWeight = "bold";
    resultsTitle.style.fontSize = "16px";

    const pages = document.getElementById("pages");
    pages.style.display = "flex";
    pages.style.justifyContent = "center";
    pages.style.alignItems = "center";
    pages.style.gap = "12px";
    pages.style.margin = "20px 0";

    const leftArrow = document.createElement("button");
    leftArrow.textContent = "←";
    leftArrow.className = "page-arrow";

    const pageInfo = document.createElement("span");
    pageInfo.id = "page-info";

    const rightArrow = document.createElement("button");
    rightArrow.textContent = "→";
    rightArrow.className = "page-arrow";

    pages.appendChild(leftArrow);
    pages.appendChild(pageInfo);
    pages.appendChild(rightArrow);

    let selectedTypes = new Set();
    let selectedTags = new Set();

    function getEra(year) {
      if (year >= 1992 && year <= 2002) return "1-foundational-era";
      if (year >= 2003 && year <= 2007) return "2-alliance-era";
      if (year >= 2008 && year <= 2015) return "3-control-era";
      if (year >= 2016 && year <= 2020) return "4-disney-era";
      return "5-modern-era";
    }

    function updateList() {
      const searchVal = searchInput.value.toLowerCase();

      const filtered = games.filter(g => {
        const matchesSearch =
          g.name.toLowerCase().includes(searchVal) ||
          g.type.join(" ").toLowerCase().includes(searchVal) ||
          g.tags.map(t => t.name).join(" ").toLowerCase().includes(searchVal) ||
          String(g.year).includes(searchVal);

        const matchesType = [...selectedTypes].every(t => g.type.includes(t));
        const matchesTags = [...selectedTags].every(tag => g.tags.some(t => t.name === tag));

        return matchesSearch && matchesType && matchesTags;
      });

      filtered.sort((a, b) => yearAscending ? a.year - b.year : b.year - a.year);

      resultsTitle.textContent = `${filtered.length} result${filtered.length !== 1 ? "s" : ""} match your filters`;

      const totalPages = Math.ceil(filtered.length / CARDS_PER_PAGE);
      if (currentPage > totalPages) currentPage = totalPages || 1;

      const start = (currentPage - 1) * CARDS_PER_PAGE;
      const end = start + CARDS_PER_PAGE;
      const visibleGames = filtered.slice(start, end);

      pageInfo.textContent = `Showing ${Math.min(end, filtered.length)} of ${filtered.length}`;

      leftArrow.disabled = currentPage === 1;
      rightArrow.disabled = currentPage === totalPages;

      list.innerHTML = "";
      visibleGames.forEach(g => {
        const era = getEra(g.year);
        const card = document.createElement("a");
        card.href = `/resources/game-history/${era}/${g.slug}/`;
        card.className = "game-card";

        const left = document.createElement("div");
        left.className = "card-left";
        left.textContent = g.year;

        const right = document.createElement("div");
        right.className = "card-right";

        const name = document.createElement("div");
        name.className = "card-name";
        name.textContent = g.name;

        const types = document.createElement("div");
        types.className = "card-types";
        types.textContent = `Type of game: ${g.type.join(", ")}`;

        const desc = document.createElement("div");
        desc.className = "card-desc";
        desc.textContent = g.desc;
        desc.style.display = showDescriptions ? 'block' : 'none';

        right.appendChild(name);
        right.appendChild(types);
        right.appendChild(desc);

        card.appendChild(left);
        card.appendChild(right);
        list.appendChild(card);
      });
    }

    function populateFilterPopup(popup, items, selectedSet, isTag = false) {
      popup.innerHTML = "";
      if (isTag) {
        const categoryOrder = ["game piece", "endgame", "field"];
        const grouped = {};
        items.forEach(t => {
          if (!grouped[t.type]) grouped[t.type] = [];
          grouped[t.type].push(t.name);
        });

        categoryOrder.forEach(cat => {
          if (!grouped[cat]) return;
          grouped[cat].sort().forEach(name => {
            const label = document.createElement("label");
            label.style.display = "flex";
            label.style.alignItems = "center";
            label.style.margin = "2px 0";

            const checkbox = document.createElement("input");
            checkbox.type = "checkbox";
            checkbox.value = name;
            checkbox.checked = selectedSet.has(name);
            checkbox.onchange = () => {
              if (checkbox.checked) selectedSet.add(name);
              else selectedSet.delete(name);
              updateList();
            };

            label.appendChild(checkbox);
            label.appendChild(document.createTextNode(name.charAt(0).toUpperCase() + name.slice(1)));
            popup.appendChild(label);
          });
        });
      } else {
        items.sort().forEach(name => {
          const label = document.createElement("label");
          label.style.display = "flex";
          label.style.alignItems = "center";
          label.style.margin = "2px 0";

          const checkbox = document.createElement("input");
          checkbox.type = "checkbox";
          checkbox.value = name;
          checkbox.checked = selectedSet.has(name);
          checkbox.onchange = () => {
            if (checkbox.checked) selectedSet.add(name);
            else selectedSet.delete(name);
            updateList();
          };

          label.appendChild(checkbox);
          label.appendChild(document.createTextNode(name.charAt(0).toUpperCase() + name.slice(1)));
          popup.appendChild(label);
        });
      }
    }

    function fetchAndInitFilters() {
      fetch("/resources/game-history/games.json")
        .then(r => r.json())
        .then(data => {
          games = data;

          const typeSet = new Set();
          const tagsArray = [];

          games.forEach(g => {
            g.type.forEach(t => typeSet.add(t));
            g.tags.forEach(tag => tagsArray.push(tag));
          });

          const uniqueTags = Array.from(
            new Map(tagsArray.map(tag => [`${tag.type}|${tag.name}`, tag])).values()
          );

          populateFilterPopup(typePopup, Array.from(typeSet), selectedTypes);
          populateFilterPopup(tagsPopup, uniqueTags, selectedTags, true);

          sortArrow.style.transform = yearAscending ? "rotate(0deg)" : "rotate(180deg)";
          updateList();
        });
    }

    fetchAndInitFilters();

    searchInput.addEventListener('input', updateList);

    yearSortButton.onclick = () => {
      yearAscending = !yearAscending;
      sortArrow.style.transform = yearAscending ? "rotate(0deg)" : "rotate(180deg)";
      updateList();
    };

    resetButton.onclick = () => {
      searchInput.value = "";
      selectedTypes.clear();
      selectedTags.clear();
      yearAscending = false;
      sortArrow.style.transform = "rotate(180deg)";

      const typeSet = new Set();
      const tagsArray = [];
      games.forEach(g => {
        g.type.forEach(t => typeSet.add(t));
        g.tags.forEach(tag => tagsArray.push(tag));
      });
      const uniqueTags = Array.from(
        new Map(tagsArray.map(tag => [`${tag.type}|${tag.name}`, tag])).values()
      );

      populateFilterPopup(typePopup, Array.from(typeSet), selectedTypes);
      populateFilterPopup(tagsPopup, uniqueTags, selectedTags, true);
      updateList();
    };

    function togglePopup(button, popup) {
      const isVisible = popup.style.display === 'flex';
      document.querySelectorAll('.filter-popup').forEach(p => p.style.display = 'none');

      if (!isVisible) {
        popup.style.display = 'flex';
        const rect = button.getBoundingClientRect();
        popup.style.top = `${rect.bottom + window.scrollY + 4}px`;
        popup.style.left = `${rect.left + window.scrollX}px`;
        popup.style.position = 'absolute';
        popup.style.flexDirection = 'column';
        popup.style.padding = '8px';
        popup.style.zIndex = 1000;
        popup.style.boxShadow = '0 4px 8px rgba(0,0,0,0.15)';
      }
    }

    typeButton.onclick = e => { e.stopPropagation(); togglePopup(typeButton, typePopup); };
    tagsButton.onclick = e => { e.stopPropagation(); togglePopup(tagsButton, tagsPopup); };

    document.addEventListener('click', e => {
      if (!e.target.closest('.filter-btn') && !e.target.closest('.filter-popup')) {
        document.querySelectorAll('.filter-popup').forEach(p => p.style.display = 'none');
      }
    });

    leftArrow.onclick = () => {
      if (currentPage > 1) {
        currentPage--;
        updateList();
      }
    };

    rightArrow.onclick = () => {
      currentPage++;
      updateList();
    };
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initGameWidget);
  } else {
    initGameWidget();
  }
</script>

<style>

  /* Filters row */
  #game-filters {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-bottom: 12px;
  }

  #year-sort,
  #reset-filters,
  #filter-type-btn,
  #filter-tags-btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 4px 8px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  #year-sort svg,
  #reset-filters svg {
    display: block;
    width: 24px;
    height: 24px;
    pointer-events: none;
  }

  #game-widget input#search {
    font-size: 16px;
    padding: 6px 12px;
    border: 1px solid #ccc;
    border-radius: 6px;
    outline: none;
    min-width: 200px;
    transition: border-color 0.2s, box-shadow 0.2s;
  }

  #game-widget input#search:focus {
    border-color: #4CAE4F;
    box-shadow: 0 0 4px rgba(76, 174, 79, 0.5);
  }

  #results-title {
    font-size: 16px;
    font-weight: bold;
    margin-bottom: 8px;
  }

  /* Game Cards */
  #games-list {
    list-style-type: none;
    padding-left: 0;
    margin-top: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .game-card {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 12px;
    border-radius: 8px;
    background-color: var(--card-bg, #fff);
    border: 1px solid var(--card-border, #ccc);
    box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), 
                box-shadow 0.2s, 
                color 0.2s;
    width: 100%;
    max-width: 800px;
    color: var(--card-text, #1F2129);
    text-decoration: none !important;
    cursor: pointer;
    margin-bottom: 4px;
    min-height: 60px;
  }

  /* Left side (year) */
  .game-card .card-left {
    flex: 0 0 80px;
    font-weight: bold;
    font-size: 22px;
    text-align: center;
    margin-right: 16px;
    color: #4CAE4F; 
  }

  /* Right side (info) */
  .game-card .card-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    overflow: hidden;
    color: var(--card-text, #1F2129);
  }

  .game-card .card-name {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: #4CAE4F;
  }

  .game-card .card-types {
    font-size: 15px;
    margin-top: 2px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    color: var(--card-text, #1F2129);
  }

  .game-card .card-desc {
    font-size: 13px;
    color: var(--card-text-secondary, #777); 
    line-height: 1.4;
    margin-top: 4px;
    overflow: hidden;
    text-overflow: ellipsis;
  }

  .game-card:hover {
    transform: translateY(-2px); 
    color: #4CAE4F;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15), 0 0 0 2px #4CAE4F; 
  }

  /* Filter Buttons */
  .filter-popup {
    position: absolute;
    background: var(--popup-bg, white);
    color: var(--popup-text, black);
    border: 1px solid var(--popup-border, #ccc);
    padding: 8px;
    border-radius: 6px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.2);
    z-index: 1000;
    display: flex;
    flex-wrap: wrap;
    max-width: 300px;
    max-height: 200px;
    gap: 6px;
  }

  .filter-popup label {
    display: flex;
    align-items: center;
    margin-right: 12px;
    margin-bottom: 6px;
    cursor: pointer;
    font-size: 14px;
  }

  .filter-popup input[type="checkbox"] {
    margin-right: 6px;
    accent-color: #4CAE4F; 
  }

  .filter-btn {
    padding: 6px 8px;
    border: 1px solid var(--filter-btn-border, #ccc);
    border-radius: 6px;
    background-color: var(--filter-btn-bg, #f0f0f0);
    color: var(--filter-btn-text, #1F2129);
    cursor: pointer;
    font-size: 14px;
    transition: background 0.2s, border 0.2s;
  }

  .filter-btn:hover {
    background-color: var(--filter-btn-hover-bg, #e0e0e0);
  }

  /* Description Toggle */
  #desc-toggle-label {
    display:inline-flex; 
    align-items:center; 
    gap:4px; 
    cursor:pointer;
  }

  #desc-toggle-label input[type="checkbox"] {
    accent-color: #4CAE4F; 
  }

  .page-arrow {
    padding: 6px 10px;
    background: none;
    border: 3px solid #4CAE4F;
    color: #4CAE4F;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: 0.2s;
  }

  .page-arrow:disabled {
    opacity: 0.3;
    cursor: not-allowed;
  }

  .page-arrow:hover:not(:disabled) {
    background: rgba(76,174,79,0.15);
  }

  /* Dark/light mode */
  [data-md-color-scheme="default"] .filter-btn {
    --filter-btn-bg: #f0f0f0;
    --filter-btn-text: #000;
    --filter-btn-border: #ccc;
    --filter-btn-hover-bg: #e0e0e0;
  }

  [data-md-color-scheme="slate"] .filter-btn {
    --filter-btn-bg: #1F2129;
    --filter-btn-text: #eee;
    --filter-btn-border: #555;
    --filter-btn-hover-bg: #3a3a3a;
  }

  [data-md-color-scheme="default"] .filter-popup {
    --popup-bg: white;
    --popup-text: black;
    --popup-border: #ccc;
  }

  [data-md-color-scheme="slate"] .filter-popup {
    --popup-bg: #1F2129;
    --popup-text: #eee;
    --popup-border: #555;
  }

  [data-md-color-scheme="slate"] .game-card {
    --card-bg: #1F2129;
    --card-border: #555;
    --card-text: #fff;
  }
</style>


<br>
this page:
I definitely want to add some sorting function (by year, by game type/piece, etc.) whether that be sorting or filtering the games

year pages:
Speaking of page content, I'm thinking every page would include a short game breakdown (field/game piece info, etc.), game links (game animation [if available], match video, game manual), a picture of a few good robots (to give an idea), a small strategical breakdown explaining what was good and why, and some important things to consider in terms of design, and any other special considerations (e.g. the importance of bins in 2015 probably?)