const botao = document.querySelector("#botao");
let mensagem = document.querySelector("#mensangem");

botao.addEventListener("click", exibirMensagem);

function exibirMensagem(){
    mensagem.innerHTML = "Olá, é um prazer te conhecer!!!";
    setTimeout(()=>{
        mensagem.innerHTML="";
    },5000);
}