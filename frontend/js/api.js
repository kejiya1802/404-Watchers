const API_BASE_URL = "http://127.0.0.1:5000/api";
async function getCompetitors() {
    const response = await fetch(`${API_BASE_URL}/competitors`);

    if (!response.ok) {
        throw new Error("Failed to fetch competitors");
    }

    return await response.json();
}
async function runWatcher() {
    const response = await fetch(`${API_BASE_URL}/monitor/run`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        }
    });

    if (!response.ok) {
        throw new Error("Watcher failed");
    }

    return await response.json();
}
async function getChanges() {
    const response = await fetch(`${API_BASE_URL}/changes`);

    if (!response.ok) {
        throw new Error("Failed to fetch changes");
    }

    return await response.json();
}