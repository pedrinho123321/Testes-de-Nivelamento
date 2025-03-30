COPY operadoras FROM '/data/operadoras_ativas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);

COPY demonstracoes_contabeis FROM '/data/demonstracoes_{YEAR}_{QUARTER}.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);
