// QUESTÃO 02 — Parte II — Grafo centrado na hashtag principal (10 a 20 nós, com o nó RU) — RU 5454601
// Antes de rodar: troque SUBSTITUA_PELA_HASHTAG pelo valor encontrado no script 04.
// Ajuste o LIMIT se o grafo ficar com menos de 10 ou mais de 20 nós.
// Lembrete: NÃO use "MATCH (n) RETURN n" — é proibido como comando final.
// Lembrete: na visualização, deixe a legenda dos tipos de nó visível e sem zoom.

MATCH (h:Hashtag)<-[:POSSUI]-(t:Tweet)
WHERE h.text = "issoaglobonaomostra"
WITH h, t
LIMIT 12
WITH h, collect(t) AS tweets_ru5454601
MATCH (ru5454601:RU {RU: "RU-5454601"})
RETURN h, tweets_ru5454601, ru5454601;
