# Usando o Git Branch

## Instruções

1. Crie um ramo novo com nome `ramo1` usando `git branch ramo1`
2. Mude a _HEAD_ (versão ativa) para o `ramo1` com `git checkout ramo1`
3. Crie um arquivo texto chamado `resolução1.md` com conteúdo `Esse aquivo só pertence ao ramo1`
4. Adicione ele aos arquivos rastreados e faça um commit com mensagem `Arquivo resolução1 adicionado`
5. Faça um _push_ para o GitHub :octocat: `git push -u origin ramo1`
   - Esse comando faz duas coisas ao mesmo tempo.
   - Faz com que o `ramo1` local do seu computador seja atrelado ao `ramo1` do servidor remoto chamado `origin` que é o servidor do GitHub.
   - Empurra todas as modificações para o servidor do GitHub
   - Depois de atrelar, toda modificação futura dentro do `ramo1` pode ser empurrada para o servidor simplesmente com o `git push`
6. Mude a _HEAD_ para o ramo `main` (o principal/padrão) com `git checkout main`
7. Verifique que o arquivo `resolução1.md` não está mais no diretório.
8. Crie um ramo novo chamado `ramo2` e mude a _HEAD_ para ele em um comando só `git checkout -b ramo2` é uma versão resumida de fazer `git branch ramo2` e depois `git checkout ramo2`.
9. Adicione o arquivo texto `resolução2.md` com conteúdo `Esse arquivo só pertence ao ramo2`
10. Adicione ele aos arquivos rastreados e faça um commit com mensagem `Arquivo resolução2 adicionado`
11. Faça um _push_ para o GitHub :octocat: `git push -u origin ramo2`
12. Volte a _HEAD_ para o main com `git checkout main`.
13. Abra uma issue no github com título _Exercício Concluído_ e adicione o professor da disciplina como responsável.

No final você deverá ter três ramos diferentes o `ramo1` com o arquivo `resolução1.md`, o `ramo2` com o arquivo `resolução2.md` e o `main` sem esses dois arquivos.
