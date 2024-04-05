CREATE TABLE IF NOT EXISTS Empresas (
    cnpj_basico VARCHAR(8),
    razao_social VARCHAR(255),
    natureza_juridica VARCHAR(4),
    qualificacao_do_responsavel VARCHAR(2),
    capital_social_da_empresa VARCHAR(20),
    porte_da_empresa SMALLINT,
    ente_federativo_responsavel VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS Estabelecimentos (
    cnpj_basico VARCHAR(8),
    cnpj_ordem VARCHAR(4),
    cnpj_dv VARCHAR(2),
    identificador_matriz_filial SMALLINT,
    nome_fantasia VARCHAR(100),
    situacao_cadastral SMALLINT,
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
CREATE TABLE IF NOT EXISTS Simples (
    cnpj_basico VARCHAR(8),
    opcao_pelo_simples VARCHAR(1),
    data_de_opcao_pelo_simples VARCHAR(8),
    data_de_exclusao_do_simples VARCHAR(8),
    opcao_pelo_mei VARCHAR(1),
    data_de_opcao_pelo_mei VARCHAR(8),
    data_de_exclusao_do_mei VARCHAR(8)
);
CREATE TABLE IF NOT EXISTS Socios (
    cnpj_basico VARCHAR(8),
    identificador_de_socio SMALLINT,
    nome_do_socio_razao_social VARCHAR(255),
    cnpj_cpf_do_socio VARCHAR(14),
    qualificacao_do_socio VARCHAR(2),
    data_de_entrada_sociedade VARCHAR(8),
    pais VARCHAR(3),
    representante_legal VARCHAR(11),
    nome_do_representante VARCHAR(255),
    qualificacao_do_representante_legal VARCHAR(2),
    faixa_etaria SMALLINT
);
CREATE TABLE IF NOT EXISTS Cnaes (
    codigo VARCHAR(7) NOT NULL PRIMARY KEY,
    descricao VARCHAR(200)
);
CREATE TABLE IF NOT EXISTS Motivos (
    codigo VARCHAR(2) NOT NULL PRIMARY KEY,
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS Municipios (
    codigo VARCHAR(4) NOT NULL PRIMARY KEY,
    descricao VARCHAR(40)
);
CREATE TABLE IF NOT EXISTS Naturezas (
    codigo VARCHAR(4) NOT NULL PRIMARY KEY,
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS Paises (
    codigo VARCHAR(3) NOT NULL PRIMARY KEY,
    descricao VARCHAR(50)
);
CREATE TABLE IF NOT EXISTS Qualificacoes (
    codigo VARCHAR(2) NOT NULL PRIMARY KEY,
    descricao VARCHAR(100)
);
CREATE TABLE IF NOT EXISTS PorteEmpresa (
    codigo SMALLINT NOT NULL PRIMARY KEY,
    descricao VARCHAR(30)
);
INSERT INTO PorteEmpresa (codigo, descricao) VALUES
(0, 'NÃO INFORMADO'),
(1, 'MICRO EMPRESA'),
(3, 'EMPRESA DE PEQUENO PORTE'),
(5, 'DEMAIS');
CREATE TABLE IF NOT EXISTS MatrizFilial (
    codigo SMALLINT NOT NULL PRIMARY KEY,
    descricao VARCHAR(10)
);
INSERT INTO MatrizFilial (codigo, descricao) VALUES
(1, 'MATRIZ'),
(2, 'FILIAL');
CREATE TABLE IF NOT EXISTS SituacaoCadastral (
    codigo SMALLINT NOT NULL PRIMARY KEY,
    descricao VARCHAR(10)
);
INSERT INTO SituacaoCadastral (codigo, descricao) VALUES
(1, 'NULA'),
(2, 'ATIVA'),
(3, 'SUSPENSA'),
(4, 'INAPTA'),
(8, 'BAIXADA');
CREATE TABLE IF NOT EXISTS IdentificacaoSocio (
    codigo SMALLINT NOT NULL PRIMARY KEY,
    descricao VARCHAR(20)
);
INSERT INTO IdentificacaoSocio (codigo, descricao) VALUES
(1, 'PESSOA JURÍDICA'),
(2, 'PESSOA FÍSICA'),
(3, 'ESTRANGEIRO');
CREATE TABLE IF NOT EXISTS FaixaEtaria (
    codigo SMALLINT NOT NULL PRIMARY KEY,
    descricao VARCHAR(20)
);
INSERT INTO FaixaEtaria (codigo, descricao) VALUES
(1, '0-12'),
(2, '13-20'),
(3, '21-30'),
(4, '31-40'),
(5, '41-50'),
(6, '51-60'),
(7, '61-70'),
(8, '71-80'),
(9, '+80'),
(0, 'NÃO SE APLICA');
CREATE TABLE IF NOT EXISTS HashArquivos (
    nome VARCHAR(30) NOT NULL,
    hash VARCHAR(64) NOT NULL,
    ultima_modificacao TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
ALTER TABLE Empresas ADD CONSTRAINT fk_natureza_juridica FOREIGN KEY (natureza_juridica) REFERENCES Naturezas(codigo);
ALTER TABLE Empresas ADD CONSTRAINT fk_porte_da_empresa FOREIGN KEY (porte_da_empresa) REFERENCES PorteEmpresa(codigo);
ALTER TABLE Empresas ADD CONSTRAINT fk_qualificacao_do_responsavel FOREIGN KEY (qualificacao_do_responsavel) REFERENCES Qualificacoes(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_identificador_matriz_filial FOREIGN KEY (identificador_matriz_filial) REFERENCES MatrizFilial(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_situacao_cadastral FOREIGN KEY (situacao_cadastral) REFERENCES SituacaoCadastral(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_motivo_situacao_cadastral FOREIGN KEY (motivo_situacao_cadastral) REFERENCES Motivos(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_pais FOREIGN KEY (pais) REFERENCES Paises(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_cnae_fiscal_principal FOREIGN KEY (cnae_fiscal_principal) REFERENCES Cnaes(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_cnae_fiscal_secundaria FOREIGN KEY (cnae_fiscal_secundaria) REFERENCES Cnaes(codigo);
ALTER TABLE Estabelecimentos ADD CONSTRAINT fk_municipio FOREIGN KEY (municipio) REFERENCES Municipios(codigo);
ALTER TABLE Socios ADD CONSTRAINT fk_identificador_de_socio FOREIGN KEY (identificador_de_socio) REFERENCES IdentificacaoSocio(codigo);
ALTER TABLE Socios ADD CONSTRAINT fk_qualificacao_do_socio FOREIGN KEY (qualificacao_do_socio) REFERENCES Qualificacoes(codigo);
ALTER TABLE Socios ADD CONSTRAINT fk_pais FOREIGN KEY (pais) REFERENCES Paises(codigo);
ALTER TABLE Socios ADD CONSTRAINT fk_qualificacao_do_representante_legal FOREIGN KEY (qualificacao_do_representante_legal) REFERENCES Qualificacoes(codigo);
ALTER TABLE Socios ADD CONSTRAINT fk_faixa_etaria FOREIGN KEY (faixa_etaria) REFERENCES FaixaEtaria(codigo);