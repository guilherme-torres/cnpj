CREATE INDEX IF NOT EXISTS cnpj_empresas_idx ON empresas (cnpj_basico);
CREATE INDEX IF NOT EXISTS cnpj_estabelecimentos_idx ON estabelecimentos (cnpj_basico);
CREATE INDEX IF NOT EXISTS cnpj_simples_idx ON simples (cnpj_basico);
CREATE INDEX IF NOT EXISTS cnpj_socios_idx ON socios (cnpj_basico);