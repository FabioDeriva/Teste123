# Projeto de Teste do GitHub

Este projeto tem como objetivo testar o GitHub e explorar suas funcionalidades.

# Comandos Git Essenciais

![Logo Github](images.png)
'
## Trabalhando com arquivos

- `git add .`  
  Adiciona **todos os arquivos modificados** ao repositório local.  
  ⚠️ **Não usar sempre**, pois pode adicionar arquivos desnecessários.

- `git add caminho/do/arquivo`  
  Adiciona um arquivo específico ao repositório local.  
  ✅ **Sempre preferível** para controlar melhor o que vai commitar.

- `git commit -m 'mensagem'`  
  Salva as alterações adicionadas ao repositório local na branch atual com uma mensagem descritiva.

## Branches

- `git branch`  
  Mostra a **branch atual** e todas as branches existentes.

- `git checkout -b NomeDaBranch`  
  Cria uma **nova branch** e já troca para ela.

- `git checkout NomeDaBranch`  
  Troca para a branch especificada.

- `git branch -D NomeDaBranch`  
  Deleta uma branch **forçadamente**.

- `git branch -m NomeDoRepositorioOriginal NomeQueEuQuero`  
  Renomeia a branch atual.

## Status e atualizações

- `git status`  
  Mostra quais arquivos foram alterados, quais estão staged para commit e quais não estão.

- `git push origin NomeDaBranch`  
  Envia as alterações da branch local para o repositório remoto (GitHub).

- `git pull origin NomeDaBranch`  
  Puxa as alterações do repositório remoto para o repositório local.

## Inicializando repositórios

- `git init`  
  Inicializa um repositório Git local.  
  Depois é necessário usar `git add` e `git commit` para registrar as primeiras alterações.

- `git remote add origin LinkDoGithub`  
  Conecta o repositório local a um remoto no GitHub usando o link do repositório.
