<div align="center">
  <h1>🤖 LangChain Unit Test Generator</h1>
  <p align="center">
    Automatização da criação de testes unitários utilizando LLMs.<br/>
    <a href="https://github.com/sofiahernandes/machine-learning-studies/issues">Report Bug</a>
    |
    <a href="https://github.com/sofiahernandes/machine-learning-studies/issues">Request Feature</a>
  </p>
</div>
<br/>

## 🚀 Tech Stack
- Python
- LangChain
- Azure OpenAI / ChatGPT
- Pytest

Os testes são gerados usando dois modos:
- `prod`: Gera os testes via **Azure OpenAI + LangChain**
- `mock`: Simula uma resposta da API (sem custos)

E dois modos de execução (definidos no `.env`):
```env
MODE=prod # Para rodar com Azure ChatGPT (produção)
MODE=mock # Para simular resultado (sem consumir API)
```

## 🛠️ Começando
1. Clone o projeto
2. Crie um `.env` com base no `.env.example`
3. Instale as dependências:
```bash
pip install langchain langchain-community langchain-openai python-dotenv
```

4. Execute:
```bash
python main.py
```

5. Teste o arquivo gerado:
```bash
pytest generated_tests/
```

> ⚠️ Caso tenha problemas com os comandos tente executar com **python3** ou **python3 -m**.
<br/>

Este projeto foi inspirado no automatizador de testes do [romanozamoth](https://github.com/romanozamoth) para fins de estudo.

---

<div align="center">
  <h1>📩 Vamos nos Conectar!</h1>
  <a href="https://github.com/sofiahernandes"><img height="30px" src="https://skillicons.dev/icons?i=github"/></a><span> ∙ </span>
  <a href="https://www.linkedin.com/in/sofiahernandes"><img height="30px" src="https://skillicons.dev/icons?i=linkedin"/></a><span> ∙ </span>
  <a href="mailto:sofiahernandes.dev@gmail.com"><img height="30px" src="https://skillicons.dev/icons?i=gmail"/></a><span> ∙ </span>
  <a href="https://www.instagram.com/sofiabotechia/"><img height="30px" src="https://skillicons.dev/icons?i=instagram"/></a>
</div>