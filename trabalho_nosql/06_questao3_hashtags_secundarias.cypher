// QUESTÃO 03 — Análise livre escolhida: HASHTAGS SECUNDÁRIAS MAIS USADAS JUNTO COM A HASHTAG PRINCIPAL — RU 5454601
// Pergunta: quais outras hashtags aparecem com mais frequência nos mesmos tweets que usam "issoaglobonaomostra"?
// Regras: pode usar MERGE/CREATE sobre os dados já importados, mas NÃO pode ler JSON nem usar APOC.
// Grafo final deve ter 10 ou mais nós interligados entre si (não pode ser vários grupos desconectados).
// Lembrete: NÃO use "MATCH (n) RETURN n" — é proibido como comando final.

// Parte I — código/consulta
MATCH (h:Hashtag {text: "issoaglobonaomostra"})<-[:POSSUI]-(t:Tweet)
WITH h, t
LIMIT 15
OPTIONAL MATCH (t)-[:POSSUI]->(h2:Hashtag)
WHERE h2.text <> "issoaglobonaomostra"
WITH h, collect(DISTINCT t) AS tweets_ru5454601, collect(DISTINCT h2) AS hashtags_secundarias_ru5454601
MATCH (ru5454601:RU {RU: "RU-5454601"})
RETURN h, tweets_ru5454601, hashtags_secundarias_ru5454601, ru5454601;

// ---------------------------------------------------------------
// ALTERNATIVAS DESCARTADAS (mantidas só de referência):
// ---------------------------------------------------------------

// Opção A — Usuário mais ativo (testada: deu só 7 nós com a amostra de 5 arquivos, abaixo do mínimo de 10)
// MATCH (u:User)-[:TUITOU]->(t:Tweet)
// WITH u, count(t) AS qtd_tweets_ru5454601
// ORDER BY qtd_tweets_ru5454601 DESC
// LIMIT 1
// MATCH (u)-[:TUITOU]->(t:Tweet)
// OPTIONAL MATCH (t)-[:POSSUI]->(h:Hashtag)
// WITH u, collect(DISTINCT t) AS tweets_ru5454601, collect(DISTINCT h) AS hashtags_ru5454601
// LIMIT 1
// MATCH (ru5454601:RU {RU: "RU-5454601"})
// RETURN u, tweets_ru5454601, hashtags_ru5454601, ru5454601;

// Opção C — Usuários mais mencionados em conversas (mesma conversation_id de muitos tweets)
// MATCH (t1:Tweet)
// WITH t1.conversation_id AS conversa_ru5454601, count(t1) AS qtd_ru5454601
// ORDER BY qtd_ru5454601 DESC
// LIMIT 1
// MATCH (t:Tweet {conversation_id: conversa_ru5454601})<-[:TUITOU]-(u:User)
// WITH collect(t) AS tweets_ru5454601, collect(u) AS usuarios_ru5454601
// MATCH (ru5454601:RU {RU: "RU-5454601"})
// RETURN tweets_ru5454601, usuarios_ru5454601, ru5454601;
