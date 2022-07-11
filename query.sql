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

-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.

SELECT DISTINCT city FROM station WHERE city REGEXP "^[aeiou].*";

-- Query the list of CITY names ends with vowels (i.e., a, e, i, o, or u) from STATION. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE RIGHT(CITY,1) IN ('a','e','i','o','u');

-- Query the list of CITY names from STATION which have vowels (i.e., a, e, i, o, and u) as both their first and last characters. Your result cannot contain duplicates.
SELECT DISTINCT CITY FROM STATION WHERE LOWER(LEFT(CITY,1)) IN ('a','e','i','o','u') AND RIGHT(CITY,1) IN ('a','e','i','o','u');
SELECT DISTINCT city FROM station WHERE city RLIKE '^[aeiou].*[aeiou]$';

-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE NOT city RLIKE '^[aeiou].*';

--Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. Your result cannot contain duplicates.
SELECT DISTINCT city FROM station WHERE city NOT RLIKE '^[aeiou].*'  OR city NOT RLIKE '[aeiou]$';

-- Query the Name of any student in STUDENTS who scored higher than 75 Marks. Order your output by the last three characters of each name. If two or more students both have names ending in the same last three characters (i.e.: Bobby, Robby, etc.), secondary sort them by ascending ID.
select name from students where marks > 75 order by right(name,3), ID ASC;

-- Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to  decimal places.
SELECT ROUND(MIN(Lat_N), 4) FROM Station WHERE Lat_N > 38.7780;

-- Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to 4 decimal places.
select round(LONG_W,4) from STATION where LAT_N=(select min(LAT_N) from STATION where LAT_N>38.7780);
