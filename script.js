// ---------- SLIDER ----------
const lengthSlider = document.getElementById("length");
const lengthValue = document.getElementById("lengthValue");

// Display slider value
function updateLengthValue() {
  lengthValue.textContent = lengthSlider.value;
}

// Initial display
updateLengthValue();

// Update on move
lengthSlider.addEventListener("input", updateLengthValue);

// ---------- PASSWORD STRENGTH ----------
const passwordInput = document.getElementById("passwordInput");
const strengthText = document.getElementById("strengthText");
const strengthBar = document.getElementById("strengthBar");

passwordInput.addEventListener("input", () => {
  const pwd = passwordInput.value;
  let score = 0;

  if (pwd.length >= 8) score++;
  if (/[A-Z]/.test(pwd)) score++;
  if (/[a-z]/.test(pwd)) score++;
  if (/[0-9]/.test(pwd)) score++;
  if (/[^A-Za-z0-9]/.test(pwd)) score++;

  const levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"];
  const colors = ["red", "orange", "yellow", "lightgreen", "green"];

  strengthText.textContent = pwd ? levels[score - 1] || "Very Weak" : "";
  strengthBar.style.width = score * 20 + "%";
  strengthBar.style.background = colors[score - 1] || "red";
});

// ---------- PASSWORD GENERATOR ----------
function generate() {
  const length = parseInt(lengthSlider.value);
  const upper = document.getElementById("upper").checked;
  const lower = document.getElementById("lower").checked;
  const number = document.getElementById("number").checked;
  const symbol = document.getElementById("symbol").checked;

  let chars = "";
  if (upper) chars += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  if (lower) chars += "abcdefghijklmnopqrstuvwxyz";
  if (number) chars += "0123456789";
  if (symbol) chars += "!@#$%^&*()_+";

  if (!chars) {
    alert("Select at least one option!");
    return;
  }

  let password = "";
  for (let i = 0; i < length; i++) {
    password += chars[Math.floor(Math.random() * chars.length)];
  }

  document.getElementById("generatedPassword").value = password;
}

// ---------- PWA ----------
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js");
}
