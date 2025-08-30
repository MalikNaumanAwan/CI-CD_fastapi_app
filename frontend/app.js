//const API = "http://localhost:8090/api/todos";
const API = "https://ci-cdfastapiapp-production.up.railway.app";
// Fetch and render todos
async function fetchTodos() {
  const res = await fetch(`${API}/api/todos/`);
  const data = await res.json();
  const list = document.getElementById("list");
  list.innerHTML = "";

  for (const t of data) {
    const li = document.createElement("li");
    li.className =
      "flex items-center justify-between bg-white rounded p-3 shadow";

    li.innerHTML = `
      <span class="${t.completed ? "line-through text-gray-400" : ""}">
        ${t.title}
      </span>
      <div class="space-x-2">
        <button data-id="${
          t.id
        }" class="done px-3 py-1 bg-green-600 text-white rounded">Done</button>
        <button data-id="${
          t.id
        }" class="del px-3 py-1 bg-red-600 text-white rounded">Delete</button>
      </div>
    `;

    list.appendChild(li);
  }

  attachEventListeners();
}

// Event bindings
function attachEventListeners() {
  document.querySelectorAll(".done").forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      const id = e.target.dataset.id;
      // match backend route
      await fetch(`${API}/api/todos/${id}/done`, {
        method: "POST",
      });
      fetchTodos();
    });
  });

  document.querySelectorAll(".del").forEach((btn) => {
    btn.addEventListener("click", async (e) => {
      const id = e.target.dataset.id;
      await fetch(`${API}/api/todos/${id}`, { method: "DELETE" });
      fetchTodos();
    });
  });
}

// Add new todo
document.getElementById("todo-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const input = document.getElementById("title");
  const title = input.value.trim();
  if (!title) return;

  await fetch(`${API}/api/todos/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });

  input.value = "";
  fetchTodos();
});

// Initial load
fetchTodos();
