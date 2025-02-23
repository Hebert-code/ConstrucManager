[JAVASCRIPT__BADGE]: https://img.shields.io/badge/Javascript-000?style=for-the-badge&logo=javascript
[TYPESCRIPT__BADGE]: https://img.shields.io/badge/typescript-D4FAFF?style=for-the-badge&logo=typescript
[REACT__BADGE]: https://img.shields.io/badge/React-005CFE?style=for-the-badge&logo=react
[VUE__BADGE]: https://img.shields.io/badge/VueJS-fff?style=for-the-badge&logo=vue
[GATSBY__BADGE]: https://img.shields.io/badge/Gatsby-7026b9?style=for-the-badge&logo=gatsby
[ANGULAR__BADGE]: https://img.shields.io/badge/Angular-red?style=for-the-badge&logo=angular
[PROJECT__BADGE]: https://img.shields.io/badge/Visit_this_project-000?style=for-the-badge&logo=project
[PROJECT__URL]: https://github.com/Fernanda-Kipper/Readme-Templates

<h1 align="center" style="font-weight: bold;">ConstrucManager 🏗️</h1>

![django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![html5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![css3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![aws](https://img.shields.io/badge/Amazon_AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

<p align="center">
 <a href="#about">Sobre</a> • 
 <a href="#started">Decolando</a> • 
  <a href="#routes">Rotas da Aplicação</a> • 
  <a href="#colab">Contribuidores</a> •
 <a href="#contribute">Contribuir</a>
</p>


<p align="center">
    <img src="https://github.com/user-attachments/assets/70249ce0-a299-40e1-abe7-10dac7bfd371" alt="Image Example" width="1000px">
</p>

<p align="center">
    <img src="https://github.com/user-attachments/assets/991d4614-7ced-4eeb-a33e-46f13f7456ee" width="500px">
</p>

<p align="center">
    <img src="https://github.com/user-attachments/assets/7d113099-cc2e-4ad9-8f96-066126a8f93f" alt="Image Example" width="500px">
</p>

<h2 id="about">📌 Sobre</h2>

Este projeto foi desenvolvido como parte da disciplina de Sistemas Distribuídos, com o objetivo de aplicar e consolidar diversos conceitos aprendidos em sala de aula. Trata-se de um aplicativo completo para o gerenciamento de uma loja de material de construção, que permite o cadastro de produtos, fornecedores e clientes, além de facilitar a realização de vendas e compras. O sistema também oferece funcionalidades para gerenciar o estoque e controlar as vendas diárias. O backend foi desenvolvido utilizando Django, enquanto o frontend foi construído com HTML e CSS. Para o armazenamento de dados, foram utilizados os serviços da AWS, e a hospedagem foi realizada no Google Cloud, demonstrando a aplicação prática de conceitos de sistemas distribuídos em um ambiente real.
<h2 id="started">🚀 Decolando</h2>

Para rodar o projeto localmente, siga os passos abaixo:

<h3>Pré-requisitos</h3>

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/)
- [AWS CLI](https://aws.amazon.com/cli/) (para configurar o acesso ao banco de dados AWS)
- [Google Cloud SDK](https://cloud.google.com/sdk) (para configurar o acesso à hospedagem do Google Cloud)

<h3>Clonagem</h3>

Clone o repositório do projeto:

```bash
git clone https://github.com/Hebert-code/ConstrucManager.git
```

<h3>Começando</h3>

Navegue até a pasta do projeto:

```bash
cd ConstrucManager
```
Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Linux/macOS
venv\Scripts\activate  # No Windows
```
Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```
Configure o banco de dados AWS e as variáveis de ambiente necessárias.

Execute as migrações do Django:

```bash
python manage.py migrate
```
Inicie o servidor de desenvolvimento:

```bash
python manage.py runserver
```

<h2 id="routes">📍  Rotas da Aplicação (Django)</h2>

Aqui estão as principais rotas da aplicação Django:

| Rota               | Descrição                                          
|----------------------|-----------------------------------------------------
|<kbd>/home/</kbd>                      | Página inicial do sistema.
<kbd>/clientes/</kbd>                   | Lista todos os clientes cadastrados.
<kbd>/clientes/novo/</kbd>              | Formulário para criar um novo cliente.
<kbd>/clientes/editar/:pk/</kbd>        | Formulário para editar um cliente existente.
<kbd>/clientes/deletar/:pk/</kbd>       | Deleta um cliente existente.
<kbd>/produtos/</kbd>                   | Lista todos os produtos cadastrados.
<kbd>/produtos/novo/</kbd>              | Formulário para cadastrar um novo produto.
<kbd>/produtos/editar/:pk/</kbd>        | Formulário para editar um produto existente.
<kbd>/produtos/excluir/:pk/</kbd>       | Deleta um produto existente.
<kbd>/fornecedores/</kbd>               | Lista todos os fornecedores cadastrados.
<kbd>/fornecedores/novo/</kbd>          | Formulário para cadastrar um novo fornecedor.
<kbd>/fornecedores/editar/:pk/</kbd>    | Formulário para editar um fornecedor existente.
<kbd>/fornecedores/excluir/:pk/</kbd>   | Deleta um fornecedor existente.
<kbd>/vendas/</kbd>                     | Lista todas as vendas realizadas.
<kbd>/vendas/novo/</kbd>                | Formulário para registrar uma nova venda.
<kbd>/vendas/editar/:venda_id/</kbd>    | Formulário para editar uma venda existente.
<kbd>/vendas/excluir/:venda_id/</kbd>   | Deleta uma venda existente.
<kbd>/compras/</kbd>                    | Lista todas as compras realizadas.
<kbd>/compras/novo/</kbd>               | Formulário para registrar uma nova compra.
<kbd>/compras/detalhar/:compra_id/</kbd>| Detalhes de uma compra específica.
<kbd>/compras/cancelar/:compra_id/</kbd>| Cancela uma compra específica.
<kbd>/estoque/</kbd>                    | Consulta o estoque de produtos.
<kbd>/estoque/atualizar/:produto_id/</kbd> | Formulário para atualizar o estoque de um produto.
<kbd>/estoque/alertas/</kbd>            | Exibe alertas de estoque baixo.

<h2 id="colab">🤝 Contribuidores</h2>

Agradecimento especial a todos que contribuíram para este projeto.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/111450232?v=4" width="100px;" alt="Hebert Henrique"/><br>
        <sub>
          <b>Hebert Henrique</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/76446377?v=4" width="100px;" alt="Gustavo Souza"/><br>
        <sub>
          <b>Gustavo Souza</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/145232952?v=4" width="100px;" alt="Luiz Carlos"/><br>
        <sub>
          <b>Luiz Carlos</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribuir</h2>

Para contribuir com o projeto, siga os passos abaixo:

1. Faça um fork do repositório:
```bash
git clone https://github.com/Hebert-code/ConstrucManager.git
```
    
2. Crie uma branch para a sua feature: git checkout -b feature/minha-feature
    
3. Siga os padrões de commit.
    
4. Abra um Pull Request explicando o problema resolvido ou a feature implementada. Se houver modificações visuais, adicione screenshots e aguarde a revisão!

