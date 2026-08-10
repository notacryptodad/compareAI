/* CompareAI viewer — static. Reads dist/data.json (produced by build_data.py) and
   renders the comparison. Never edited to change content; content lives in the YAML. */
'use strict';

const BADGE = {
  ga:'GA', preview:'Preview', limited:'Limited', documented:'Documented',
  partner:'Partner', oss:'OSS', none:'No', unknown:'·',
};

const state = { db:null, bucket:'b', query:'', diff:false, hideUnknown:false, providers:{} };

const $ = (s) => document.querySelector(s);

fetch('data.json')
  .then((r) => { if (!r.ok) throw new Error('data.json ' + r.status); return r.json(); })
  .then((db) => { state.db = db; init(); })
  .catch((e) => {
    $('#main').innerHTML =
      '<p class="empty">Could not load data.json (' + e.message +
      '). This viewer must be served over http (Cloudflare Pages, or a local static ' +
      'server) — opening index.html directly via file:// blocks fetch().</p>';
  });

function init() {
  const db = state.db;

  // Freshness banner.
  const counts = tally();
  $('#banner').innerHTML =
    '<b>Data as of ' + (db.data_as_of || 'n/a') + '.</b> ' +
    counts.verified + ' of ' + counts.total + ' cells verified (' +
    Math.round(100 * counts.verified / counts.total) + '%). ' +
    'GA/Preview mean the vendor stated the stage; <b>Documented</b> = verified fact, ' +
    'no stage claimed — not a synonym for GA.';

  // Bucket tabs.
  const tabs = $('#tabs');
  Object.entries(db.buckets).forEach(([k, b]) => {
    const btn = document.createElement('button');
    btn.textContent = k.toUpperCase() + '. ' + b.name;
    btn.setAttribute('role', 'tab');
    btn.onclick = () => { state.bucket = k; syncTabs(); render(); };
    btn.dataset.k = k;
    tabs.appendChild(btn);
  });

  // Provider picker — default all on.
  const picker = $('#picker');
  Object.entries(db.providers).forEach(([k, p]) => {
    state.providers[k] = true;
    const lab = document.createElement('label');
    const cb = document.createElement('input');
    cb.type = 'checkbox'; cb.checked = true;
    cb.onchange = () => { state.providers[k] = cb.checked; render(); };
    lab.appendChild(cb); lab.appendChild(document.createTextNode(p.short));
    picker.appendChild(lab);
  });

  // Legend.
  $('#legend').innerHTML = Object.entries(BADGE)
    .map(([k, v]) => '<span class="badge b-' + k + '">' + v + '</span> ' + k).join('');

  $('#search').oninput = (e) => { state.query = e.target.value.toLowerCase(); render(); };
  $('#diff').onchange = (e) => { state.diff = e.target.checked; render(); };
  $('#hideUnknown').onchange = (e) => { state.hideUnknown = e.target.checked; render(); };
  $('#dlgClose').onclick = () => $('#dlg').close();

  syncTabs();
  render();
}

function syncTabs() {
  document.querySelectorAll('#tabs button').forEach((b) =>
    b.setAttribute('aria-selected', b.dataset.k === state.bucket ? 'true' : 'false'));
}

function tally() {
  let total = 0, verified = 0;
  const db = state.db;
  Object.values(db.data).forEach((byBucket) =>
    Object.values(byBucket).forEach((bd) =>
      Object.values(bd.capabilities).forEach((c) => {
        total++; if (c.status !== 'unknown') verified++;
      })));
  return { total, verified };
}

function activeProviders() {
  return Object.keys(state.db.providers).filter((k) => state.providers[k]);
}

function cellOf(pkey, bucket, rowId) {
  const bd = state.db.data[pkey] && state.db.data[pkey][bucket];
  return bd ? bd.capabilities[rowId] : undefined;
}

function badge(cell) {
  const st = cell ? cell.status : 'unknown';
  if (!cell || st === 'unknown') return '<span class="badge b-unknown">·</span>';
  let html = '<span class="badge b-' + st + '">' + (BADGE[st] || st) + '</span>';
  if (cell.product) html += '<span class="prod">' + esc(cell.product) + '</span>';
  else if (Array.isArray(cell.value))
    html += '<span class="prod">' + esc(cell.value.slice(0, 3).join(', ')) +
            (cell.value.length > 3 ? ', +' + (cell.value.length - 3) : '') + '</span>';
  else if (cell.value != null && typeof cell.value !== 'object')
    html += '<span class="prod">' + esc(String(cell.value)) + '</span>';
  return html;
}

function render() {
  const db = state.db, bucket = state.bucket, provs = activeProviders();
  const main = $('#main');
  main.innerHTML = '';

  if (!provs.length) { main.innerHTML = '<p class="empty">Select at least one provider.</p>'; return; }

  // Products-compared line.
  const prods = provs.map((p) => {
    const bd = db.data[p] && db.data[p][bucket];
    return '<b>' + db.providers[p].short + ':</b> ' + esc((bd && bd.product) || '—');
  }).join(' · ');
  const qline = document.createElement('div');
  qline.className = 'qline';
  qline.innerHTML = '<b>' + db.buckets[bucket].question + '</b> &nbsp; ' + prods;
  main.appendChild(qline);

  let shownRows = 0;

  db.dimensions.forEach((dim) => {
    const rows = dim.rows.filter((r) => {
      if (!r.buckets.includes(bucket)) return false;
      if (state.query && !r.label.toLowerCase().includes(state.query) &&
          !(r.hint || '').toLowerCase().includes(state.query)) return false;
      const cells = provs.map((p) => cellOf(p, bucket, r.id));
      const anyData = cells.some((c) => c && c.status !== 'unknown');
      if (state.hideUnknown && !anyData) return false;
      if (state.diff) {
        const keys = cells.map((c) => (c ? c.status + '|' + (c.product || '') : '·'));
        if (new Set(keys).size <= 1) return false;
      }
      if (!state.query && !state.hideUnknown && cells.every((c) => c === undefined)) return false;
      return true;
    });
    if (!rows.length) return;

    const details = document.createElement('details');
    details.open = true;
    details.className = 'dim-section';
    const summary = document.createElement('summary');
    summary.className = 'dim';
    summary.textContent = dim.name;
    details.appendChild(summary);

    if (dim.reframe && dim.reframe[bucket]) {
      const rf = document.createElement('div'); rf.className = 'reframe';
      rf.textContent = dim.reframe[bucket].trim();
      details.appendChild(rf);
    }

    const t = document.createElement('table');
    let head = '<tr><th class="cap">Capability</th>';
    provs.forEach((p) => { head += '<th>' + db.providers[p].short + '</th>'; });
    head += '</tr>';
    let body = '';
    rows.forEach((r) => {
      shownRows++;
      body += '<tr><td class="cap">' + esc(r.label) + '</td>';
      provs.forEach((p) => {
        const cell = cellOf(p, bucket, r.id);
        body += '<td class="cell" data-p="' + p + '" data-r="' + r.id + '">' +
          badge(cell) + '</td>';
      });
      body += '</tr>';
    });
    t.innerHTML = head + body;
    t.querySelectorAll('td.cell').forEach((td) =>
      td.onclick = () => openCell(td.dataset.p, bucket, td.dataset.r, main));
    details.appendChild(t);
    main.appendChild(details);
  });

  if (!shownRows) main.insertAdjacentHTML('beforeend',
    '<p class="empty">No rows match the current filters.</p>');
  $('#foot-count').textContent =
    activeProviders().length + ' provider(s) · bucket ' + bucket.toUpperCase();
}

function openCell(pkey, bucket, rowId) {
  const db = state.db, cell = cellOf(pkey, bucket, rowId);
  const row = db.dimensions.flatMap((d) => d.rows).find((r) => r.id === rowId) || {};
  $('#dlgTitle').textContent = (db.providers[pkey].short) + ' — ' + (row.label || rowId);
  $('#dlgSub').textContent =
    (BADGE[cell.status] || cell.status) +
    (cell.product ? ' · ' + cell.product : '') +
    (cell.verified_on ? ' · verified ' + cell.verified_on : '');
  let b = '';
  if (cell.notes) b += '<div class="k">Notes</div><pre>' + esc(cell.notes.trim()) + '</pre>';
  if (Array.isArray(cell.value))
    b += '<div class="k">Value</div><pre>' + esc(cell.value.join(', ')) + '</pre>';
  if (cell.source) b += '<div class="k">Source</div><pre><a href="' + esc(cell.source) +
    '" target="_blank" rel="noopener">' + esc(cell.source) + '</a></pre>';
  if (!cell.notes && !cell.source)
    b += '<p class="empty">No notes or source recorded for this cell.</p>';
  b += '<div class="k" style="margin-top:16px"><a class="contribute" href="' +
    esc(contributeUrl(pkey, bucket, rowId)) +
    '" target="_blank" rel="noopener">&#9873; Report stale / Suggest update</a></div>';
  $('#dlgBody').innerHTML = b;
  $('#dlg').showModal();
}

const REPO_URL = 'https://github.com/notacryptodad/compareAI';

function contributeUrl(pkey, bucket, rowId) {
  const db = state.db;
  const cell = cellOf(pkey, bucket, rowId);
  const row = db.dimensions.flatMap((d) => d.rows).find((r) => r.id === rowId) || {};
  const provider = db.providers[pkey].short;
  const bucketName = db.buckets[bucket].name;
  const title = '[Data update] ' + provider + ' / bucket ' + bucket.toUpperCase() + ' / ' + (row.label || rowId);
  const status = cell ? cell.status : 'unknown';
  const verifiedOn = cell && cell.verified_on ? cell.verified_on : 'n/a';
  const source = cell && cell.source ? cell.source : 'none';
  const body = '## Current data\n\n' +
    '- **Provider:** ' + provider + '\n' +
    '- **Bucket:** ' + bucket.toUpperCase() + ' — ' + bucketName + '\n' +
    '- **Capability:** ' + (row.label || rowId) + '\n' +
    '- **Status:** ' + status + '\n' +
    '- **Verified on:** ' + verifiedOn + '\n' +
    '- **Source:** ' + source + '\n\n' +
    '## What\'s changed?\n\n' +
    '<!-- Paste a URL and quote from the vendor\'s documentation showing updated information -->\n\n' +
    '## Evidence\n\n' +
    '<!-- Screenshot or verbatim quote from the vendor page -->\n';
  return REPO_URL + '/issues/new?' +
    'title=' + encodeURIComponent(title) +
    '&body=' + encodeURIComponent(body) +
    '&labels=data-update';
}

function esc(s) {
  return String(s).replace(/[&<>"]/g, (c) =>
    ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;' }[c]));
}
