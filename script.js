function clicouBotao() {
    document.getElementById("template").innerHTML = `
      <div class="meu-template">
        <h1>Meu template</h1>
        <p>Este é o meu template HTML.</p>
        <button>Clique aqui</button>
      </div>
    `;
  }
  
  document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("meuBotao").addEventListener("click", clicouBotao);
  });
  