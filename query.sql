-- Query an alphabetically ordered list of all names in OCCUPATIONS, immediately followed by the first letter of each profession as a parenthetical (i.e.: enclosed in parentheses). For example: AnActorName(A), ADoctorName(D), AProfessorName(P), and ASingerName(S).
-- Query the number of ocurrences of each occupation in OCCUPATIONS. Sort the occurrences in ascending order, and output them in the following format:

-- There are a total of [occupation_count] [occupation]s.

SELECT concat(NAME,concat("(",concat(substr(OCCUPATION,1,1),")"))) FROM OCCUPATIONS ORDER BY NAME ASC;

SELECT "There are a total of ", count(OCCUPATION), concat(lower(occupation),"s.") FROM OCCUPATIONS GROUP BY OCCUPATION ORDER BY count(OCCUPATION), OCCUPATION ASC

-- Query a list of CITY names from STATION for cities that have an even ID number. where LAT_N is the northern latitude and LONG_W is the western longitude.

-- Print the results in any order, but exclude duplicates from the answer.
select distinct city from station where lat_n > 0 and long_w > 0 and MOD(id, 2) = 0;

-- Difference between total number of cities and unique cities
SELECT (COUNT(CITY) - COUNT(DISTINCT CITY)) FROM STATION where lat_n > 0 and long_w > 0;

-- Print the cities with shortest and longest names sorted alphabethically
select city, length(city) from station order by length(city),city asc limit 1;
select city, length(city) from station order by length(city) desc limit 1;