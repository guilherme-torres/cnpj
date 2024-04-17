UPDATE Empresas SET porte_da_empresa = '00' WHERE porte_da_empresa = '';
ALTER TABLE Empresas ADD CONSTRAINT fk_porte_da_empresa FOREIGN KEY (porte_da_empresa) REFERENCES PorteEmpresa(codigo);