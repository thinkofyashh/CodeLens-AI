const API_URL = "http://127.0.0.1:8000/explain-code";

const form = document.querySelector("#explainForm");
const submitButton = document.querySelector("#submitButton");
const apiStatus = document.querySelector("#apiStatus");
const emptyState = document.querySelector("#emptyState");
const resultContent = document.querySelector("#resultContent");

const summary = document.querySelector("#summary");
const steps = document.querySelector("#steps");
const timeComplexity = document.querySelector("#timeComplexity");
const spaceComplexity = document.querySelector("#spaceComplexity");
const bugs = document.querySelector("#bugs");
const improvements = document.querySelector("#improvements");

function setStatus(message, type = "") {
  apiStatus.textContent = message;
  apiStatus.className = `status ${type}`.trim();
}

function setLoading(isLoading) {
  submitButton.disabled = isLoading;
  submitButton.textContent = isLoading ? "Explaining..." : "Explain Code";
}

function renderList(element, items, fallback) {
  element.innerHTML = "";
  const values = Array.isArray(items) && items.length > 0 ? items : [fallback];

  values.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    element.appendChild(li);
  });
}

function renderResult(data) {
  emptyState.classList.add("hidden");
  resultContent.classList.remove("hidden");

  summary.textContent = data.summary || "No summary returned.";
  timeComplexity.textContent = data.complexity?.time || "Not provided";
  spaceComplexity.textContent = data.complexity?.space || "Not provided";

  renderList(steps, data.step_by_step, "No step-by-step explanation returned.");
  renderList(bugs, data.bugs, "No obvious bugs found.");
  renderList(improvements, data.improvements, "No improvements suggested.");
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const formData = new FormData(form);
  const payload = {
    code: formData.get("code"),
    language: formData.get("language"),
    level: formData.get("level"),
  };

  setLoading(true);
  setStatus("Explaining...");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const errorText = await response.text();
      throw new Error(errorText || `Request failed with ${response.status}`);
    }

    const data = await response.json();
    renderResult(data);
    setStatus("Explanation ready", "success");
  } catch (error) {
    setStatus("Backend error", "error");
    emptyState.classList.remove("hidden");
    resultContent.classList.add("hidden");
    emptyState.textContent = "Could not get an explanation. Check that the backend is running.";
    console.error(error);
  } finally {
    setLoading(false);
  }
});
