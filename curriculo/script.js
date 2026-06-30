// Alternar tema claro/escuro
const btn = document.getElementById('themeToggle');
btn.addEventListener('click', () => {
  document.body.classList.toggle('dark');
});

// Validação e envio simulado do formulário de contato
document.getElementById('contatoForm').addEventListener('submit', function (e) {
  e.preventDefault(); // impede o envio real da página

  const nome = document.getElementById('nome').value.trim();
  const email = document.getElementById('email').value.trim();
  const mensagem = document.getElementById('mensagem').value.trim();

  // Limpa erros anteriores antes de revalidar
  document.getElementById('erroNome').textContent = '';
  document.getElementById('erroEmail').textContent = '';
  document.getElementById('erroMensagem').textContent = '';

  let valido = true;

  // Validação do nome
  if (nome === '') {
    document.getElementById('erroNome').textContent = 'Informe seu nome.';
    valido = false;
  }

  // Validação do e-mail com regex
  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (email === '') {
    document.getElementById('erroEmail').textContent = 'Informe seu e-mail.';
    valido = false;
  } else if (!regexEmail.test(email)) {
    document.getElementById('erroEmail').textContent = 'E-mail inválido.';
    valido = false;
  }

  // Validação da mensagem
  if (mensagem === '') {
    document.getElementById('erroMensagem').textContent = 'Escreva uma mensagem.';
    valido = false;
  }

  // Se tudo válido: limpa o formulário e mostra confirmação
  if (valido) {
    document.getElementById('contatoForm').reset();
    document.getElementById('confirmacao').style.display = 'block';
  }
});
