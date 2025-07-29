1. Importando bibliotecas
```
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
```

📝 Explicações:
- tensorflow: biblioteca principal usada para construir e treinar redes neurais.
- tensorflow_datasets (tfds): ferramenta da própria equipe do TensorFlow que facilita o acesso a bases de dados famosas.
- matplotlib.pyplot: biblioteca usada para visualizar gráficos, como curvas de acurácia.

2. Carregando o dataset Caltech101
```
(ds_train, ds_test), ds_info = tfds.load(
    'caltech101',
    split=['train[:80%]', 'train[80%:]'],
    shuffle_files=True,
    as_supervised=True,
    with_info=True
)
```

📝 Explicações:
- tfds.load: baixa e prepara o dataset automaticamente.
- 'caltech101': nome do dataset a ser carregado.
- split: separa o conjunto em 80% para treino, 20% para teste.
- shuffle_files=True: embaralha os arquivos para não ter viés na ordem.
- as_supervised=True: retorna tuplas (imagem, rótulo) ao invés de dicionários.
- with_info=True: retorna metadados do dataset (como o nome das classes).

3. Verificando os nomes das classes
```
print(ds_info.features['label'].names)
```

📝 Explicações:
- Mostra uma lista com os nomes das 101 classes (ex: 'camera', 'airplanes', etc.).

4. Selecionando duas classes específicas
```
selected_classes = ['camera', 'motorbikes']
class_names = ds_info.features['label'].names
selected_ids = [class_names.index(name) for name in selected_classes]
```

📝 Explicações:
- selected_classes: você define manualmente as duas classes que deseja usar.
- class_names: lista com o nome de todas as classes do dataset.
- selected_ids: obtém os índices numéricos correspondentes aos nomes selecionados (necessário para filtrar depois).

5. Filtrando apenas essas duas classes
```
def filter_classes(image, label):
    return tf.reduce_any([label == selected_ids[0], label == selected_ids[1]])
```

📝 Explicações:
- Função que será usada para filtrar apenas imagens cujos rótulos pertençam às duas classes escolhidas.
- tf.reduce_any(...): retorna True se qualquer condição for verdadeira.

6. Reconvertendo rótulos para 0 e 1
```
def reencode_labels(image, label):
    new_label = tf.cast(label == selected_ids[1], tf.int64)
    return image, new_label
```

📝 Explicações:
- Convertemos os rótulos para 0 ou 1 para facilitar o uso de classificação binária.
- Se o rótulo for igual à segunda classe (ex: 'motorbikes'), ele vira 1; senão, 0.

7. Pré-processamento de imagens
```
IMG_SIZE = (160, 160)
BATCH_SIZE = 32

def preprocess(image, label):
    image = tf.image.resize(image, IMG_SIZE) / 255.0
    return image, label
```

📝 Explicações:
- IMG_SIZE: define que todas as imagens terão tamanho 160x160 pixels.
- BATCH_SIZE: número de imagens processadas por vez durante o treino.
- preprocess: redimensiona cada imagem e normaliza os pixels (de 0 a 1).

8. Aplicando filtros e criando os datasets finais
```
train_ds = ds_train.filter(filter_classes).map(reencode_labels).map(preprocess).batch(BATCH_SIZE).prefetch(1)
test_ds = ds_test.filter(filter_classes).map(reencode_labels).map(preprocess).batch(BATCH_SIZE).prefetch(1)
```

📝 Explicações:
- .filter(...): aplica a função de filtro para manter só as duas classes.
- .map(...): aplica a conversão de rótulos e depois o pré-processamento.
- .batch(BATCH_SIZE): agrupa imagens em lotes de 32.
- .prefetch(1): melhora o desempenho carregando os dados enquanto o modelo treina.

9. Carregando o modelo pré-treinado MobileNetV2
```
base_model = tf.keras.applications.MobileNetV2(
    input_shape=IMG_SIZE + (3,),
    include_top=False,
    weights='imagenet'
)
base_model.trainable = False
```

📝 Explicações:
- MobileNetV2: rede treinada com milhões de imagens (ImageNet).
- input_shape: precisa combinar com o tamanho das nossas imagens (160x160x3).
- include_top=False: remove a “cabeça” original do modelo (classificador original).
- weights='imagenet': carrega os pesos já treinados.
- trainable=False: congela os pesos para usar como extrator de características fixo.

10. Adicionando novas camadas para nosso problema
```
model = tf.keras.Sequential([
    base_model,
    tf.keras.layers.GlobalAveragePooling2D(),
    tf.keras.layers.Dense(1, activation='sigmoid')
])
```

📝 Explicações:
- Sequential: cria uma pilha de camadas.
- GlobalAveragePooling2D: resume cada mapa de ativação com uma média (reduz parâmetros).
- Dense(1, activation='sigmoid'): camada final com 1 saída para classificação binária.

11. Compilando o modelo
```
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
```

📝 Explicações:
- optimizer='adam': algoritmo eficiente para ajuste dos pesos.
- loss='binary_crossentropy': função de perda usada em classificações binárias.
- metrics=['accuracy']: acompanha a acurácia durante o treinamento.

12. Treinando o modelo
```
history = model.fit(
    train_ds,
    validation_data=test_ds,
    epochs=5
)
```

📝 Explicações:
- model.fit(...): treina o modelo.
- epochs=5: faz 5 passagens completas pelos dados.
- validation_data: validação com dados que o modelo nunca viu.

13. Visualizando a acurácia
```
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

plt.plot(acc, label='Treinamento')
plt.plot(val_acc, label='Validação')
plt.legend()
plt.title("Acurácia por Época")
plt.show()
```

📝 Explicações:
- history.history: contém os registros da acurácia a cada época.
- plt.plot: desenha os gráficos para comparar treino vs. validação.
- Isso ajuda a ver se o modelo está aprendendo ou sofrendo overfitting.