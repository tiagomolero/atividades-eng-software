// QUESTÃO 02 — Parte I — Descobrir a hashtag presente em TODOS os Tweets originais — RU 5454601
// Regras: sem APOC, sem ler JSON — só consulta o grafo já criado.
// Só considera nós :Tweet (Retweet/Resposta/Citacao já perderam esse rótulo no passo de reclassificação).

// Subquery (MATCH + RETURN próprios): pega as hashtags de 1 tweet original como candidatas
CALL {
  MATCH (t0:Tweet)
  WITH t0 LIMIT 1
  MATCH (t0)-[:POSSUI]->(h0:Hashtag)
  RETURN collect(h0.text) AS candidatas_ru5454601
}
UNWIND candidatas_ru5454601 AS candidata_ru5454601
// Para cada candidata, confere se ela está em TODOS os tweets originais
MATCH (t:Tweet)
OPTIONAL MATCH (t)-[:POSSUI]->(h:Hashtag {text: candidata_ru5454601})
WITH candidata_ru5454601, count(t) AS total_tweets_ru5454601, count(h) AS tweets_com_essa_hashtag_ru5454601
WHERE total_tweets_ru5454601 = tweets_com_essa_hashtag_ru5454601
RETURN candidata_ru5454601 AS hashtag_principal_ru5454601;

// Anote o valor retornado: é a resposta de uma palavra da Questão 02 (Parte III).
// Substitua "SUBSTITUA_PELA_HASHTAG" no arquivo 05_questao2_grafo.cypher por esse valor.
