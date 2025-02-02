# Custom Wallpaper

![Custom Wallpaper](https://img.shields.io/badge/version-1.0-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)
![Pillow](https://img.shields.io/badge/Pillow-9.0-green)

**Custom Wallpaper** é um programa que permite personalizar imagens redimensionando-as ao formato A4 e adicionando textos personalizados em posições estratégicas. O aplicativo é simples, eficiente e fácil de usar, ideal para criar papéis de parede personalizados para impressão ou uso digital.

## 🚀 Funcionalidades

- **Redimensionamento de imagens**: Ajusta qualquer imagem enviada para o formato A4.
- **Adição de texto**: Insere textos personalizados na parte superior, central ou inferior da imagem.
- **Pré-visualização**: Mostra a imagem ajustada antes de realizar o download.
- **Exportação em PNG**: Baixe a imagem editada diretamente no formato PNG.

## 🛠 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) - Framework para criação de aplicativos web interativos.
- [Pillow](https://pillow.readthedocs.io/) - Biblioteca de manipulação de imagens.

## 📋 Pré-requisitos

Antes de começar, certifique-se de ter o seguinte instalado:

- Python 3.8 ou superior
- Pip para gerenciar pacotes Python

## 🖥 Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/masilvaarcs/custom_wallpaper.git
   cd custom_wallpaper
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # No Windows: .venv\Scripts\activate
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o programa**:
   ```bash
   streamlit run src/custom_wallpaper.py
   ```

5. **Acesse no navegador**:
   O aplicativo será aberto automaticamente. Caso contrário, acesse o endereço exibido no terminal (geralmente `http://localhost:8501`).

## 📂 Estrutura do Projeto

```plaintext
custom_wallpaper/
├── .venv/                    # Ambiente virtual
├── src/                      # Código-fonte do projeto
│   └── custom_wallpaper.py   # Código principal do aplicativo
├── requirements.txt          # Dependências do projeto
└── README.md                 # Documentação do projeto
```

## 📝 Como Usar

1. Faça o upload de uma imagem no aplicativo.
2. Insira os textos desejados para o topo, centro e parte inferior.
3. Clique no botão **Aplicar Texto** para adicionar os textos à imagem.
4. Baixe a imagem editada clicando no botão **Baixar Imagem**.

## 💡 Exemplos de Uso

- Criar papéis de parede personalizados.
- Adicionar mensagens motivacionais ou informativas em imagens.
- Preparar imagens para impressão no formato A4.

## 🤝 Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias.

1. Fork o repositório.
2. Crie uma branch com a nova funcionalidade:
   ```bash
   git checkout -b minha-nova-funcionalidade
   ```
3. Faça commit das alterações:
   ```bash
   git commit -m 'Adiciona nova funcionalidade'
   ```
4. Envie a branch:
   ```bash
   git push origin minha-nova-funcionalidade
   ```
5. Abra um Pull Request.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

Criado por [@masilvaarcs](https://github.com/masilvaarcs). 😊
```
