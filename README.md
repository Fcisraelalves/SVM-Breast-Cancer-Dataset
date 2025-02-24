# Classificação do Dataset Breast Cancer com SVM

Este projeto utiliza o algoritmo **Support Vector Machine (SVM)** para classificação do dataset **Breast Cancer**. O objetivo é prever se um tumor é maligno ou benigno com base em diversas medições.

## 📌 Descrição
O dataset Breast Cancer contém informações sobre 569 amostras de tumores, divididas em duas classes:
- **Maligno**
- **Benigno**

Cada amostra possui 30 atributos, incluindo:
- **Raio médio**
- **Textura média**
- **Perímetro médio**
- **Área média**
- **Suavidade média**
- Entre outros...

O modelo SVM é treinado para identificar a natureza do tumor com base nesses atributos.

## 🛠 Tecnologias Utilizadas
- **Python**
- **Scikit-learn** (para implementação do SVM)
- **Pandas** (para manipulação do dataset)
- **Matplotlib & Seaborn** (para visualização de dados)
- **Jupyter Notebook** (para desenvolvimento e testes)

## 💂 Estrutura do Projeto
```
/
|-- Breast_Cancer.ipynb  # Notebook contendo o código do projeto
|-- README.md   # Documentação do projeto
|-- requirements.txt  # Lista de dependências
```

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/svm-breast-cancer.git
   ```

2. Acesse a pasta do projeto:
   ```bash
   cd svm-breast-cancer
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Execute o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

6. Abra o arquivo `Breast_Cancer.ipynb` e execute as células passo a passo.

## 📊 Resultados
- Visualização das distribuições dos dados.
- Treinamento e avaliação do modelo SVM.
- Testes de previsão com novos dados.

## 📝 Contribuição
Se quiser contribuir com melhorias, sinta-se à vontade para:
1. Fazer um fork do repositório.
2. Criar uma branch para suas modificações:
   ```bash
   git checkout -b minha-modificacao
   ```
3. Commitar suas mudanças:
   ```bash
   git commit -m "Melhoria no modelo SVM"
   ```
4. Enviar suas alterações para o repositório remoto:
   ```bash
   git push origin minha-modificacao
   ```
5. Abrir um Pull Request.

## 🐝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usá-lo e modificá-lo como desejar.

---
Desenvolvido por Israel Alves 🚀

---

