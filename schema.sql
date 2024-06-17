--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--



--
-- Name: generos; Type: TABLE; Schema: livros_db; Owner: -
--

CREATE TABLE livros_db.generos (
    genero_id smallint NOT NULL,
    descricao character varying(30) NOT NULL
);


--
-- Name: livros; Type: TABLE; Schema: livros_db; Owner: -
--

CREATE TABLE livros_db.livros (
    livro_id smallint NOT NULL,
    titulo character varying(150) NOT NULL,
    autor character varying(150) NOT NULL,
    edicao smallint NOT NULL,
    ano smallint NOT NULL,
    editora character varying(50) NOT NULL,
    genero_id smallint NOT NULL,
    descricao character varying(450) NOT NULL,
    preco numeric(15,2) NOT NULL,
    estoque smallint NOT NULL,
    reserva smallint NOT NULL,
    capa bytea
);


--
-- Name: pedidos; Type: TABLE; Schema: livros_db; Owner: -
--

CREATE TABLE livros_db.pedidos (
    pedido_id integer NOT NULL,
    usuario_id smallint NOT NULL,
    data_pedido date NOT NULL,
    tipo_pag smallint NOT NULL
);


--
-- Name: pedidos_detalhe; Type: TABLE; Schema: livros_db; Owner: -
--

CREATE TABLE livros_db.pedidos_detalhe (
    detalhe_id integer NOT NULL,
    pedido_id bigint NOT NULL,
    livro_id smallint NOT NULL,
    qtd smallint NOT NULL
);


--
-- Name: pedidos_detalhe_detalhe_id_seq; Type: SEQUENCE; Schema: livros_db; Owner: -
--

CREATE SEQUENCE livros_db.pedidos_detalhe_detalhe_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: pedidos_detalhe_detalhe_id_seq; Type: SEQUENCE OWNED BY; Schema: livros_db; Owner: -
--

ALTER SEQUENCE livros_db.pedidos_detalhe_detalhe_id_seq OWNED BY livros_db.pedidos_detalhe.detalhe_id;


--
-- Name: pedidos_pedido_id_seq; Type: SEQUENCE; Schema: livros_db; Owner: -
--

CREATE SEQUENCE livros_db.pedidos_pedido_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: pedidos_pedido_id_seq; Type: SEQUENCE OWNED BY; Schema: livros_db; Owner: -
--

ALTER SEQUENCE livros_db.pedidos_pedido_id_seq OWNED BY livros_db.pedidos.pedido_id;


--
-- Name: usuarios; Type: TABLE; Schema: livros_db; Owner: -
--

CREATE TABLE livros_db.usuarios (
    usuario_id smallint NOT NULL,
    nome character varying(40) NOT NULL,
    endereco character varying(40),
    bairro character varying(30),
    cidade character varying(30) NOT NULL,
    uf character(2) NOT NULL,
    cep character(8) NOT NULL,
    fone character varying(20) NOT NULL,
    login character varying(20) NOT NULL,
    senha character varying(20) NOT NULL
);


--
-- Name: pedidos pedido_id; Type: DEFAULT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos ALTER COLUMN pedido_id SET DEFAULT nextval('livros_db.pedidos_pedido_id_seq'::regclass);


--
-- Name: pedidos_detalhe detalhe_id; Type: DEFAULT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos_detalhe ALTER COLUMN detalhe_id SET DEFAULT nextval('livros_db.pedidos_detalhe_detalhe_id_seq'::regclass);


--
-- Name: generos generos_pkey; Type: CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.generos
    ADD CONSTRAINT generos_pkey PRIMARY KEY (genero_id);


--
-- Name: livros livros_pkey; Type: CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.livros
    ADD CONSTRAINT livros_pkey PRIMARY KEY (livro_id);


--
-- Name: pedidos_detalhe pedidos_detalhe_pkey; Type: CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos_detalhe
    ADD CONSTRAINT pedidos_detalhe_pkey PRIMARY KEY (detalhe_id);


--
-- Name: pedidos pedidos_pkey; Type: CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos
    ADD CONSTRAINT pedidos_pkey PRIMARY KEY (pedido_id);


--
-- Name: usuarios usuarios_pkey; Type: CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.usuarios
    ADD CONSTRAINT usuarios_pkey PRIMARY KEY (usuario_id);


--
-- Name: livros livros_genero_id_fkey; Type: FK CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.livros
    ADD CONSTRAINT livros_genero_id_fkey FOREIGN KEY (genero_id) REFERENCES livros_db.generos(genero_id);


--
-- Name: pedidos_detalhe pedidos_detalhe_livro_id_fkey; Type: FK CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos_detalhe
    ADD CONSTRAINT pedidos_detalhe_livro_id_fkey FOREIGN KEY (livro_id) REFERENCES livros_db.livros(livro_id);


--
-- Name: pedidos_detalhe pedidos_detalhe_pedido_id_fkey; Type: FK CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos_detalhe
    ADD CONSTRAINT pedidos_detalhe_pedido_id_fkey FOREIGN KEY (pedido_id) REFERENCES livros_db.pedidos(pedido_id);


--
-- Name: pedidos pedidos_usuario_id_fkey; Type: FK CONSTRAINT; Schema: livros_db; Owner: -
--

ALTER TABLE ONLY livros_db.pedidos
    ADD CONSTRAINT pedidos_usuario_id_fkey FOREIGN KEY (usuario_id) REFERENCES livros_db.usuarios(usuario_id);


--
-- PostgreSQL database dump complete
--

