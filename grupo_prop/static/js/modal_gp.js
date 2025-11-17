document.addEventListener("DOMContentLoaded", () => {

    const modal = document.getElementById("modal-gp-overlay");

    // Abrir o modal
    document.querySelectorAll("[data-gp='open-modal']").forEach(btn => {
        btn.addEventListener("click", () => {
            modal.classList.add("show");
            document.body.style.overflow = "hidden";
        });
    });

    // Fechar o modal (botão cancelar OU clique fora)
    document.querySelectorAll("[data-gp='close']").forEach(btn => {
        btn.addEventListener("click", () => {
            modal.classList.remove("show");
            document.body.style.overflow = "auto";
        });
    });

    // Fechar com ESC
    document.addEventListener("keydown", e => {
        if (e.key === "Escape") {
            modal.classList.remove("show");
            document.body.style.overflow = "auto";
        }
    });

});
