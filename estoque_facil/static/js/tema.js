const toggleButton = document.getElementById('toggleTheme');

window.onload = () => {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme) {
        document.documentElement.setAttribute('data-theme', savedTheme);
    } else {
        document.documentElement.setAttribute('data-theme', 'light'); // Tema padrão
    }
};

toggleButton.addEventListener('click', () => {
  const currentTheme = document.documentElement.getAttribute('data-theme');
  
  if (currentTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'light'); // Muda para o tema claro
      localStorage.setItem('theme', 'light'); // Salva no localStorage
  } else {
      document.documentElement.setAttribute('data-theme', 'dark'); // Muda para o tema escuro
      localStorage.setItem('theme', 'dark'); // Salva no localStorage
  }
});
