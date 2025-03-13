const toggleTheme = document.getElementById('toggleTheme');

// Adiciona um evento de clique ao botão
toggleButton.addEventListener('click', () => {
  // Verifica qual tema está ativo
  const currentTheme = document.documentElement.getAttribute('data-theme');
  
  // Alterna entre os temas
  if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'light'); // Muda para o tema claro
  } else {
    document.documentElement.setAttribute('data-theme', 'dark'); // Muda para o tema escuro
  }
});