--
-- PostgreSQL database dump
--

-- Dumped from database version 13.7
-- Dumped by pg_dump version 13.7

-- Started on 2022-06-16 16:24:42 UTC

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
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: user
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO "user";

--
-- TOC entry 3049 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: user
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 201 (class 1259 OID 16447)
-- Name: location; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.location (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    lat real NOT NULL,
    long real NOT NULL,
    score real NOT NULL
);


ALTER TABLE public.location OWNER TO "user";

--
-- TOC entry 200 (class 1259 OID 16445)
-- Name: location_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.location_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.location_id_seq OWNER TO "user";

--
-- TOC entry 3050 (class 0 OID 0)
-- Dependencies: 200
-- Name: location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.location_id_seq OWNED BY public.location.id;


--
-- TOC entry 205 (class 1259 OID 16471)
-- Name: post; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.post (
    id integer NOT NULL,
    social_profile_id integer NOT NULL,
    media_type character varying(255) NOT NULL,
    media_s3_key character varying(255) NOT NULL,
    location_id integer NOT NULL
);


ALTER TABLE public.post OWNER TO "user";

--
-- TOC entry 204 (class 1259 OID 16469)
-- Name: post_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.post_id_seq OWNER TO "user";

--
-- TOC entry 3051 (class 0 OID 0)
-- Dependencies: 204
-- Name: post_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.post_id_seq OWNED BY public.post.id;


--
-- TOC entry 207 (class 1259 OID 16494)
-- Name: postscore; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.postscore (
    id integer NOT NULL,
    media_score real NOT NULL,
    caption_score real NOT NULL,
    post_id integer NOT NULL
);


ALTER TABLE public.postscore OWNER TO "user";

--
-- TOC entry 206 (class 1259 OID 16492)
-- Name: postscore_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.postscore_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.postscore_id_seq OWNER TO "user";

--
-- TOC entry 3052 (class 0 OID 0)
-- Dependencies: 206
-- Name: postscore_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.postscore_id_seq OWNED BY public.postscore.id;


--
-- TOC entry 203 (class 1259 OID 16456)
-- Name: socialprofile; Type: TABLE; Schema: public; Owner: user
--

CREATE TABLE public.socialprofile (
    id integer NOT NULL,
    username character varying(255) NOT NULL,
    suggested_profiles_id integer
);


ALTER TABLE public.socialprofile OWNER TO "user";

--
-- TOC entry 202 (class 1259 OID 16454)
-- Name: socialprofile_id_seq; Type: SEQUENCE; Schema: public; Owner: user
--

CREATE SEQUENCE public.socialprofile_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.socialprofile_id_seq OWNER TO "user";

--
-- TOC entry 3053 (class 0 OID 0)
-- Dependencies: 202
-- Name: socialprofile_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: user
--

ALTER SEQUENCE public.socialprofile_id_seq OWNED BY public.socialprofile.id;


--
-- TOC entry 2884 (class 2604 OID 16450)
-- Name: location id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.location ALTER COLUMN id SET DEFAULT nextval('public.location_id_seq'::regclass);


--
-- TOC entry 2886 (class 2604 OID 16474)
-- Name: post id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post ALTER COLUMN id SET DEFAULT nextval('public.post_id_seq'::regclass);


--
-- TOC entry 2887 (class 2604 OID 16497)
-- Name: postscore id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.postscore ALTER COLUMN id SET DEFAULT nextval('public.postscore_id_seq'::regclass);


--
-- TOC entry 2885 (class 2604 OID 16459)
-- Name: socialprofile id; Type: DEFAULT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.socialprofile ALTER COLUMN id SET DEFAULT nextval('public.socialprofile_id_seq'::regclass);


--
-- TOC entry 3037 (class 0 OID 16447)
-- Dependencies: 201
-- Data for Name: location; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.location (id, name, lat, long, score) FROM stdin;
\.


--
-- TOC entry 3041 (class 0 OID 16471)
-- Dependencies: 205
-- Data for Name: post; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.post (id, social_profile_id, media_type, media_s3_key, location_id) FROM stdin;
\.


--
-- TOC entry 3043 (class 0 OID 16494)
-- Dependencies: 207
-- Data for Name: postscore; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.postscore (id, media_score, caption_score, post_id) FROM stdin;
\.


--
-- TOC entry 3039 (class 0 OID 16456)
-- Dependencies: 203
-- Data for Name: socialprofile; Type: TABLE DATA; Schema: public; Owner: user
--

COPY public.socialprofile (id, username, suggested_profiles_id) FROM stdin;
\.


--
-- TOC entry 3054 (class 0 OID 0)
-- Dependencies: 200
-- Name: location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.location_id_seq', 1, false);


--
-- TOC entry 3055 (class 0 OID 0)
-- Dependencies: 204
-- Name: post_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.post_id_seq', 1, false);


--
-- TOC entry 3056 (class 0 OID 0)
-- Dependencies: 206
-- Name: postscore_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.postscore_id_seq', 1, false);


--
-- TOC entry 3057 (class 0 OID 0)
-- Dependencies: 202
-- Name: socialprofile_id_seq; Type: SEQUENCE SET; Schema: public; Owner: user
--

SELECT pg_catalog.setval('public.socialprofile_id_seq', 1, false);


--
-- TOC entry 2890 (class 2606 OID 16452)
-- Name: location location_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.location
    ADD CONSTRAINT location_pkey PRIMARY KEY (id);


--
-- TOC entry 2897 (class 2606 OID 16479)
-- Name: post post_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_pkey PRIMARY KEY (id);


--
-- TOC entry 2900 (class 2606 OID 16499)
-- Name: postscore postscore_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.postscore
    ADD CONSTRAINT postscore_pkey PRIMARY KEY (id);


--
-- TOC entry 2892 (class 2606 OID 16461)
-- Name: socialprofile socialprofile_pkey; Type: CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.socialprofile
    ADD CONSTRAINT socialprofile_pkey PRIMARY KEY (id);


--
-- TOC entry 2888 (class 1259 OID 16453)
-- Name: location_name; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX location_name ON public.location USING btree (name);


--
-- TOC entry 2895 (class 1259 OID 16491)
-- Name: post_location_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX post_location_id ON public.post USING btree (location_id);


--
-- TOC entry 2898 (class 1259 OID 16490)
-- Name: post_social_profile_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX post_social_profile_id ON public.post USING btree (social_profile_id);


--
-- TOC entry 2901 (class 1259 OID 16505)
-- Name: postscore_post_id; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX postscore_post_id ON public.postscore USING btree (post_id);


--
-- TOC entry 2893 (class 1259 OID 16468)
-- Name: socialprofile_suggested_profiles_id; Type: INDEX; Schema: public; Owner: user
--

CREATE INDEX socialprofile_suggested_profiles_id ON public.socialprofile USING btree (suggested_profiles_id);


--
-- TOC entry 2894 (class 1259 OID 16467)
-- Name: socialprofile_username; Type: INDEX; Schema: public; Owner: user
--

CREATE UNIQUE INDEX socialprofile_username ON public.socialprofile USING btree (username);


--
-- TOC entry 2904 (class 2606 OID 16485)
-- Name: post post_location_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_location_id_fkey FOREIGN KEY (location_id) REFERENCES public.location(id);


--
-- TOC entry 2903 (class 2606 OID 16480)
-- Name: post post_social_profile_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.post
    ADD CONSTRAINT post_social_profile_id_fkey FOREIGN KEY (social_profile_id) REFERENCES public.socialprofile(id);


--
-- TOC entry 2905 (class 2606 OID 16500)
-- Name: postscore postscore_post_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.postscore
    ADD CONSTRAINT postscore_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.post(id);


--
-- TOC entry 2902 (class 2606 OID 16462)
-- Name: socialprofile socialprofile_suggested_profiles_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: user
--

ALTER TABLE ONLY public.socialprofile
    ADD CONSTRAINT socialprofile_suggested_profiles_id_fkey FOREIGN KEY (suggested_profiles_id) REFERENCES public.socialprofile(id);


-- Completed on 2022-06-16 16:24:42 UTC

--
-- PostgreSQL database dump complete
--
