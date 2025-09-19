CREATE TABLE usuario (
id_usuario INTEGER,
cpf_usuario INTEGER NOT NULL,
nome_usuario VARCHAR2(50),
data_nasc DATE NOT NULL,
user_admin CHAR(1) NOT NULL,

CONSTRAINT usuario_pk PRIMARY KEY ( id_usuario ),
CONSTRAINT usuario_cpf_un UNIQUE (cpf_usuario)

);

ALTER TABLE usuario
ADD CONSTRAINT usuario_admin_ck CHECK (user_admin IN ('S', 'N'));


CREATE TABLE perfil(
id_perfil INTEGER,
descricao VARCHAR(20) NOT NULL,
modo_acesso VARCHAR(30) NOT NULL,

CONSTRAINT perfil_pk PRIMARY KEY (id_perfil)
);


CREATE TABLE acesso (
id_acesso INTEGER,
data_acesso DATE NOT NULL,
id_usuario INTEGER,

CONSTRAINT acesso_pk PRIMARY KEY (id_acesso)
);

ALTER TABLE acesso
    ADD CONSTRAINT acesso_usuario_fk FOREIGN KEY (id_usuario)
        REFERENCES  usuario (id_usuario);
        
CREATE TABLE categoria_tutorial(
id_categoria INTEGER,
nome_categoria VARCHAR(50) NOT NULL,
desc_categoria VARCHAR(100) NOT NULL,

CONSTRAINT categoria_tuto_pk PRIMARY KEY (id_categoria)
);

CREATE TABLE video_tutoriais(
id_tutorial INTEGER,
titulo VARCHAR(50) NOT NULL,
url_video VARCHAR(255) NOT NULL,
id_categoria INTEGER,

CONSTRAINT videos_tuto_pk PRIMARY KEY (id_tutorial)
);

ALTER TABLE video_tutoriais
    ADD CONSTRAINT id_categoria_fk FOREIGN KEY (id_categoria)
        REFERENCES  categoria_tutorial (id_categoria);



CREATE TABLE lembretes(
id_lembrete INTEGER,
nome_lembrete VARCHAR(20) NOT NULL,
data_lembrete DATE NOT NULL,
desc_lembrete VARCHAR(200) NOT NULL,

CONSTRAINT id_lembrete_pk PRIMARY KEY (id_lembrete)
);

CREATE TABLE suporte(
id_suporte INTEGER,
duvida VARCHAR(200) NOT NULL,

CONSTRAINT id_suporte_pk PRIMARY KEY (id_suporte)
);