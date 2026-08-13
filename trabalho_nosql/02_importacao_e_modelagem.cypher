// QUESTÃO 01 — Parte I — Importação e modelagem do grafo — RU 5454601
// Pré-requisitos antes de rodar:
//   1. apoc.conf na pasta conf/ do DBMS com: apoc.import.file.enabled=true
//   2. 3 a 10 arquivos .json copiados para a pasta import/ do DBMS
//   3. DBMS reiniciado após adicionar o apoc.conf
// Observação: usamos a lista de arquivos manualmente (em vez de apoc.load.directory)
// porque essa função pertence ao APOC Extended, que não vem instalado por padrão.

// ---------------------------------------------------------------
// PASSO 1 — Importar os tweets e montar Tweet, User e Hashtag
// ---------------------------------------------------------------
UNWIND [
  "tweets_coletados_154.json",
  "tweets_coletados_155.json",
  "tweets_coletados_156.json",
  "tweets_coletados_157.json",
  "tweets_coletados_158.json"
] AS arquivo_ru5454601
CALL apoc.load.json(arquivo_ru5454601) YIELD value AS pacote_ru5454601
UNWIND pacote_ru5454601.data AS tweet_ru5454601

MERGE (t:Tweet {id: tweet_ru5454601.id})
SET t.text = tweet_ru5454601.text,
    t.created_at = tweet_ru5454601.created_at,
    t.conversation_id = tweet_ru5454601.conversation_id,
    t.tipo_ref = coalesce(tweet_ru5454601.referenced_tweets[0].type, "original"),
    t.id_ref = tweet_ru5454601.referenced_tweets[0].id

MERGE (u:User {id: tweet_ru5454601.author_id})
MERGE (u)-[:TUITOU]->(t)

WITH t, tweet_ru5454601
UNWIND coalesce(tweet_ru5454601.entities.hashtags, [{tag: null}]) AS hashtag_ru5454601
WITH t, hashtag_ru5454601
WHERE hashtag_ru5454601.tag IS NOT NULL
WITH t, apoc.text.replace(apoc.text.clean(hashtag_ru5454601.tag), '[^a-zA-Z0-9]', '') AS hashtag_limpa_ru5454601
MERGE (h:Hashtag {text: hashtag_limpa_ru5454601})
MERGE (t)-[:POSSUI]->(h);

// ---------------------------------------------------------------
// PASSO 2 — Reclassificar Tweets que são respostas/retweets/citações
// (executar um de cada vez, depois do PASSO 1 terminar)
// ---------------------------------------------------------------

// Retweets
MATCH (t:Tweet)
WHERE t.tipo_ref = "retweeted"
REMOVE t:Tweet
SET t:Retweet;

// Respostas
MATCH (t:Tweet)
WHERE t.tipo_ref = "replied_to"
REMOVE t:Tweet
SET t:Resposta;

// Citações
MATCH (t:Tweet)
WHERE t.tipo_ref = "quoted"
REMOVE t:Tweet
SET t:Citacao;

// ---------------------------------------------------------------
// PASSO 3 — Nó de identificação pessoal (RU)
// ---------------------------------------------------------------
MERGE (ru5454601:RU {RU: "RU-5454601"});
