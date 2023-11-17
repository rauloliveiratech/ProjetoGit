# Projeto Git 📚🔗

## Descrição

O Projeto Git é um espaço para aprender e compartilhar conhecimentos valiosos sobre o Git, uma ferramenta fundamental no desenvolvimento de software.

## Configuração Inicial
```bash
# Configurações Globais
git config --global user.name "Fulano de tal"
git config --global user.email "Fulano@gmail.com"

git branch -M "Main" # Altera o nome da branch master para "Main"

git remote add origin https://github.com/rauloliveiratech/ProjetoGit.git

git pull origin main # Puxa o repositório da branch main
```

## Comandos Úteis
```bash
git checkout -b "novo-botao" # Cria uma nova branch chamada "novo-botao"

git revert abc123 # Reverte o commit com o hash "abc123"

git remote set-url origin nova_URL # Atualiza a URL remota do repositório

git init # Inicia um novo repositório Git

git add "Readme.md" # Adiciona o arquivo para ser commitado

git status # Mostra os commits pendentes

git commit readme.md -m "minha mensagem de commit" # Faz o commit do arquivo readme.md com uma mensagem

git push origin main # Envia o commit para o Github na branch main
```
