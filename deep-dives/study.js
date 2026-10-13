'use strict';
const Study = {
  queue(arrivals, fraction, reviewers, minutes) {
    if (![arrivals, fraction, reviewers, minutes].every(Number.isFinite) || arrivals < 0 || fraction < 0 || fraction > 100 || reviewers < 1 || !Number.isSafeInteger(reviewers) || minutes <= 0) return null;
    const demand = arrivals * (fraction / 100), capacity = reviewers * (60 / minutes);
    const utilization = demand / capacity;
    return [demand, capacity, utilization].every(Number.isFinite) && capacity > 0 ? {demand, capacity, utilization, backlog: Math.max(0, demand - capacity)} : null;
  },
  budget(total, target, bad) {
    if (![total, target, bad].every(Number.isFinite) || !Number.isSafeInteger(total) || !Number.isSafeInteger(bad) || total < 1 || bad < 0 || bad > total || target <= 0 || target >= 100) return null;
    const allowed = total * ((100 - target) / 100);
    return {allowed, remaining: allowed - bad, burn: bad / allowed, observed: 100 * (1 - bad / total)};
  },
  restore(raw, ids) {
    try { const data = JSON.parse(raw); return Array.isArray(data) && data.every(x => typeof x === 'string' && ids.includes(x)) ? [...new Set(data)] : []; }
    catch (_) { return []; }
  },
  answer(correct, selected) { return Number.isInteger(selected) && selected >= 0 && selected < 4 ? (correct === selected ? 'correct' : 'review') : 'unanswered'; }
};
if (typeof module !== 'undefined') module.exports = Study;
if (typeof document !== 'undefined') {
  const completions = [...document.querySelectorAll('[data-complete]')];
  const ids = completions.map(x => x.dataset.complete);
  const key = 'ccarp-deep-2026-10-13-' + document.body.dataset.domain;
  let storageOK = true, saved = [];
  try { saved = Study.restore(localStorage.getItem(key), ids); } catch (_) { storageOK = false; }
  const progress = document.getElementById('study-progress');
  const note = document.getElementById('save-note');
  function update() {
    if (progress) { const count = completions.filter(x => x.checked).length; progress.textContent = `${count} / ${ids.length} sections marked studied`; }
    if (note) note.textContent = storageOK ? 'Section marks stay in this browser. They are a study aid, not a competence score.' : 'Browser storage is unavailable. Marks last only while this page stays open.';
  }
  completions.forEach(input => {
    input.checked = saved.includes(input.dataset.complete);
    input.addEventListener('change', () => {
      try { localStorage.setItem(key, JSON.stringify(completions.filter(x => x.checked).map(x => x.dataset.complete))); } catch (_) { storageOK = false; }
      update();
    });
  });
  update();
  document.querySelectorAll('[data-check]').forEach(form => form.addEventListener('submit', event => {
    event.preventDefault();
    const selected = form.querySelector('input:checked');
    const verdict = Study.answer(Number(form.dataset.correct), selected ? Number(selected.value) : null);
    const status = form.querySelector('[role=status]');
    status.textContent = verdict === 'unanswered' ? 'Choose a response first.' : verdict === 'correct' ? 'Correct. Read the reasoning and why the alternatives fail.' : 'Review this decision. Compare the constraints in each explanation.';
    if (verdict !== 'unanswered') form.querySelector('details').open = true;
  }));
  document.querySelectorAll('[data-calc]').forEach(form => {
    const output = form.querySelector('output');
    function calculate() {
      const values = [...form.querySelectorAll('input')].map(x => x.value.trim() === '' ? NaN : Number(x.value));
      const result = Study[form.dataset.calc](...values);
      if (!result) { output.textContent = 'Enter valid values within the limits shown. Blank fields do not count as zero.'; return; }
      const n = x => x.toLocaleString(undefined, {maximumFractionDigits: 2});
      output.textContent = form.dataset.calc === 'queue'
        ? `${n(result.demand)} reviews/hour needed; ${n(result.capacity)} reviews/hour available. Utilization: ${n(result.utilization * 100)}%. Excess demand: ${n(result.backlog)} reviews/hour. ${result.utilization >= 1 ? 'No spare capacity: reduce intake or add approved capacity before promising a response time.' : 'Nominal capacity passes. Validate burst handling, reviewer availability and actual tail waiting time.'}`
        : `Allowed bad events: ${n(result.allowed)}. Remaining allowance: ${n(result.remaining)}. Budget consumed: ${n(result.burn * 100)}%. Observed good-event rate: ${n(result.observed)}%. ${result.remaining < -1e-9 ? 'Target missed in this window.' : 'Within this event budget; check every separate quality and safety gate.'}`;
    }
    form.addEventListener('input', calculate);
    form.addEventListener('submit', event => { event.preventDefault(); calculate(); });
    calculate();
  });
  const print = document.getElementById('print-page');
  if (print) print.addEventListener('click', () => window.print());
  let folded = [];
  window.addEventListener('beforeprint', () => { folded = [...document.querySelectorAll('details:not([open])')]; folded.forEach(x => x.open = true); });
  window.addEventListener('afterprint', () => { folded.forEach(x => x.open = false); folded = []; });
}
