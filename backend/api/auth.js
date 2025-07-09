
document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("login-form");

  if (form) {
    form.addEventListener("submit", async function (e) {
      e.preventDefault();

      const email = document.getElementById("email").value;
      const senha = document.getElementById("senha").value;

      try {
        const response = await fetch("http://localhost:8000/api/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email: email, senha: senha }),
        });

        if (response.ok) {
          const data = await response.json();
          localStorage.setItem("token", data.token);
          window.location.href = "index.html";  // Redireciona após login bem-sucedido
        } else {
          const error = await response.json();
          alert("Erro: " + (error.detail || "Credenciais inválidas"));
        }
      } catch (err) {
        console.error("Erro na requisição:", err);
        alert("Erro ao conectar com o servidor.");
      }
    });
  }
});
