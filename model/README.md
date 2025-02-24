# 📦 Modelo Salvo com Joblib

Este diretório contém um modelo de machine learning salvo no formato .pkl utilizando a biblioteca joblib.

📌 Descrição

O arquivo svmBreastCancer.pkl contém um modelo treinado que pode ser carregado e utilizado para fazer previsões sem a necessidade de re-treinamento. Além disso, o arquivo scalerBreastCancer.pkl contém o standardScaler usado para normalizar os dados.

🚀 Como Usar

Para carregar o modelo em Python, utilize o seguinte código:

```python
import joblib

# Carregar o modelo
modelo = joblib.load("svmBreastCancer.pkl")
scaler = joblib.load("scalerBreastCancer.pkl")

# Fazer previsões
X_scaled = scaler.transform(X_novo)
predicao = modelo.predict(X_scaled)
```
📝 Observações

- Certifique-se de que a biblioteca joblib está instalada (`pip install joblib`).
- O modelo foi treinado com um conjunto de dados específico, então os dados de entrada para previsão devem seguir o mesmo formato.

Desenvolvido por Israel Alves🚀

