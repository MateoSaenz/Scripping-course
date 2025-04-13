USE ratings;
(SELECT 'name', 'rating', 'region' FROM ratings)
UNION
SELECT * FROM ratings
INTO OUTFILE 'C:/Users/mateo/OneDrive/Documentos/Educación externa/Scripping-course/Fourth_module/sql_scripts/table.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
