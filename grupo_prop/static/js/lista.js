// --- 1. LÓGICA DO MODAL DE ADIÇÃO (EXISTENTE) ---

var btnNovoGrupo = document.getElementById("btnNovoGrupo");
var btnCancelar = document.getElementById("btnCancelarModal");
var modalOverlay = document.getElementById("modal-overlay");

// Verificar se os elementos do modal existem
if (btnNovoGrupo && btnCancelar && modalOverlay) {
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
        // Verifica se o clique foi diretamente no overlay (e não dentro do modal)
        if (e.target === modalOverlay) {
            modalOverlay.style.display = "none";
        }
    });
}

// --- 2. LÓGICA DE EXCLUSÃO (NOVA) ---

// 2.1. Encontra todos os botões de exclusão
var deleteButtons = document.querySelectorAll('.botao_excluir');

// 2.2. Obtém a URL base de exclusão definida no HTML
var deleteUrlBase = window.DELETE_URL_BASE;

if (deleteButtons.length > 0 && deleteUrlBase) {
    // 2.3. Adiciona um event listener para cada botão de exclusão
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault(); // Impede a ação padrão do botão (se houver)
            
            // Pega o ID (código) do item do atributo data-id
            var grupoId = this.getAttribute('data-id');

            if (grupoId) {
                // Solicita confirmação ao usuário
                var confirmacao = confirm(`Tem certeza que deseja excluir o Grupo de Propriedade Código ${grupoId}? Esta ação é irreversível.`);
                
                if (confirmacao) {
                    // Constrói a URL de exclusão
                    // Exemplo: /excluir-grupo/123/
                    //var finalUrl = deleteUrlBase.replace(/\/$/, '') + grupoId + '/';
                    var finalUrl = deleteUrlBase + grupoId + '/';

                    // Redireciona para a URL de exclusão
                    window.location.href = finalUrl;
                }
            }
        });
    });
}
/*});*/
