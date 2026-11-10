USE dados_cafe

--- TOP 10 (Arábica)
SELECT TOP 10 ranking_global, species, country_of_origin, variety,
processing_method, aroma, flavor, aftertaste, acidity, body, balance, uniformity,
clean_cup, sweetness, cupper_points, total_cup_points, altitude_mean_meters
FROM arabica
ORDER BY ranking_global ASC

--- TOP 10 Brasileiros (Arábica)
SELECT TOP 10 ranking_global, species, country_of_origin, region, producer, variety,
processing_method, aroma, flavor, aftertaste, acidity, body, balance, uniformity,
clean_cup, sweetness, cupper_points, total_cup_points, altitude_mean_meters
FROM arabica
WHERE country_of_origin = 'brazil'
ORDER BY ranking_global ASC

--- Média de Pontuação por País (Arábica)
SELECT country_of_origin, AVG(total_cup_points) as 'media_pontos', 
MAX(total_cup_points) as 'maior_pontuacao', COUNT(*) as 'total_lotes'
FROM arabica
GROUP BY country_of_origin
HAVING COUNT (*) >= 20
ORDER BY AVG(total_cup_points) DESC

--- O Melhor Café de Cada País (Arábica)
SELECT country_of_origin, MAX(total_cup_points) AS 'maior_pontuação'
FROM arabica
GROUP BY country_of_origin 
ORDER BY MAX(total_cup_points) DESC

--- Os 10 Países Com o Maior Número Total de Sacas (Arábica)
SELECT TOP 10 country_of_origin, SUM(number_of_bags) AS 'total_de_sacas'
FROM arabica
GROUP BY country_of_origin
ORDER BY SUM(number_of_bags) DESC

--- Impacto do Processamento (Arábica)
SELECT processing_method, MAX(total_cup_points) AS 'pontuacao_maxima', 
AVG(total_cup_points) AS 'pontuacao_media',COUNT(*) AS 'total_lotes'
FROM arabica
WHERE processing_method IS NOT NULL
GROUP BY processing_method
ORDER BY pontuacao_maxima DESC

--- Impacto da Altitude (Arábica)
SELECT altitude_mean_meters, MAX(total_cup_points) AS 'pontuacao_maxima', 
AVG(total_cup_points) AS 'pontuacao_media',COUNT(*) AS 'total_lotes'
FROM arabica
WHERE altitude_mean_meters IS NOT NULL
GROUP BY altitude_mean_meters
ORDER BY pontuacao_media DESC

--- Arábica x Robusta
SELECT species, MAX(total_cup_points) AS 'pontuacao_maxima',
AVG(total_cup_points) AS 'pontuacao_media', COUNT(*) AS 'total_lotes'
FROM arabica
GROUP BY species
UNION ALL
SELECT species, MAX(total_cup_points) AS 'pontuacao_maxima',
AVG(total_cup_points) AS 'pontuacao_media', COUNT(*) AS 'total_lotes'
FROM robusta
GROUP BY species

--- Notas (Robusta)
SELECT ranking_global, species, country_of_origin, processing_method, fragrance_aroma, 
flavor, aftertaste, salt_acid, bitter_sweet, mouthfeel, uniform_cup, clean_cup, balance,
cupper_points, total_cup_points
FROM robusta

--- Média de Pontuação por País e Número Total de Sacas (Robusta)
SELECT country_of_origin, AVG(total_cup_points) as 'media_pontos', MAX(total_cup_points) as 'maior_pontuacao', 
COUNT(*) as 'total_lotes', SUM(number_of_bags) AS 'total_de_sacas'
FROM robusta
GROUP BY country_of_origin
ORDER BY AVG(total_cup_points) DESC