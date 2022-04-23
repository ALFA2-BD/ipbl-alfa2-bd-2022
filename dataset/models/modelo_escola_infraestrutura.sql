-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-04-22 18:52:52.241

-- tables
-- Table: CONTRATO
CREATE TABLE CONTRATO (
    con_id serial  NOT NULL,
    uni_id serial  NOT NULL,
    inf_id serial  NOT NULL,
    con_data_ini date  NOT NULL,
    con_data_fim date  NOT NULL,
    con_tipo int  NOT NULL,
    CONSTRAINT CONTRATO_pk PRIMARY KEY (con_id)
);

-- Table: INFRAESTRUTURA
CREATE TABLE INFRAESTRUTURA (
    inf_id serial  NOT NULL,
    inf_nome_cluster varchar(30)  NOT NULL,
    inf_nivel_gov int  NOT NULL,
    inf_nome_provedor varchar(255)  NOT NULL,
    CONSTRAINT INFRAESTRUTURA_pk PRIMARY KEY (inf_id)
);

-- Table: NODE
CREATE TABLE NODE (
    nod_id serial  NOT NULL,
    inf_id serial  NOT NULL,
    nod_ip varchar(15)  NOT NULL,
    nod_porta int  NOT NULL,
    CONSTRAINT NODE_pk PRIMARY KEY (nod_id)
);

-- Table: UNIDADE_ESCOLAR
CREATE TABLE UNIDADE_ESCOLAR (
    uni_id serial  NOT NULL,
    uni_codigo_inep int  NOT NULL,
    uni_nome varchar(255)  NOT NULL,
    uni_uf char(2)  NOT NULL,
    uni_cep char(9)  NOT NULL,
    uni_endereco varchar(255)  NOT NULL,
    uni_municipio varchar(50)  NOT NULL,
    uni_categ_admin int  NOT NULL,
    uni_depen_admin int  NOT NULL,
    CONSTRAINT UNIDADE_ESCOLAR_pk PRIMARY KEY (uni_id)
);

-- foreign keys
-- Reference: CONTRATO_INFRAESTRUTURA (table: CONTRATO)
ALTER TABLE CONTRATO ADD CONSTRAINT CONTRATO_INFRAESTRUTURA
    FOREIGN KEY (inf_id)
    REFERENCES INFRAESTRUTURA (inf_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: CONTRATO_UNIDADE_ESCOLAR (table: CONTRATO)
ALTER TABLE CONTRATO ADD CONSTRAINT CONTRATO_UNIDADE_ESCOLAR
    FOREIGN KEY (uni_id)
    REFERENCES UNIDADE_ESCOLAR (uni_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: NODE_INFRAESTRUTURA (table: NODE)
ALTER TABLE NODE ADD CONSTRAINT NODE_INFRAESTRUTURA
    FOREIGN KEY (inf_id)
    REFERENCES INFRAESTRUTURA (inf_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

