COPY operadoras FROM '/data/operadoras_ativas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);

COPY demonstracoes_contabeis FROM '/data/demonstracoes_{ANO}_{TRIMESTRE}.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);
