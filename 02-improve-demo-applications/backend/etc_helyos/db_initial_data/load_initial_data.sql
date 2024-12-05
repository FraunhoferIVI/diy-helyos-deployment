--
-- helyOS PostgreSQL Internal Data
--


--
-- Data for Yard
--

ALTER TABLE public.yards DISABLE TRIGGER ALL;

INSERT INTO public.yards 
            (id, uid , name,   description,   source    ,   yard_type     ,   map_data,                                                            lat,      lon,  alt,    created_at,                      modified_at )
     VALUES   
            (1, 'FTB', 'Football', 'test yard', 'initial data', 'logistic_yard', '{"origin": {"lat": 51.0531973, "lon": 13.7031056, "alt": 116, "zoomLevel": 19}}', 48.1139, 11.542205, 116, '2024-08-03 12:00:00.000000', '2020-08-03 12:00:00.000000');

ALTER TABLE public.yards ENABLE TRIGGER ALL;
SELECT pg_catalog.setval('public.yards_id_seq', 3, true);

--
-- Data for Map Objects
--

ALTER TABLE public.map_objects DISABLE TRIGGER ALL;

--
--  Insert map objects here ...
--

ALTER TABLE public.map_objects ENABLE TRIGGER ALL;
SELECT pg_catalog.setval('public.map_objects_id_seq', 1, true);




