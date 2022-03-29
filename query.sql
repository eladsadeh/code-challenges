-- Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

-- There are a total of [occupation_count] [occupation]s.

SELECT concat(NAME,concat("(",concat(substr(OCCUPATION,1,1),")"))) FROM OCCUPATIONS ORDER BY NAME ASC;

SELECT "There are a total of ", count(OCCUPATION), concat(lower(occupation),"s.") FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY count(OCCUPATION), OCCUPATION ASC