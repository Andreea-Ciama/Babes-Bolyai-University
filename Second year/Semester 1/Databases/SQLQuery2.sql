
DROP TABLE Producers
DROP TABLE Directors
DROP TABLE Movies
DROP TABLE Battle_with
DROP TABLE Heroes
DROP TABLE Villans
DROP TABLE Play_in
DROP TABLE Plays_in
DROP TABLE GActors
DROP TABLE BActors
DROP TABLE Series





CREATE TABLE Heroes
	(HID INT PRIMARY KEY,
	Name VARCHAR(50) UNIQUE,
	Super_power VARCHAR(50),
	Planet VARCHAR(50),
	)



CREATE TABLE Villans
	(VID INT PRIMARY KEY,
	Name VARCHAR(50) UNIQUE,
	Super_power VARCHAR(50),
	Planet VARCHAR(50),
	)


CREATE TABLE Battle_with
	(HID INT REFERENCES Heroes(HID),
	VID INT REFERENCES Villans(VID)
	PRIMARY KEY(HID,VID)
	)

CREATE TABLE Producers
	(PID INT PRIMARY KEY,
	FirstName VARCHAR(50) UNIQUE,
	LastName VARCHAR(50) UNIQUE,
	Date_Of_Birth DATE,
	)
	
CREATE TABLE Directors
	(DID INT PRIMARY KEY,
	FirstName VARCHAR(50) UNIQUE,
	LastName VARCHAR(50) UNIQUE,
	Date_Of_Birth DATE,
	)

CREATE TABLE Movies
	(MID int primary key,
	Release_year VARCHAR(50),
	Phase INT,
	PID INT FOREIGN KEY REFERENCES Producers(PID) ON DELETE CASCADE ON UPDATE CASCADE,
	BID INT FOREIGN KEY REFERENCES Directors(DID)ON DELETE CASCADE ON UPDATE CASCADE,
	NameMovie VARCHAR(50)
	)
	
CREATE TABLE GActors
	(GAID INT PRIMARY KEY,
	FirstName VARCHAR(50) UNIQUE,
	LastName VARCHAR(50) UNIQUE,
	Nationality VARCHAR(50),
	Date_Of_Birth VARCHAR(50),
	HID INT FOREIGN KEY REFERENCES Heroes(HID) ON DELETE CASCADE ON UPDATE CASCADE
	)

ALTER TABLE GActors
DROP COLUMN HID



SELECT *
FROM Directors 
SELECT *
FROM Producers 



CREATE TABLE BActors
	(BAID INT PRIMARY KEY,
	FirstName VARCHAR(50) UNIQUE,
	LastName VARCHAR(50) UNIQUE,
	Nationality VARCHAR(50),
	Date_Of_Birth VARCHAR(50),
	VID INT UNIQUE FOREIGN KEY REFERENCES Villans(VID)
	)


DROP TABLE Series

CREATE TABLE Series
	(SID INT
	CONSTRAINT SERIES_PRIMARY_KEY PRIMARY KEY(SID),
	Release_year VARCHAR(50),
	BID INT NOT NULL,
	NameSeries VARCHAR(100) NOT NULL
	)



CREATE TABLE Play_in
	(GAID INT REFERENCES GActors(GAID),
	MID INT REFERENCES Movies(MID)
	PRIMARY KEY(GAID,MID)
	)

CREATE TABLE Plays_in
	(BAID INT REFERENCES BActors(BAID),
	MID INT REFERENCES Movies(MID)
	PRIMARY KEY(BAID,MID)
	)

CREATE TABLE Fan(
	fan_id INT PRIMARY KEY NOT NULL,
	fan_name VARCHAR(50),
	fan_age TINYINT,
	fan_country VARCHAR(50)
	)

CREATE TABLE Fan_of_hero(
	FID INT FOREIGN KEY REFERENCES Fan(fan_id) ON DELETE CASCADE ON UPDATE CASCADE,
	HID INT FOREIGN KEY REFERENCES Heroes(HID) ON DELETE CASCADE ON UPDATE CASCADE,
	favourite_hero VARCHAR(50),
	fan_percentage INT,
	PRIMARY KEY (FID, HID)
);



CREATE TABLE Series
	(SID INT
	CONSTRAINT SERIES_PRIMARY_KEY PRIMARY KEY(SID),
	Release_year VARCHAR(50),
	DID INT NOT NULL,
	NameSeries VARCHAR(100) NOT NULL
	)

ALTER TABLE Villans
ADD NrOfHeroes	INT

INSERT INTO Villans(VID,Name, Super_power, Planet,NrOfHeroes)
VALUES (1, 'Ultron', 'Robot', 'Earth', 4)

INSERT INTO Villans(VID,Name, Super_power, Planet,NrOfHeroes)
VALUES (2, 'Scarlet', 'Magic', 'Earth', 2)

INSERT INTO BActors(BAID,FirstName, LastName,Nationality,Date_Of_Birth,VID)
VALUES(1,'Olsen','Elizabeth','American', 1965-04-04,2)
 

SELECT COUNT(VID), NrOfHeroes
FROM Villans
GROUP BY NrOfHeroes;



SELECT M.NameMovie
FROM Movies M, GActors G, Heroes H, Villans V, Play_in P, Battle_with B
WHERE M.MID=P.MID AND P.GAID=G.GAID AND G.HID=H.HID AND H.HID=B.HID AND V.VID=B.VID AND V.Name='Ultron'



INSERT INTO Producers(PID, FirstName, LastName, Date_Of_Birth)
VALUES (2, 'Kalvin', 'Noah', '1979.05.12')



UPDATE Producers
SET Date_Of_Birth = '1966.10.19'
WHERE FirstName = 'Kalvin'

DELETE
FROM Producers 
WHERE FirstName = 'Feige'

ALTER TABLE Producers
ADD NrOfMovies	INT

ALTER TABLE Directors
ADD NrOfMovies	INT

ALTER TABLE GActors
ADD Salary INT

ALTER TABLE BActors
ADD Salary INT

UPDATE Producers
SET NrOfMovies = 0
WHERE FirstName = 'Kalvin'

UPDATE Directors
SET NrOfMovies = 2
WHERE FirstName = 'Favreau'

UPDATE Producers
SET NrOfMovies = 2
WHERE FirstName = 'Kalvin'


INSERT INTO Producers(PID, FirstName, LastName, Date_Of_Birth,NrOfMovies)
VALUES (1, 'Hoorain', 'Mellor', '1969-09-09',3),
	   (2, 'Feige', 'Kevin', '1973-06-02',0),
	   (3, 'Malvin', 'Chloe', '1979-05-13',3),
	   (4, 'Reagan', 'Galindo', '1980-09-30',1),
	   (5, 'Nel', 'Pruitt', '1984-11-15',2)
	   
	   

INSERT INTO Directors(DID, FirstName, LastName, Date_Of_Birth,NrOfMovies)
VALUES (2, 'Katerina', 'Mcconnell', '1990-11-09',3),
	   (3, 'Declan ', 'Grainger', '1988-06-01',1),
	   (4, 'Aida ', 'Browning', '1978-07-20',2),
	   (1, 'Favreau', 'Jon', '1966.10.19',1)

INSERT INTO Heroes(HID,Name, Super_power,Planet)
VALUES (1,'Thor', 'lighting', 'Asgard'),
	   (2,'Iron Man', 'technology','Earth'),
	   (3, 'Spider Man', 'self-designed web', 'Earth'),
	   (4, 'Gamora',' fighting skills', 'Zen-Whoberi'),
	   (5, 'Hulk', 'superhuman strength', 'Earth')

INSERT INTO Battle_with(HID,VID)
VALUES  (1,1)

INSERT INTO GActors(GAID,FirstName, LastName,Nationality,Date_Of_Birth,HID)
VALUES(1,'Downey','Robert','American', 1965-04-04,2),
	  (2,'Hemsworth', 'Chris', 'Australian',1983-08-11,1),
	  (3,'Saldana', 'Zoe', 'American', 1978-06-19,4),
	  (4,'Holland', 'Tom', 'English', 1996-06-01,3),
	  (5,'Ruffalo', 'Mark', 'American', 1967-11-22,5)



INSERT INTO Movies(MID, Release_year, Phase, PID, BID, NameMovie)
VALUES (1,2008,1,1,1,'The Incredible Hulk'),
	   (2,2012,2,2,3,'Age of Ultron'),
	   (3,2011,4,3,4,'Captain America'),
	   (4,2019,3,4,2,'Captain Marvel')
	   
UPDATE Movies
SET Release_year=2008
WHERE MID=2

ALTER TABLE Movies
ADD Budget INT

UPDATE Movies
SET Budget=10000
WHERE MID=1

UPDATE Movies
SET Budget=15000
WHERE MID=2

UPDATE Movies
SET Budget=13000
WHERE MID=3


UPDATE Movies
SET Budget=12000
WHERE MID=4


INSERT INTO Play_in(GAID, MID)
VALUES (1,2),
		(2,2),
		(5,1)
INSERT INTO Play_in(GAID, MID)
VALUES (4,3)

INSERT INTO Fan(fan_id,fan_name,fan_age, fan_country)
VALUES  (1,'Alex', 19,'Germany'),
		(2,'Maria', 17, 'Sweden'),
		(3, 'Carlos', 15, 'Spain'),
		(4, 'Kate', 20, 'Norway')

INSERT INTO Fan(fan_id,fan_name,fan_age, fan_country)
VALUES(5,'Carla',18,'Romania')

DELETE FROM Fan
WHERE fan_id = 5

INSERT INTO Fan_of_hero(FID,HID,favourite_hero,fan_percentage)
VALUES  (1,2,'Iron Man',60),
		(2,4,'Gamora',70)

INSERT INTO Fan_of_hero(FID,HID,favourite_hero,fan_percentage)
VALUES  (4,2,'Iron Man',60)

INSERT INTO Fan_of_hero(FID,HID,favourite_hero,fan_percentage)
VALUES  (3,2,'Iron Man',60)

DELETE FROM Fan_of_hero
WHERE FID=3

SELECT *
FROM Fan_of_hero

UPDATE GActors
SET Salary=1600
WHERE GAID=5

SELECT G.FirstName,G.Nationality,G.Salary
FROM GActors G

--a) 2 queries with the union operation; use UNION [ALL] and OR;
--First name of producers and directors who have 2 movies
SELECT P.FirstName, D.FirstName
FROM Producers P, Directors D
WHERE P.NrOfMovies = 2 OR D.NrOfMovies =2 

SELECT P.FirstName FROM Producers P
UNION ALL
SELECT D.FirstName FROM Directors D;

--b) two queries with the intersection operation; use INTERSECT and IN
--All producers who are also directors
SELECT P.FirstName, P.LastName
FROM Producers P
INTERSECT
SELECT D.FirstName, D.LastName
FROM Directors D

--All producers who are also directors (alternative with IN)
SELECT P.FirstName, P.LastName 
FROM Producers P 
WHERE P.FirstName  IN (SELECT D.FirstName FROM Directors D)


--c) two queries with the difference operation; use EXCEPT and NOT IN
--Heroes that are from earth, but are not the favorite hero of a fan

SELECT H.Name 
FROM Heroes H
WHERE H.Planet = 'Earth'
EXCEPT
SELECT FH.favourite_hero
FROM Fan_of_hero FH

--Heroes that are from earth, but are not the favorite hero of a fan
SELECT H.Name 
FROM Heroes H
WHERE H.Planet = 'Earth' AND H.Name NOT IN (SELECT FH.favourite_hero FROM Fan_of_hero FH)

--d) 4 queries with INNER JOIN, LEFT JOIN, RIGHT JOIN and FULL JOIN (one query per operator); 
--one query will join at least 3 tables, while another one will join at least two m:n relationships
-- Good actors and bad actors who have the same nationality

SELECT G.FirstName,G.LastName, B.FirstName,B.LastName
FROM GActors G
INNER JOIN BActors B
ON G.Nationality = B.Nationality

--LEFT JOIN
--Print all the producers and their movies and series, including the ones that have no movie or series
--join 3 tables: Movies, Producers, Directors
SELECT P.FirstName, P.LastName, M.NameMovie, S.NameSeries
FROM Producers P 
LEFT JOIN Movies M ON M.PID = P.PID
LEFT JOIN Series S ON M.PID = S.PID

--RIGHT JOIN
--Print all the movies including the Good Actors that play in; include actors that did not play in any movie
SELECT M.NameMovie, G.FirstName, G.LastName 
FROM Movies M
RIGHT JOIN Play_in P ON  P.MID= M.MID
RIGHT JOIN GActors G ON P.GAID = G.GAID

--FULL JOIN
--Print all the villans and the heroes that they are battling with,which has at least one fan;
--include villans that are not battling any hero , heroes that don't have a fan 
--and fans that don't have a favourite hero
--join at least two many-to-many relationships
SELECT V.Name, H.Name, F.fan_name
FROM Villans V
FULL JOIN Battle_with B ON B.VID= V.VID
FULL JOIN Heroes H ON H.HID = B.HID
FULL JOIN Fan_of_hero FH ON FH.HID = H.HID
FULL JOIN Fan F ON F.fan_id= FH.FID

--e) 2 queries with the IN operator and a subquery in the WHERE clause; in at least one case, the subquery should include a subquery in its own WHERE clause
--Print the name of fan which is a fan of a hero who is played by an good actor
--used DISTINCT


SELECT F.fan_name
FROM Fan F
WHERE F.fan_id IN (
	SELECT DISTINCT FH.FID
	FROM Heroes H2
	INNER JOIN	Fan_of_hero FH ON H2.HID = FH.HID
	INNER JOIN Fan FN ON FH.FID = FN.fan_id
	WHERE FH.HID IN (
		SELECT FH.HID
		FROM Heroes H3
		INNER JOIN GActors G ON H3.HID = G.HID
	)
)

--Print the name of fans which have fans that have as a favourite hero from earth who is played by an actor .

--condition in the WHERE clause with AND
--used DISTINCT
SELECT F.fan_name
FROM Fan F
WHERE F.fan_id IN (
	SELECT FH.FID
	FROM Fan_of_hero FH
	WHERE FH.favourite_hero IN (
		SELECT H.Name
		FROM Heroes H
		WHERE H.Planet= 'Earth' AND H.HID IN (
			SELECT DISTINCT G.HID
			FROM GActors G
		)
	)
)



--f) 2 queries with the EXISTS operator and a subquery in the WHERE clause
-- find the name of the producer who produced the movie with id 2 and increase the nr of movies with one
SELECT P.FirstName,P.NrOfMovies +1 AS NewNrOfMovies
FROM Producers P
WHERE EXISTS ( SELECT *
			   FROM Movies M
			   WHERE M.MID = 2 AND M.PID=P.PID
			   )


--Print heroes that battle with a villan
SELECT H.Name
FROM Heroes H 
WHERE EXISTS(
	SELECT * 
	FROM Villans V
	INNER JOIN Battle_with B ON V.VID = B.VID
	INNER JOIN Heroes H2 ON H2.HID = B.HID
	WHERE H2.HID = H.HID
)


--g) 2 queries with a subquery in the FROM clause
--Print the actors which have a salary of at least 1700 and are playing a hero
--Their salary will increase with 100 as a bonus for their hard work (arithmetic operation in the SELECT clause)
--condition in the WHERE clause with NOT
--used DISTINCT
SELECT g.FirstName, g.Salary + 100 AS increased_salary
FROM (
	SELECT *
	FROM GActors G
	WHERE NOT G.Salary < 1700
)g WHERE g.HID IN (
	SELECT DISTINCT H.HID 
	FROM Heroes H
)
ORDER BY increased_salary DESC

--Print the movies that have producers whith at least one movie produced, and which are played by good actors
--The budget will be increase by 2000
--arithmetic operation in the SELECT clause
--order ascending by the procentage   
SELECT m.NameMovie, m.Budget + 2000 AS budget
FROM (
	SELECT M.NameMovie,M.Budget,M.MID
	FROM Movies M INNER JOIN Producers P on P.PID = M.PID
	WHERE P.NrOfMovies >= 1
)m WHERE m.MID IN (
	SELECT M2.MID
	FROM Movies M2
	INNER JOIN Play_in P ON P.MID = M2.MID
	INNER JOIN GActors G ON G.GAID = P.GAID
)
ORDER BY budget ASC



--h) 4 queries with the GROUP BY clause, 3 of which also contain the HAVING clause; 2 of the latter will also have a subquery in the HAVING clause; use the aggregation operators: COUNT, SUM, AVG, MIN, MAX
--Print countries and the number of fans for each of them
--used COUNT
SELECT F.fan_country, COUNT(*) AS fans
FROM Fan F
GROUP BY F.fan_country

--Print the heroes with the most fans
--contains the HAVING clause
--has a subquery in the HAVING clause
--used COUNT, MAX
SELECT H.HID,H.Name, COUNT(*) AS fans
FROM Heroes H INNER JOIN Fan_of_hero FH ON H.HID = FH.HID INNER JOIN Fan F ON F.fan_id = FH.FID
GROUP BY H.HID, H.Name
HAVING COUNT(*) = (
	SELECT MAX(T.C)
	FROM (
		SELECT COUNT(*) C
		FROM Heroes H2 INNER JOIN Fan_of_hero FH2 ON H2.HID = FH2.HID INNER JOIN Fan F2 ON F2.fan_id = FH2.FID
		GROUP BY H2.HID, H2.Name
	)T
)

--Print the minimum from all the total budget per phase
--contains the HAVING clause
--has a subquery in the HAVING clause
--used SUM, MIN
SELECT M.Phase, SUM(M.Budget) AS total_budget
FROM Movies M
GROUP BY M.Phase
HAVING SUM(M.Budget) = (
	SELECT MIN(T.b)
	FROM (
		SELECT SUM(M2.Budget) b
		FROM Movies M2
		GROUP BY M2.Phase
	)T
)

--Print the average budget for each movie phase with at least 1 movie released after 2011
--used AVG, COUNT
--contains the HAVING clause
--has a subquery in the HAVING clause
SELECT M.Phase, AVG(M.Budget) AS average_budget
FROM Movies M
GROUP BY M.Phase
HAVING 1 <= (SELECT COUNT(M2.MID)
			FROM Movies M2
			WHERE M.Phase = M2.Phase AND M2.Release_year > 2011)




--i) 4 queries using ANY and ALL to introduce a subquery in the WHERE clause (2/operator); rewrite 2 of them with aggregation operators, and the other 2 with IN/[NOT] IN
--Find the top 3 good actors which earn more money than the american actor who earn less then the others
--using ANY
--using ORDER BY salary

SELECT TOP 3 G.*
FROM GActors G
WHERE G.Salary > ANY (
	SELECT G2.Salary
	FROM GActors G2
	WHERE G2.Nationality='American')
ORDER BY G.Salary DESC

--rewritten with an aggregation operator
--use MIN instead of ANY

SELECT TOP 3 G.*
FROM GActors G
WHERE G.Salary >  (
	SELECT MIN(G2.Salary)
	FROM GActors G2
	WHERE G2.Nationality='American')
ORDER BY G.Salary DESC

--find all the producers for the newest movies (movies that were released at least in 2018)
--using ANY
SELECT P.*
FROM Producers P
WHERE P.PID = ANY(
	SELECT M.PID
	FROM Movies M
	WHERE M.Release_year>2018)


--rewritten with IN
SELECT P.*
FROM Producers P
WHERE P.PID IN(
	SELECT M.PID
	FROM Movies M
	WHERE M.Release_year>2018)

--Find the movies for which the phase is greater than the phase of the movies with a budget smaller than 11000
--using ALL
--ordered descending by experience
SELECT  M.*
FROM Movies M
WHERE M.Phase > ALL (
	SELECT M2.Phase
	FROM Movies M2
	WHERE M2.Budget < 11000)
ORDER BY M.Phase DESC

--rewritten with an aggreation operator 
--used MAX instead of ALL
SELECT  M.*
FROM Movies M
WHERE M.Phase >  (
	SELECT MAX(M2.Phase)
	FROM Movies M2
	WHERE M2.Budget < 11000)
ORDER BY M.Phase DESC

--Find all the producers who didn't produce a movie from phase 2 
--using ALL
SELECT P.*
FROM Producers P
WHERE P.PID <> ALL (
	SELECT M.PID
	FROM Movies M
	WHERE M.Phase =2)

--rewritten using NOT IN
SELECT P.*
FROM Producers P
WHERE P.PID NOT IN (
	SELECT M.PID
	FROM Movies M
	WHERE M.Phase =2)

