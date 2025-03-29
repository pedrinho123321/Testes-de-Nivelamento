-- Create table for operadoras ativas
CREATE TABLE operadoras (
    registro_ans VARCHAR(20) PRIMARY KEY,
    cnpj VARCHAR(14),
    razao_social VARCHAR(255),
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    logradouro VARCHAR(255),
    numero VARCHAR(20),
    complemento VARCHAR(100),
    bairro VARCHAR(100),
    cidade VARCHAR(100),
    uf VARCHAR(2),
    cep VARCHAR(8),
    ddd VARCHAR(2),
    telefone VARCHAR(20),
    fax VARCHAR(20),
    email VARCHAR(100),
    representante VARCHAR(255),
    cargo_representante VARCHAR(100),
    data_registro_ans DATE
);

-- Create table for demonstracoes contabeis
CREATE TABLE demonstracoes_contabeis (
    registro_ans VARCHAR(20),
    data_trimestre DATE,
    codigo_conta VARCHAR(20),
    descricao_conta VARCHAR(255),
    valor_conta DECIMAL(15,2),
    PRIMARY KEY (registro_ans, data_trimestre, codigo_conta),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);

-- Create index for better query performance
CREATE INDEX idx_demonstracoes_data ON demonstracoes_contabeis(data_trimestre);
CREATE INDEX idx_demonstracoes_conta ON demonstracoes_contabeis(codigo_conta);