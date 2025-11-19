const sidebar = document.getElementById('sidebar'); // captura a sidebar pelo ID

function toggleSidebar() {
  sidebar.classList.toggle('collapsed'); // alterna a classe 'collapsed' para abrir/fechar a sidebar
}

function toggleSub(id) {
  const sub = document.getElementById(id); // seleciona o submenu pelo ID
  if (!sub) return; // evita erro caso o submenu não exista na página

  const isOpen = sub.style.display === 'flex'; // verifica se o submenu já está aberto

  if (isOpen) {
    sub.style.display = 'none'; // fecha o submenu
  } else {
    sub.style.display = 'flex'; // abre o submenu
    sub.style.flexDirection = 'column'; // garante layout em coluna
  }
}

function showScreen(name) {
  const screen = document.getElementById('screen'); // área onde o conteúdo será exibido
  const title = document.getElementById('screen-title'); // título da área de conteúdo
  
  // --- CARREGAMENTO DINÂMICO DA LISTA VIA FETCH ---
  if (name === 'prod-list') {
    title.textContent = 'Grupo de Propriedade'; // altera título da tela
    
    fetch('/produtos/') // chama a URL para carregar a lista
      
      

      .then(r => r.text()) // converte resposta para texto/HTML
      .then(html => {
        screen.innerHTML = html; // injeta HTML carregado via fetch

        const scripts = screen.querySelectorAll("script"); // pega scripts contidos no HTML injetado

        scripts.forEach(oldScript => {
          const newScript = document.createElement("script"); // cria nova tag script

          if (oldScript.src) {
            newScript.src = oldScript.src; // se for arquivo externo (ex: modal_gp.js)
          } else {
            newScript.innerHTML = oldScript.innerHTML; // se for script inline
          }

          newScript.defer = true; // executa script após carregar HTML
          oldScript.remove(); // remove o script antigo para evitar duplicação
          screen.appendChild(newScript); // adiciona script novo e funcional ao DOM
        });

      })
      .catch(err => {
        console.error('Erro ao carregar produtos:', err); // exibe erro no console
        screen.innerHTML = '<p>Erro ao carregar produtos.</p>'; // feedback visual
      });

    return; // encerra função para não executar o restante
  }

  // --- OUTRAS TELAS SIMPLES (SEM FETCH) ---
  const screens = {
    'home': { title: 'Início', html: `<h3>Início</h3><p>Conteúdo da tela inicial.</p>` },
    'prod-create': { title: 'Criar Produto', html: `<h3>Criar Produto</h3><p>Formulário de criação.</p>` },
    'prod-cats': { title: 'Categorias', html: `<h3>Categorias</h3><p>Gerencie categorias aqui.</p>` },
    'profile': { title: 'Perfil', html: `<h3>Perfil</h3><p>Dados do usuário.</p>` },
    'prefs': { title: 'Preferências', html: `<h3>Preferências</h3><p>Ajustes do sistema.</p>` },
    'reports': { title: 'Relatórios', html: `<h3>Relatórios</h3><p>Visões e gráficos (placeholder).</p>` }
  };

  const s = screens[name] || { title: 'Tela', html: `<h3>${name}</h3><p>Conteúdo padrão.</p>` }; // fallback caso a tela não exista
  title.textContent = s.title; // altera o título da tela
  screen.innerHTML = s.html; // insere o conteúdo correspondente

  if (window.innerWidth < 800) {
    sidebar.classList.add('collapsed'); // fecha sidebar automaticamente em telas pequenas
  }
}

// --- ATALHO DE TECLADO (TECLA M) ---
/*window.addEventListener('keydown', e => {
  if (e.key.toLowerCase() === 'm') { // se pressionar "M"
    toggleSidebar(); // abre/fecha menu lateral
  }
});*/
