const sidebar = document.getElementById('sidebar');

function toggleSidebar(){
  sidebar.classList.toggle('collapsed');
}

function toggleSub(id){
  const sub = document.getElementById(id);
  const toggle = document.getElementById(id + '-toggle');
  const isOpen = sub.style.display === 'flex';

  if(isOpen){
    sub.style.display = 'none';
    toggle.classList.remove('open');
  }else{
    sub.style.display = 'flex';
    sub.style.flexDirection = 'column';
    toggle.classList.add('open');
  }
}

function showScreen(name){
  const screen = document.getElementById('screen');
  const title = document.getElementById('screen-title');

  if(name === 'prod-list'){
    title.textContent = 'Grupo de Propriedade';
    fetch('/produtos/')
      .then(r => r.text())
      .then(html => { screen.innerHTML = html; })
      .catch(err => {
        console.error('Erro ao carregar produtos:', err);
        screen.innerHTML = '<p>Erro ao carregar produtos.</p>';
      });
    return;
  }

  const screens = {
    'home': {title:'Início', html:`<h3>Início</h3><p>Conteúdo da tela inicial.</p>`},
    'prod-create': {title:'Criar Produto', html:`<h3>Criar Produto</h3><p>Formulário de criação.</p>`},
    'prod-cats': {title:'Categorias', html:`<h3>Categorias</h3><p>Gerencie categorias aqui.</p>`},
    'profile': {title:'Perfil', html:`<h3>Perfil</h3><p>Dados do usuário.</p>`},
    'prefs': {title:'Preferências', html:`<h3>Preferências</h3><p>Ajustes do sistema.</p>`},
    'reports': {title:'Relatórios', html:`<h3>Relatórios</h3><p>Visões e gráficos (placeholder).</p>`}
  };

  const s = screens[name] || {title:'Tela', html:`<h3>${name}</h3><p>Conteúdo padrão.</p>`};
  title.textContent = s.title;
  screen.innerHTML = s.html;

  if(window.innerWidth < 800){ 
    sidebar.classList.add('collapsed'); 
  }
}

window.addEventListener('keydown', e=>{ 
  if(e.key.toLowerCase()==='m'){ toggleSidebar(); } 
});
