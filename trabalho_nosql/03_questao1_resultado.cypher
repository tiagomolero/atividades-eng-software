// ⚠️ NÃO USAR NO CADERNO DE RESPOSTA — este script usa RETURN, e o roteiro é explícito:
// "O uso de RETURN zerará a nota desta parte" para a Questão 01 Parte II.
// Serve só como conferência pessoal (somatório do que foi importado). A Parte II oficial
// são os prints das barras de sucesso ao rodar 02_importacao_e_modelagem.cypher.
// QUESTÃO 01 — conferência pessoal (NÃO é grafo, é tabela de texto) — RU 5454601

OPTIONAL MATCH (t:Tweet)
WITH count(t) AS qtd_tweets_ru5454601
OPTIONAL MATCH (rt:Retweet)
WITH qtd_tweets_ru5454601, count(rt) AS qtd_retweets_ru5454601
OPTIONAL MATCH (rp:Resposta)
WITH qtd_tweets_ru5454601, qtd_retweets_ru5454601, count(rp) AS qtd_respostas_ru5454601
OPTIONAL MATCH (cit:Citacao)
WITH qtd_tweets_ru5454601, qtd_retweets_ru5454601, qtd_respostas_ru5454601, count(cit) AS qtd_citacoes_ru5454601
OPTIONAL MATCH (u:User)
WITH qtd_tweets_ru5454601, qtd_retweets_ru5454601, qtd_respostas_ru5454601, qtd_citacoes_ru5454601, count(u) AS qtd_usuarios_ru5454601
OPTIONAL MATCH (h:Hashtag)
WITH qtd_tweets_ru5454601, qtd_retweets_ru5454601, qtd_respostas_ru5454601, qtd_citacoes_ru5454601, qtd_usuarios_ru5454601, count(h) AS qtd_hashtags_ru5454601
MATCH (ru5454601:RU {RU: "RU-5454601"})
RETURN ru5454601.RU AS identificacao,
       qtd_tweets_ru5454601 AS tweets_originais,
       qtd_retweets_ru5454601 AS retweets,
       qtd_respostas_ru5454601 AS respostas,
       qtd_citacoes_ru5454601 AS citacoes,
       qtd_usuarios_ru5454601 AS usuarios,
       qtd_hashtags_ru5454601 AS hashtags;
