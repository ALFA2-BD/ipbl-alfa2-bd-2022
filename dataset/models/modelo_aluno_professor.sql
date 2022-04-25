-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2022-04-25 02:37:14.915

-- tables
-- Table: ALUNO
CREATE TABLE ALUNO (
    alu_id serial  NOT NULL,
    alu_primeiro_nome varchar(255)  NOT NULL,
    alu_segundo_nome varchar(255)  NOT NULL,
    alu_escola varchar(255)  NOT NULL,
    CONSTRAINT ALUNO_pk PRIMARY KEY (alu_id)
);

-- Table: PROFESSOR
CREATE TABLE PROFESSOR (
    pro_id serial  NOT NULL,
    pro_primeiro_nome varchar(255)  NOT NULL,
    pro_segundo_nome varchar(255)  NOT NULL,
    pro_escola varchar(255)  NOT NULL,
    CONSTRAINT PROFESSOR_pk PRIMARY KEY (pro_id)
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

-- foreign keys
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

-- End of file.

