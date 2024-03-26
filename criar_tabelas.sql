CREATE TABLE IF NOT EXISTS empresas (
    cnpj_basico VARCHAR(8),
    razao_social VARCHAR(255),
    natureza_juridica VARCHAR(4),
    qualificacao_do_responsavel VARCHAR(2),
    capital_social_da_empresa VARCHAR(20),
    porte_da_empresa VARCHAR(2),
    ente_federativo_responsavel VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS estabelecimentos (
    cnpj_basico VARCHAR(8),
    cnpj_ordem VARCHAR(4),
    cnpj_dv VARCHAR(2),
    identificador_matriz_filial VARCHAR(1),
    nome_fantasia VARCHAR(100),
    situacao_cadastral VARCHAR(2),
    data_situacao_cadastral VARCHAR(8),
    motivo_situacao_cadastral VARCHAR(2),
    nome_da_cidade_no_exterior VARCHAR(60),
    pais VARCHAR(3),
    data_de_inicio_atividade VARCHAR(8),
    cnae_fiscal_principal VARCHAR(7),
    cnae_fiscal_secundaria VARCHAR(1000),
    tipo_de_logradouro VARCHAR(20),
    logradouro VARCHAR(255),
    numero VARCHAR(10),
    complemento VARCHAR(255),
    bairro VARCHAR(255),
    cep VARCHAR(8),
    uf VARCHAR(2),
    municipio VARCHAR(4),
    ddd_1 VARCHAR(4),
    telefone_1 VARCHAR(9),
    ddd_2 VARCHAR(4),
    telefone_2 VARCHAR(9),
    ddd_do_fax VARCHAR(4),
    fax VARCHAR(9),
    correio_eletronico VARCHAR(255),
    situacao_especial VARCHAR(255),
    data_da_situacao_especial VARCHAR(8)
);
CREATE TABLE IF NOT EXISTS simples (
    cnpj_basico VARCHAR(8),
    opcao_pelo_simples VARCHAR(1),
    data_de_opcao_pelo_simples VARCHAR(8),
    data_de_exclusao_do_simples VARCHAR(8),
    opcao_pelo_mei VARCHAR(1),
    data_de_opcao_pelo_mei VARCHAR(8),
    data_de_exclusao_do_mei VARCHAR(8)
);
CREATE TABLE IF NOT EXISTS socios (
    cnpj_basico VARCHAR(8),
    identificador_de_socio VARCHAR(1),
    nome_do_socio_razao_social VARCHAR(255),
    cnpj_cpf_do_socio VARCHAR(14),
    qualificacao_do_socio VARCHAR(2),
    data_de_entrada_sociedade VARCHAR(8),
    pais VARCHAR(3),
    representante_legal VARCHAR(11),
    nome_do_representante VARCHAR(255),
    qualificacao_do_representante_legal VARCHAR(2),
    faixa_etaria VARCHAR(1)
);
CREATE TABLE IF NOT EXISTS cnaes (
    codigo VARCHAR(7),
    descricao VARCHAR(200)
);
CREATE TABLE IF NOT EXISTS motivos (
    codigo VARCHAR(2),
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS municipios (
    codigo VARCHAR(4),
    descricao VARCHAR(40)
);
CREATE TABLE IF NOT EXISTS naturezas (
    codigo VARCHAR(4),
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS paises (
    codigo VARCHAR(3),
    descricao VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS qualificacoes (
    codigo VARCHAR(2),
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS porte_empresa (
    codigo VARCHAR(2),
    descricao VARCHAR(30)
);
INSERT INTO porte_empresa (codigo, descricao) VALUES
('00', 'NÃO INFORMADO'),
('01', 'MICRO EMPRESA'),
('03', 'EMPRESA DE PEQUENO PORTE'),
('05', 'DEMAIS');
CREATE TABLE IF NOT EXISTS matriz_filial (
    codigo VARCHAR(1),
    descricao VARCHAR(10)
);
INSERT INTO matriz_filial (codigo, descricao) VALUES
('1', 'MATRIZ'),
('2', 'FILIAL');
CREATE TABLE IF NOT EXISTS situacao_cadastral (
    codigo VARCHAR(2),
    descricao VARCHAR(10)
);
INSERT INTO situacao_cadastral (codigo, descricao) VALUES
('01', 'NULA'),
('2', 'ATIVA'),
('3', 'SUSPENSA'),
('4', 'INAPTA'),
('08', 'BAIXADA');
CREATE TABLE IF NOT EXISTS identificacao_socio (
    codigo VARCHAR(1),
    descricao VARCHAR(20)
);
INSERT INTO identificacao_socio (codigo, descricao) VALUES
('1', 'PESSOA JURÍDICA'),
('2', 'PESSOA FÍSICA'),
('3', 'ESTRANGEIRO');
CREATE TABLE IF NOT EXISTS faixa_etaria (
    codigo VARCHAR(2),
    descricao VARCHAR(20)
);
INSERT INTO faixa_etaria (codigo, descricao) VALUES
('1', '0-12'),
('2', '13-20'),
('3', '21-30'),
('4', '31-40'),
('5', '41-50'),
('6', '51-60'),
('7', '61-70'),
('8', '71-80'),
('9', '+80'),
('0', 'não se aplica');