/*document.addEventListener("DOMContentLoaded", function () {*/

const btnNovoGrupo = document.getElementById("btnNovoGrupo");
const btnCancelar = document.getElementById("btnCancelarModal");
const modalOverlay = document.getElementById("modal-overlay");

// Abrir modal
btnNovoGrupo.addEventListener("click", () => {
    modalOverlay.style.display = "flex";
});

// Fechar modal clicando no botão cancelar
btnCancelar.addEventListener("click", () => {
    modalOverlay.style.display = "none";
});

// Fechar modal clicando fora da caixa
modalOverlay.addEventListener("click", function (e) {
    if (e.target === modalOverlay) {
        modalOverlay.style.display = "none";
    }
});




/*});*/
