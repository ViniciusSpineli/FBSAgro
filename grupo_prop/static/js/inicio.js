const sidebar = document.getElementById('sidebar');

function toggleSidebar() {
  sidebar.classList.toggle('collapsed');
}

function toggleSub(id) {
  const sub = document.getElementById(id);
  if (!sub) return; // evita erro em páginas que não têm o submenu

  const isOpen = sub.style.display === 'flex';

  if (isOpen) {
    sub.style.display = 'none';
  } else {
    sub.style.display = 'flex';
    sub.style.flexDirection = 'column';
  }
}

function showScreen(name) {
  const screen = document.getElementById('screen');
  const title = document.getElementById('screen-title');

  // TELA DE LISTA (carregada via fetch)
  if (name === 'prod-list') {
    title.textContent = 'Grupo de Propriedade';

    fetch('/produtos/')
      .then(r => r.text())
      .then(html => {
        screen.innerHTML = html;

        // Executar scripts que vierem no HTML carregado
        const scripts = screen.querySelectorAll("script");

        scripts.forEach(oldScript => {
          const newScript = document.createElement("script");

          if (oldScript.src) {
            // se for arquivo externo (ex: modal_gp.js)
            newScript.src = oldScript.src;
          } else {
            // se for script inline
            newScript.innerHTML = oldScript.innerHTML;
          }

          newScript.defer = true;
          oldScript.remove();
          screen.appendChild(newScript);
        });

      })
      .catch(err => {
        console.error('Erro ao carregar produtos:', err);
        screen.innerHTML = '<p>Erro ao carregar produtos.</p>';
      });

    return;
  }

  // OUTRAS TELAS (simples)
  const screens = {
    'home': { title: 'Início', html: `<h3>Início</h3><p>Conteúdo da tela inicial.</p>` },
    'prod-create': { title: 'Criar Produto', html: `<h3>Criar Produto</h3><p>Formulário de criação.</p>` },
    'prod-cats': { title: 'Categorias', html: `<h3>Categorias</h3><p>Gerencie categorias aqui.</p>` },
    'profile': { title: 'Perfil', html: `<h3>Perfil</h3><p>Dados do usuário.</p>` },
    'prefs': { title: 'Preferências', html: `<h3>Preferências</h3><p>Ajustes do sistema.</p>` },
    'reports': { title: 'Relatórios', html: `<h3>Relatórios</h3><p>Visões e gráficos (placeholder).</p>` }
  };

  const s = screens[name] || { title: 'Tela', html: `<h3>${name}</h3><p>Conteúdo padrão.</p>` };
  title.textContent = s.title;
  screen.innerHTML = s.html;

  if (window.innerWidth < 800) {
    sidebar.classList.add('collapsed');
  }
}

window.addEventListener('keydown', e => {
  if (e.key.toLowerCase() === 'm') {
    toggleSidebar();
  }
});
