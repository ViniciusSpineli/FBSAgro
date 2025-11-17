function togglePassword() {
  const input = document.getElementById("senha");
  const type = input.getAttribute("type") === "password" ? "text" : "password";
  input.setAttribute("type", type);
}
