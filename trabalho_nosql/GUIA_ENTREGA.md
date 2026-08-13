# Guia de Entrega — Atividade Prática NoSQL (RU 5454601)

Todos os scripts Cypher já estão prontos nesta pasta, com o seu RU embutido nos nomes de
variável (ex.: `tweet_ru5454601`, `qtd_tweets_ru5454601`). Siga a ordem abaixo.

## 1. Preparar o ambiente Neo4j

1. No Neo4j Desktop, confirme que o DBMS está na versão **4.x** (não 5.x).
2. Confirme que o plugin **APOC** está instalado nesse DBMS (aba Plugins).
3. Abra a pasta do DBMS (`...` → *Open folder* → *DBMS*):
   - Copie o arquivo [01_apoc.conf](01_apoc.conf) para a subpasta `conf/`, renomeando para `apoc.conf` (se já existir um `apoc.conf`, apenas adicione a linha `apoc.import.file.enabled=true` nele).
   - Copie de 3 a 10 dos 547 arquivos `.json` para a subpasta `import/`.
4. Reinicie o DBMS para que o `apoc.conf` seja lido.
5. Abra o Neo4j Browser desse DBMS.

## 2. Questão 01 — Importação e modelagem

1. No Neo4j Browser, execute o **PASSO 1** de [02_importacao_e_modelagem.cypher](02_importacao_e_modelagem.cypher) (o bloco que termina em `MERGE (t)-[:POSSUI]->(h);`).
2. Quando terminar, execute o **PASSO 2** (as 3 consultas de reclassificação: Retweet, Resposta, Citação) — uma de cada vez.
3. Execute o **PASSO 3** (`MERGE (ru5454601:RU ...)`).
4. **Print da Parte I**: tire print do código de **todos os 5 comandos** (PASSO 1 + as 3 reclassificações + PASSO 3), não só do PASSO 1 — o exemplo do professor mostra todos juntos (Figura 1 do gabarito). Use o ícone de expandir (⤢) na barra de comando do Browser antes do print, para a query aparecer completa, sem cortar com "...".
5. **Print da Parte II**: tire print das **barras de sucesso** geradas ao rodar os 5 comandos acima (PASSO 1, as 3 reclassificações e o PASSO 3) — ex.: "Added 1060 labels, created 1060 nodes, set 3529 properties, created 1132 relationships...". **Não use `03_questao1_resultado.cypher` para isso** — aquele arquivo usa `RETURN` para montar uma tabela, e o roteiro é explícito: *"não mostrar nenhum grafo nesta parte, apenas as telas de execução dos comandos da parte I. O uso de RETURN zerará a nota desta parte."* `03_questao1_resultado.cypher` é só uma conferência pessoal de sanidade, não vai no caderno de resposta.

## 3. Questão 02 — Hashtag principal

1. Execute [04_questao2_hashtag_principal.cypher](04_questao2_hashtag_principal.cypher) no Browser.
2. Anote a palavra retornada em `hashtag_principal_ru5454601` — essa é a resposta da Parte III.
3. Abra [05_questao2_grafo.cypher](05_questao2_grafo.cypher), troque `SUBSTITUA_PELA_HASHTAG` pela palavra encontrada, e execute.
4. No painel de visualização, **desative o zoom automático** (visualize em 100%), confirme que a legenda de tipos de nó (cores) está visível, e que dá para contar entre 10 e 20 nós, incluindo o nó `RU`. Ajuste o `LIMIT` da query se precisar de mais ou menos nós.
5. **Print da Parte I**: código e resultado do **passo 1** (`04_questao2_hashtag_principal.cypher`, a query com a subquery `CALL{}` que descobre a hashtag — é o comando que o roteiro pede, com "ao menos uma dupla MATCH/RETURN"). Não use a query do grafo aqui: ela só exibe a hashtag já descoberta, não mostra a descoberta em si.
6. **Print da Parte II**: o grafo gerado pelo **passo 3** (`05_questao2_grafo.cypher`), com legenda.
7. **Parte III**: escreva a palavra da hashtag (texto, não print).

⚠️ Nunca use `MATCH (n) RETURN n;` como comando final — é vedado pelo roteiro.

## 4. Questão 03 — Análise livre

Tema escolhido: **hashtags secundárias mais usadas junto com a hashtag principal**, em
[06_questao3_hashtags_secundarias.cypher](06_questao3_hashtags_secundarias.cypher) — quais outras hashtags
aparecem nos mesmos tweets que usam `issoaglobonaomostra`. O arquivo também guarda, comentadas, duas
alternativas descartadas (usuário mais ativo: só deu 7 nós na amostra de 5 arquivos, abaixo do mínimo de 10;
usuários mais mencionados em conversas).

1. Execute a query da Parte I.
2. Confira no Browser se o grafo tem entre 10 e 200 nós (ajuste o `LIMIT` se precisar).
3. **Print da Parte I**: o código da query.
4. **Print da Parte II**: o grafo, com uma legenda/caption explicando o que ele mostra (ex.: "Hashtag principal issoaglobonaomostra, os N tweets que a usam e as hashtags secundárias compartilhadas entre eles, incluindo o nó RU-5454601").
5. **Parte III** (texto): escreva
   - por que você escolheu essa pergunta,
   - o que você esperava encontrar antes de rodar a query,
   - o que de fato encontrou, e se confirmou ou não sua expectativa.

⚠️ Mesmo aviso: não use `MATCH (n) RETURN n;`.

## 4.1 Respostas finais confirmadas

- **Questão 02 — hashtag principal**: `issoaglobonaomostra`
- **Questão 03 — tema escolhido**: hashtags secundárias mais usadas junto com a hashtag principal.
  Resultado confirmado (rodado em 2026-06-30): **54 nós** — 38 Hashtag (1 principal + 37 secundárias),
  15 Tweet, 1 RU — e **57 relações** `POSSUI`, em um único componente conectado (o nó RU fica solto,
  como no exemplo do professor).
- **Questão 03 — texto da Parte III** (versão final):

  > Escolhi investigar quais hashtags secundárias são mais usadas em conjunto com a hashtag principal (issoaglobonaomostra), para entender o contexto temático ao redor do assunto que originou a coleta dos tweets. Minha expectativa era encontrar um pequeno grupo de hashtags recorrentes, repetidas em vários tweets diferentes, formando um tema secundário comum. O resultado obtido foi um grafo único e conectado com 54 nós, no qual a hashtag principal está ligada a 15 tweets, que juntos compartilham 37 hashtags secundárias distintas, totalizando 57 relações POSSUI. O resultado **não confirmou** minha expectativa inicial: ao invés de um pequeno grupo de hashtags recorrentes, encontrei uma grande variedade de hashtags secundárias usadas quase sempre uma única vez cada (37 hashtags distintas para apenas 42 ocorrências entre os 15 tweets) — ou seja, cada tweet tende a usar seu próprio conjunto de hashtags extras, pouco compartilhado com os demais, em vez de reforçar um tema secundário único e comum a todos.

## 5. Montagem do caderno de resposta (PDF final)

Para cada questão, na ordem: **print do código → print do resultado/grafo com legenda → (Q2/Q3) resposta em texto**.

Checklist antes de exportar:
- [ ] RU-5454601 aparece em TODA imagem (como nó no grafo, ou na query visível no print da Questão 01).
- [ ] Questão 01 Parte I mostra os 5 comandos (import + 3 reclassificações + RU), não só o PASSO 1, com a query expandida (sem "...").
- [ ] RU aparece como parte de nome de variável em TODO código (já garantido nos scripts: `ru5454601`).
- [ ] Questão 01 Parte II são as barras de sucesso da execução (sem grafo, sem tabela, sem RETURN).
- [ ] Questão 02 tem grafo com 10–20 nós, centrado na hashtag, com legenda visível, sem zoom.
- [ ] Questão 03 tem grafo com 10–200 nós.
- [ ] Nenhuma questão usa `MATCH (n) RETURN n;`.
- [ ] Exportar como **PDF** (não .doc/.docx).

Quando tiver os prints, me avise — posso revisar a estrutura do documento final com você antes de exportar.
