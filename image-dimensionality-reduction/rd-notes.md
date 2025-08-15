# Redução de Dimensionalidade em Machine Learning

Redução de dimensionalidade é o processo de **diminuir o número de variáveis (features)** de um conjunto de dados, mantendo ao máximo as informações relevantes. É uma etapa crucial no **pré-processamento de dados** para melhorar desempenho, reduzir custo computacional e evitar overfitting.

---

## 📚 Por que reduzir a dimensionalidade?

- **Eliminar redundância e ruído** nos dados  
- **Melhorar performance de algoritmos** (especialmente em dados de alta dimensão)
- **Visualizar dados complexos** em 2D ou 3D
- **Evitar a maldição da dimensionalidade**  
  (quando muitos atributos pioram a performance dos modelos)

---

## 🧩 Tipos de Redução de Dimensionalidade

| Técnica                          | Tipo       | Preserva variância? | Exemplo de uso                                   |
|----------------------------------|------------|----------------------|--------------------------------------------------|
| PCA (Principal Component Analysis) | Linear     | Sim                  | Imagens, dados tabulares                         |
| t-SNE (t-distributed Stochastic Neighbor Embedding) | Não linear | Não (foca em estrutura local) | Visualização de dados em 2D/3D                   |
| UMAP (Uniform Manifold Approximation and Projection) | Não linear | Parcialmente           | Clustering e visualização                        |
| Autoencoders (Redes Neurais)    | Não linear | Depende do treinamento| Compressão de dados, imagens, voz                |
| Seleção de Features (e.g., SelectKBest) | Filtragem | Depende              | Modelos interpretáveis, feature engineering      |

---

## 📖 Teoria: PCA (Principal Component Analysis)

O **PCA** é uma técnica estatística que transforma os dados originais em um novo espaço de coordenadas, chamado de **componentes principais**, que são:

1. **Ortogonais** entre si (sem correlação)
2. Ordenados pela **variância** que explicam nos dados

### Etapas do PCA:
1. Centralizar os dados (remover a média)
2. Calcular a matriz de covariância
3. Obter os autovalores e autovetores
4. Ordenar por maior variância
5. Projetar os dados nos novos eixos (componentes)

---

## 🛠️ Prática: Exemplo com PCA em Python

```python
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Carregando os dados
data = load_iris()
X = data.data
y = data.target

# Redução para 2 dimensões
pca = PCA(n_components=2)
X_reduzido = pca.fit_transform(X)

# Visualização
plt.scatter(X_reduzido[:, 0], X_reduzido[:, 1], c=y, cmap='viridis')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PCA - Iris Dataset')
plt.show()
```

## ⚙️ Prática: Quando usar Redução de Dimensionalidade?

| Situação                                    | Usar? | Técnica recomendada         |
|---------------------------------------------|-------|------------------------------|
| Dados com muitas colunas correlacionadas    | ✅     | PCA ou Autoencoder           |
| Visualização em 2D/3D                       | ✅     | t-SNE ou UMAP                |
| Explicar variáveis de forma interpretável   | ❌     | (Redução pode prejudicar)    |
| Dados de imagem, áudio ou séries temporais  | ✅     | Autoencoders ou PCA          |

---

## 🚧 Limitações e Cuidados

- ❗ **Perda de interpretabilidade**: novos componentes podem ser difíceis de entender
- ❗ **Risco de perda de informação útil** se o número de componentes for muito reduzido
- ❗ **Overfitting em autoencoders** se não forem treinados corretamente
- ❗ t-SNE e UMAP não servem para generalização (só para visualização)

---

## 📌 Conclusão

Redução de dimensionalidade é uma ferramenta poderosa para:
- Simplificar dados
- Acelerar o treinamento de modelos
- Visualizar padrões escondidos

Ela deve ser usada com **consciência do objetivo** (visualização, desempenho, interpretabilidade) e sempre analisando o **trade-off entre simplificação e perda de informação**.
