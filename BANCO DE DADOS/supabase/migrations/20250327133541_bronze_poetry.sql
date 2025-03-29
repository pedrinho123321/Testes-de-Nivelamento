-- Importação dos dados das operadoras
COPY operadoras FROM '/data/operadoras_ativas.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);

-- Importação dos dados das demonstrações contábeis
-- Nota: Este é um template, os nomes dos arquivos precisarão ser especificados
COPY demonstracoes_contabeis FROM '/data/demonstracoes_{ANO}_{TRIMESTRE}.csv'
WITH (
    FORMAT csv,
    HEADER true,
    DELIMITER ';',
    ENCODING 'UTF8'
);