let reps = 0;
setInterval(async () => {
    const res = await fetch('/api/status');
    const data = await res.json();
    document.getElementById('rep-count').innerText = data.pushups;
    document.getElementById('status-overlay').innerText = data.status;
}, 500);

document.getElementById('start-btn').onclick = () => {
    fetch('/api/start', { method: 'POST' });
};