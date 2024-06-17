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



--
-- Name: advisor; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.advisor (
    s_id character varying(5) NOT NULL,
    i_id character varying(5)
);


--
-- Name: classroom; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.classroom (
    building character varying(15) NOT NULL,
    room_number character varying(7) NOT NULL,
    capacity numeric(4,0)
);


--
-- Name: course; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.course (
    course_id character varying(8) NOT NULL,
    title character varying(50),
    dept_name character varying(20),
    credits numeric(2,0),
    CONSTRAINT course_credits_check CHECK ((credits > (0)::numeric))
);


--
-- Name: department; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.department (
    dept_name character varying(20) NOT NULL,
    building character varying(15),
    budget numeric(12,2),
    CONSTRAINT department_budget_check CHECK ((budget > (0)::numeric))
);


--
-- Name: instructor; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.instructor (
    id character varying(5) NOT NULL,
    name character varying(20) NOT NULL,
    dept_name character varying(20),
    salary numeric(8,2),
    CONSTRAINT instructor_salary_check CHECK ((salary > (29000)::numeric))
);


--
-- Name: prereq; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.prereq (
    course_id character varying(8) NOT NULL,
    prereq_id character varying(8) NOT NULL
);


--
-- Name: section; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.section (
    course_id character varying(8) NOT NULL,
    sec_id character varying(8) NOT NULL,
    semester character varying(6) NOT NULL,
    year numeric(4,0) NOT NULL,
    building character varying(15),
    room_number character varying(7),
    time_slot_id character varying(4),
    CONSTRAINT section_semester_check CHECK (((semester)::text = ANY ((ARRAY['Fall'::character varying, 'Winter'::character varying, 'Spring'::character varying, 'Summer'::character varying])::text[]))),
    CONSTRAINT section_year_check CHECK (((year > (1701)::numeric) AND (year < (2100)::numeric)))
);


--
-- Name: student; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.student (
    id character varying(5) NOT NULL,
    name character varying(20) NOT NULL,
    dept_name character varying(20),
    tot_cred numeric(3,0),
    CONSTRAINT student_tot_cred_check CHECK ((tot_cred >= (0)::numeric))
);


--
-- Name: takes; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.takes (
    id character varying(5) NOT NULL,
    course_id character varying(8) NOT NULL,
    sec_id character varying(8) NOT NULL,
    semester character varying(6) NOT NULL,
    year numeric(4,0) NOT NULL,
    grade character varying(2)
);


--
-- Name: teaches; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.teaches (
    id character varying(5) NOT NULL,
    course_id character varying(8) NOT NULL,
    sec_id character varying(8) NOT NULL,
    semester character varying(6) NOT NULL,
    year numeric(4,0) NOT NULL
);


--
-- Name: test; Type: VIEW; Schema: university; Owner: -
--

CREATE VIEW university.test AS
 SELECT oid,
    typname,
    typnamespace,
    typowner,
    typlen,
    typbyval,
    typtype,
    typcategory,
    typispreferred,
    typisdefined,
    typdelim,
    typrelid,
    typsubscript,
    typelem,
    typarray,
    typinput,
    typoutput,
    typreceive,
    typsend,
    typmodin,
    typmodout,
    typanalyze,
    typalign,
    typstorage,
    typnotnull,
    typbasetype,
    typtypmod,
    typndims,
    typcollation,
    typdefaultbin,
    typdefault,
    typacl
   FROM pg_type;


--
-- Name: time_slot; Type: TABLE; Schema: university; Owner: -
--

CREATE TABLE university.time_slot (
    time_slot_id character varying(4) NOT NULL,
    day character varying(1) NOT NULL,
    start_hr numeric(2,0) NOT NULL,
    start_min numeric(2,0) NOT NULL,
    end_hr numeric(2,0),
    end_min numeric(2,0),
    CONSTRAINT time_slot_end_hr_check CHECK (((end_hr >= (0)::numeric) AND (end_hr < (24)::numeric))),
    CONSTRAINT time_slot_end_min_check CHECK (((end_min >= (0)::numeric) AND (end_min < (60)::numeric))),
    CONSTRAINT time_slot_start_hr_check CHECK (((start_hr >= (0)::numeric) AND (start_hr < (24)::numeric))),
    CONSTRAINT time_slot_start_min_check CHECK (((start_min >= (0)::numeric) AND (start_min < (60)::numeric)))
);


--
-- Name: advisor advisor_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.advisor
    ADD CONSTRAINT advisor_pkey PRIMARY KEY (s_id);


--
-- Name: classroom classroom_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.classroom
    ADD CONSTRAINT classroom_pkey PRIMARY KEY (building, room_number);


--
-- Name: course course_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.course
    ADD CONSTRAINT course_pkey PRIMARY KEY (course_id);


--
-- Name: department department_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.department
    ADD CONSTRAINT department_pkey PRIMARY KEY (dept_name);


--
-- Name: instructor instructor_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.instructor
    ADD CONSTRAINT instructor_pkey PRIMARY KEY (id);


--
-- Name: prereq prereq_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.prereq
    ADD CONSTRAINT prereq_pkey PRIMARY KEY (course_id, prereq_id);


--
-- Name: section section_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.section
    ADD CONSTRAINT section_pkey PRIMARY KEY (course_id, sec_id, semester, year);


--
-- Name: student student_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.student
    ADD CONSTRAINT student_pkey PRIMARY KEY (id);


--
-- Name: takes takes_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.takes
    ADD CONSTRAINT takes_pkey PRIMARY KEY (id, course_id, sec_id, semester, year);


--
-- Name: teaches teaches_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.teaches
    ADD CONSTRAINT teaches_pkey PRIMARY KEY (id, course_id, sec_id, semester, year);


--
-- Name: time_slot time_slot_pkey; Type: CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.time_slot
    ADD CONSTRAINT time_slot_pkey PRIMARY KEY (time_slot_id, day, start_hr, start_min);


--
-- Name: advisor advisor_i_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.advisor
    ADD CONSTRAINT advisor_i_id_fkey FOREIGN KEY (i_id) REFERENCES university.instructor(id) ON DELETE SET NULL;


--
-- Name: advisor advisor_s_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.advisor
    ADD CONSTRAINT advisor_s_id_fkey FOREIGN KEY (s_id) REFERENCES university.student(id) ON DELETE CASCADE;


--
-- Name: course course_dept_name_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.course
    ADD CONSTRAINT course_dept_name_fkey FOREIGN KEY (dept_name) REFERENCES university.department(dept_name) ON DELETE SET NULL;


--
-- Name: instructor instructor_dept_name_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.instructor
    ADD CONSTRAINT instructor_dept_name_fkey FOREIGN KEY (dept_name) REFERENCES university.department(dept_name) ON DELETE SET NULL;


--
-- Name: prereq prereq_course_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.prereq
    ADD CONSTRAINT prereq_course_id_fkey FOREIGN KEY (course_id) REFERENCES university.course(course_id) ON DELETE CASCADE;


--
-- Name: prereq prereq_prereq_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.prereq
    ADD CONSTRAINT prereq_prereq_id_fkey FOREIGN KEY (prereq_id) REFERENCES university.course(course_id);


--
-- Name: section section_building_room_number_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.section
    ADD CONSTRAINT section_building_room_number_fkey FOREIGN KEY (building, room_number) REFERENCES university.classroom(building, room_number) ON DELETE SET NULL;


--
-- Name: section section_course_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.section
    ADD CONSTRAINT section_course_id_fkey FOREIGN KEY (course_id) REFERENCES university.course(course_id) ON DELETE CASCADE;


--
-- Name: student student_dept_name_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.student
    ADD CONSTRAINT student_dept_name_fkey FOREIGN KEY (dept_name) REFERENCES university.department(dept_name) ON DELETE SET NULL;


--
-- Name: takes takes_course_id_sec_id_semester_year_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.takes
    ADD CONSTRAINT takes_course_id_sec_id_semester_year_fkey FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES university.section(course_id, sec_id, semester, year) ON DELETE CASCADE;


--
-- Name: takes takes_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.takes
    ADD CONSTRAINT takes_id_fkey FOREIGN KEY (id) REFERENCES university.student(id) ON DELETE CASCADE;


--
-- Name: teaches teaches_course_id_sec_id_semester_year_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.teaches
    ADD CONSTRAINT teaches_course_id_sec_id_semester_year_fkey FOREIGN KEY (course_id, sec_id, semester, year) REFERENCES university.section(course_id, sec_id, semester, year) ON DELETE CASCADE;


--
-- Name: teaches teaches_id_fkey; Type: FK CONSTRAINT; Schema: university; Owner: -
--

ALTER TABLE ONLY university.teaches
    ADD CONSTRAINT teaches_id_fkey FOREIGN KEY (id) REFERENCES university.instructor(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

