<div align="center">
  <h1>🤖 STRIDE Threat Analyzer (pt-br)</h1>
  <p align="center">
    Solução completa para análise de ameaças baseada na metodologia STRIDE, composta por um backend com FastAPI (Python) e um front-end em HTML/CSS/JS com visualização de ameaças usando Cytoscape.js.
    <a href="https://learn.microsoft.com/pt-br/azure/security/develop/threat-modeling-tool-threats"><p>Sobre a ferramenta de modelagem de ameaças</p></a>
    <a href="https://github.com/sofiahernandes/ml-studies/issues">Report Bug</a>
    |
    <a href="https://github.com/sofiahernandes/ml-studies/issues">Request Feature</a>
  </p>
</div>
<br/>

## 🚀 Tech Stack
- Azure OpenAI
- FastAPI
- Cytoscape.js

## ✨ Features
🔐 Upload de imagem e preenchimento de informações sobre o sistema  
🔐 Geração automática de modelo de ameaças STRIDE usando Azure OpenAI  
🔐 Visualização do modelo de ameaças em grafo interativo (Cytoscape.js)  
🔐 Sugestões de melhoria para o modelo de ameaças  
🔐 Botão para imprimir/exportar o grafo gerado  
<br/>

![Sobre o Stride](/public//stride.png)

<br/>

## 🛠️ Começando

### Pré-requisitos
- Python 3.10+
- Node.js
- Conta e deployment no Azure OpenAI

### 1. Clone o Repositório
Baixe o arquivo `.zip` e extraia a pasta `azure-openai-agent` para a sua pasta de projetos. Abra ela na cmd ou na sua IDE de preferência.
```bash
 cd azure-openai-agent
```

### 2. Configure o backend

1. Acesse a pasta do backend:
   ```bash
   cd backend
   ```
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install openai fastapi uvicorn
   ```
4. Crie um arquivo `.env` com seus dados do Azure OpenAI:
   ```env
   AZURE_OPENAI_API_KEY=your_key
   AZURE_OPENAI_ENDPOINT=https://<your-endpoint>.openai.azure.com
   AZURE_OPENAI_API_VERSION=2025-01-01
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o-mini
   ```

    Para conseguir essas variáveis, siga o caminho:  
    &nbsp;a) [Microsoft Azure](https://azure.microsoft.com/pt-br/get-started/azure-portal/)  
    &nbsp;b) Criar um Recurso > Azure OpenAI  
    &nbsp;c) Explore Azure AI Foundry Portal > Chat  
    &nbsp;d) Escolha o modelo gpt-4.1-mini-2 (version:2025-04-14)  
    &nbsp;e) Exibir Código > Autenticação de Chave  
    &nbsp;f) Pegue o API Version (no código)  
    &nbsp;g) Role essa tela para baixo  
    &nbsp;h) Pegue o ponto de extremidade (até "...azure.com")  
    &nbsp;i) Pegue a chave de API

5. Execute o backend (http://localhost:8001):
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8001
   ```

### 3. Configure o front-end

1. Acesse a pasta do front-end:
   ```bash
   cd ../frontend
   ```
2. Basta abrir o arquivo `index.html` com o Live Server.
<br/>

## Cuidados e dicas
- **Azure OpenAI:** Certifique-se de que seu deployment está ativo e as variáveis do `.env` estão corretas.
- **CORS:** O backend já está configurado para aceitar requisições de qualquer origem, mas se for usar em produção, ajuste as origens permitidas.
- **Limite de tokens:** O modelo do Azure OpenAI pode ter limites de tokens. Ajuste `max_tokens` se necessário.
- **Impressão do grafo:** O botão "Imprimir Grafo" exporta a visualização atual do grafo como imagem para impressão ou PDF.
- **Formato do JSON:** O front-end espera o JSON no formato retornado pelo backend. Se mudar o backend, ajuste o front-end conforme necessário.
- **Portas:** Certifique-se de que as portas 8001 (backend) e 8080 (front-end, se usar servidor) estejam livres.

---

<div align="center">
  <h1>📩 Vamos nos Conectar!</h1>
  <a href="https://github.com/sofiahernandes"><img height="30px" src="https://skillicons.dev/icons?i=github"/></a><span> ∙ </span>
  <a href="https://www.linkedin.com/in/sofiahernandes"><img height="30px" src="https://skillicons.dev/icons?i=linkedin"/></a><span> ∙ </span>
  <a href="mailto:sofiahernandes.dev@gmail.com"><img height="30px" src="https://skillicons.dev/icons?i=gmail"/></a><span> ∙ </span>
  <a href="https://www.instagram.com/sofiabotechia/"><img height="30px" src="https://skillicons.dev/icons?i=instagram"/></a>
</div>
