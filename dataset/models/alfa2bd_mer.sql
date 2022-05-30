-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-05-30 03:58:01.645

-- tables
-- Table: ALUNO
CREATE TABLE ALUNO (
    alu_id serial  NOT NULL,
    alu_primeiro_nome varchar(255)  NOT NULL,
    alu_segundo_nome varchar(255)  NOT NULL,
    alu_tipo varchar(256)  NOT NULL,
    tur_id serial  NOT NULL,
    CONSTRAINT ALUNO_pk PRIMARY KEY (alu_id)
);

-- Table: AVALIACAO
CREATE TABLE AVALIACAO (
    ava_id serial  NOT NULL,
    ava_tipo varchar(256)  NOT NULL,
    ava_data timestamp  NOT NULL,
    alu_id serial  NOT NULL,
    pro_id serial  NOT NULL,
    CONSTRAINT AVALIACAO_pk PRIMARY KEY (ava_id)
);

-- Table: COLETA
CREATE TABLE COLETA (
    col_id serial  NOT NULL,
    col_audio mp3  NOT NULL,
    col_metrica real  NOT NULL,
    fra_id serial  NOT NULL,
    ava_id serial  NOT NULL,
    CONSTRAINT COLETA_pk PRIMARY KEY (col_id)
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

-- Table: FRASE
CREATE TABLE FRASE (
    fra_id serial  NOT NULL,
    fra_frase varchar(256)  NOT NULL,
    fra_tipo int  NOT NULL,
    CONSTRAINT FRASE_pk PRIMARY KEY (fra_id)
);

-- Table: GESTOR_ADMIN
CREATE TABLE GESTOR_ADMIN (
    ges_adm_id serial  NOT NULL,
    ges_adm_primeiro_nome varchar(256)  NOT NULL,
    ges_adm_segundo_nome varchar(256)  NOT NULL,
    ges_adm_senha varchar(256)  NOT NULL,
    CONSTRAINT GESTOR_ADMIN_pk PRIMARY KEY (ges_adm_id)
);

-- Table: GESTOR_ESCOLA
CREATE TABLE GESTOR_ESCOLA (
    ges_id serial  NOT NULL,
    ges_identificador varchar(256)  NOT NULL,
    ges_primeiro_nome varchar(256)  NOT NULL,
    ges_segundo_nome varchar(256)  NOT NULL,
    ges_senha varchar(256)  NOT NULL,
    ges_ges_id int  NOT NULL,
    CONSTRAINT GESTOR_ESCOLA_pk PRIMARY KEY (ges_id)
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
    pro_identificador varchar(256)  NOT NULL,
    pro_primeiro_nome varchar(255)  NOT NULL,
    pro_segundo_nome varchar(255)  NOT NULL,
    pro_senha varchar(256)  NOT NULL,
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
    ges_id int  NOT NULL,
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

-- Reference: AVALIACAO_ALUNO (table: AVALIACAO)
ALTER TABLE AVALIACAO ADD CONSTRAINT AVALIACAO_ALUNO
    FOREIGN KEY (alu_id)
    REFERENCES ALUNO (alu_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: AVALIACAO_PROFESSOR (table: AVALIACAO)
ALTER TABLE AVALIACAO ADD CONSTRAINT AVALIACAO_PROFESSOR
    FOREIGN KEY (pro_id)
    REFERENCES PROFESSOR (pro_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_AVALIACAO (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_AVALIACAO
    FOREIGN KEY (ava_id)
    REFERENCES AVALIACAO (ava_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: COLETA_FRASES (table: COLETA)
ALTER TABLE COLETA ADD CONSTRAINT COLETA_FRASES
    FOREIGN KEY (fra_id)
    REFERENCES FRASE (fra_id)  
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

-- Reference: GESTOR_ESCOLA_GESTOR_GESTOR (table: GESTOR_ESCOLA)
ALTER TABLE GESTOR_ESCOLA ADD CONSTRAINT GESTOR_ESCOLA_GESTOR_GESTOR
    FOREIGN KEY (ges_ges_id)
    REFERENCES GESTOR_ADMIN (ges_adm_id)  
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

-- Reference: UNIDADE_ESCOLAR_GESTOR_ESCOLA (table: UNIDADE_ESCOLAR)
ALTER TABLE UNIDADE_ESCOLAR ADD CONSTRAINT UNIDADE_ESCOLAR_GESTOR_ESCOLA
    FOREIGN KEY (ges_id)
    REFERENCES GESTOR_ESCOLA (ges_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

