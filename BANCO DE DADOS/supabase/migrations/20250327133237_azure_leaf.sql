-- Import data from operadoras CSV
COPY operadoras FROM '/data/operadoras_ativas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);

-- Import data from demonstracoes contabeis
-- Note: This is a template, actual file names will need to be specified
COPY demonstracoes_contabeis FROM '/data/demonstracoes_{YEAR}_{QUARTER}.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);