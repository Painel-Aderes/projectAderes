# ProjectAderes

> Esse reposito é destinado ao template de Django funcionado em Contêiner


## 💻 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
<!---Estes são apenas requisitos de exemplo. Adicionar, duplicar ou remover conforme necessário--->
* Você instalou a versão mais recente de `<Python3 / Docker / TablePlus>`
* TablePlus, para visualização dos dados no banco.
* Banco dados criado em PostgreSQL.
* Docker para funcionar os container.
* Você tem uma máquina `<Windows / Linux / Mac>`. 
* Download Docker  [Windowns](https://www.docker.com/products/docker-desktop/) / [Linux](https://docs.docker.com/engine/install/ubuntu/) / [MacOS](https://docs.docker.com/desktop/install/mac-install/).

## 🚀 Instalando ProjectAderes

Para instalar o ProjectAderes, siga estas etapas:

Clonar o projeto:
```
https://github.com/Painel-Aderes/projectAderes.git
```

Acesse a pasta, e passe segunte comando no terminal, para iniciar banco dados:
```
docker compose up -d db
```

Use esse comando para "build" do projeto:
```
docker build .
```

Use o comando para iniciar o docker compose:
```
docker compose up 
```
## ☕ Usando ProjectAderes

Para usar ProjectAderes, acesso o endpoint:

```
https://localhost:8000/users
```

Para funcionar é preciso só ter projeto funcionando na porta 8000

## 📫 Contribuindo para Django_Docker
<!---Se o seu README for longo ou se você tiver algum processo ou etapas específicas que deseja que os contribuidores sigam, considere a criação de um arquivo CONTRIBUTING.md separado--->
Para contribuir com ProjectAderes, siga estas etapas:

1. Bifurque este repositório.
2. Crie um branch: `git checkout -b <nome_branch>`.
3. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`
4. Envie para o branch original: `git push origin <ProjectAderes> / <local>`
5. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).



## 📝 Licença

Esse projeto está sob licença. Veja o arquivo [LICENÇA](LICENSE.md) para mais detalhes.

[⬆ Voltar ao topo](#nome-do-projeto)<br>
