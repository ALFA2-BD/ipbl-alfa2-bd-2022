-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-05-19 23:03:48.263

-- tables
-- Table: ALUNO
CREATE TABLE ALUNO (
    alu_id serial  NOT NULL,
    alu_primeiro_nome varchar(255)  NOT NULL,
    alu_segundo_nome varchar(255)  NOT NULL,
    alu_escola varchar(255)  NOT NULL,
    tur_id serial  NOT NULL,
    CONSTRAINT ALUNO_pk PRIMARY KEY (alu_id)
);

-- Table: COLETA
CREATE TABLE COLETA (
    col_id serial  NOT NULL,
    col_prim_tentativa int  NOT NULL,
    col_seg_tentativa int  NULL,
    col_ter_tentativa int  NULL,
    alu_id serial  NOT NULL,
    pro_id serial  NOT NULL,
    CONSTRAINT col_id PRIMARY KEY (col_id)
);

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

-- Table: PROFESSOR
CREATE TABLE PROFESSOR (
    pro_id serial  NOT NULL,
    pro_primeiro_nome varchar(255)  NOT NULL,
    pro_segundo_nome varchar(255)  NOT NULL,
    pro_escola varchar(255)  NOT NULL,
    CONSTRAINT PROFESSOR_pk PRIMARY KEY (pro_id)
);

-- Table: TURMA
CREATE TABLE TURMA (
    tur_id serial  NOT NULL,
    tur_ano int  NOT NULL,
    tur_ano_escolar int  NOT NULL,
    uni_id serial  NOT NULL,
    pro_id serial  NOT NULL,
    CONSTRAINT TURMA_pk PRIMARY KEY (tur_id)
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
-- Reference: ALUNO_Turma (table: ALUNO)
ALTER TABLE ALUNO ADD CONSTRAINT ALUNO_Turma
    FOREIGN KEY (tur_id)
    REFERENCES TURMA (tur_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_ALUNO (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_ALUNO
    FOREIGN KEY (alu_id)
    REFERENCES ALUNO (alu_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_PROFESSOR (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_PROFESSOR
    FOREIGN KEY (pro_id)
    REFERENCES PROFESSOR (pro_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

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

-- Reference: TURMA_PROFESSOR (table: TURMA)
ALTER TABLE TURMA ADD CONSTRAINT TURMA_PROFESSOR
    FOREIGN KEY (pro_id)
    REFERENCES PROFESSOR (pro_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Turma_UNIDADE_ESCOLAR (table: TURMA)
ALTER TABLE TURMA ADD CONSTRAINT Turma_UNIDADE_ESCOLAR
    FOREIGN KEY (uni_id)
    REFERENCES UNIDADE_ESCOLAR (uni_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

