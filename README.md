# 

<h2 align="center">Http Proxy Analyst</h2>

<p align="center">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/panda12332145/http-proxy-analyst">
  
  <a href="https://github.com/panda12332145/http-proxy-analyst/commits/master">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/panda12332145/http-proxy-analyst">
  </a>
 
   <a href="https://github.com/panda12332145/http-proxy-analyst">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/panda12332145/http-proxy-analyst?style=social">
  </a>
 
</p>

<h2 id="Sobre">🔖 Resumo</h2>
<p align="center">Este código em Python é um utilitário para baixar uma lista de proxies da internet, testar sua funcionalidade e salvar os proxies funcionando em um arquivo de saída. Ele utiliza a biblioteca `requests` para fazer requisições HTTP e testar os proxies. </p>

<h3 id="Sobre">Para que serve:</h3>
<p align="center">Este código serve para automatizar o processo de obtenção e teste de proxies, útil em cenários onde é necessário verificar a funcionalidade de proxies para tarefas como scraping da web, anonimização de tráfego ou contornar restrições de rede. </p>
<p align="center">- Automatiza o processo de obtenção e teste de proxies. <br>
- Permite economizar tempo ao não ter que verificar manualmente cada proxy.<br>
- Facilita a obtenção de proxies funcionando para diferentes propósitos, como scraping ou anonimização. </p>

<h2 id="Demonstrac-oes">📽 Demonstração</h2>

  <p align="center">
  <kbd>
  <img width="500" style="border-radius: 5px" height="400" src="https://raw.githubusercontent.com/panda12332145/http-proxy-analyst/main/imagens/Screenshot_20210714-014314%20-%20Copia.jpg">
    <img width="100" style="border-radius: 5px" height="400" src="https://raw.githubusercontent.com/panda12332145/http-proxy-analyst/main/imagens/Screenshot_20210714-014314%20-%20.jpg">
  </kbd>
  </p>

<h2 id="Como Executar">⚙️  Explicação das partes importantes:</h2>
1. **Função `download_proxies`**: 
   - Esta função baixa a lista de proxies de uma URL especificada e a salva em um arquivo local.

2. **Função `verificar_proxy`**:
   - Testa a funcionalidade de um proxy específico fazendo uma requisição HTTP a um site de exemplo. Retorna o status do proxy.

3. **Função `salvar_proxys_funcionando`**:
   - Salva os proxies que foram verificados como funcionando em um arquivo de saída.

4. **Função `testar_proxies`**:
   - Lê a lista de proxies de um arquivo.
   - Testa cada proxy da lista usando a função `verificar_proxy`.
   - Salva os proxies funcionando usando a função `salvar_proxys_funcionando`.

5. **Bloco principal (`__name__ == "__main__"`)**:
   - Define a URL da API de onde a lista de proxies será baixada.
   - Solicita ao usuário o nome do arquivo de saída para os proxies funcionando.
   - Chama as funções `download_proxies`, `testar_proxies` e remove o arquivo temporário.

<h2 id="Como Executar">⚙️ Como Executar</h2>

### Requisitos
+ Python 3.9 ou superior
+ Requests
+ OS

Com as dependencias devidamente instaladas basta baixar o projeto e executar o arquivo `http-proxy-analyst`

<h2 id="autor">👾 Autor</h2>

<img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/73090399?v=4" width="100px;"/>

<p>Feito por Panda12332145 👋🏽</p>
