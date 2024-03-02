USE A5
DROP TABLE Groups
DROP TABLE Teachers
DROP TABLE Students

-- Tables creation
CREATE TABLE Students (
	aid INT PRIMARY KEY,
	a2 INT UNIQUE,
	a3 INT
)
DELETE FROM Students

CREATE TABLE Teachers (
	bid INT PRIMARY KEY,
	b2 INT
)

CREATE TABLE Groups (
	cid INT PRIMARY KEY,
	aid INT FOREIGN KEY REFERENCES Students(aid),
	bid INT FOREIGN KEY REFERENCES Teachers(bid)
)

-- Procedure to generate and insert random data into Students
GO
CREATE OR ALTER PROCEDURE insertIntoStudents(@rows INT) AS
BEGIN
	DECLARE @max INT
	SET @max = @rows*2 + 100
	WHILE @rows > 0
	BEGIN
		INSERT INTO Students VALUES (@rows, @max, @max%210)
		SET @rows = @rows - 1
		SET @max = @max - 2
	END
END

-- Procedure to generate and insert random data into Teachers
GO
CREATE OR ALTER PROCEDURE insertIntoTeachers(@rows INT) AS
BEGIN
	WHILE @rows > 0 
	BEGIN
		INSERT INTO Teachers VALUES(@rows, @rows%542)
		SET @rows = @rows - 1
	END
END

-- Procedure to generate and insert random data into Groups
GO
CREATE OR ALTER PROCEDURE insertIntoGroups(@rows INT) AS
BEGIN
	DECLARE @aid INT
	DECLARE @bid INT
	WHILE @rows > 0
	BEGIN
		SET @aid = (SELECT TOP 1 aid FROM Students ORDER BY NEWID())
		SET @bid = (SELECT TOP 1 bid FROM Teachers ORDER BY NEWID())
		INSERT INTO Groups VALUES(@rows, @aid, @bid)
		SET @rows = @rows - 1
	END
END

-- Inserting data
EXEC insertIntoStudents 5000
EXEC insertIntoTeachers 7500
EXEC insertIntoGroups 3000

SELECT *
FROM Students

SELECT *
FROM Teachers

SELECT *
FROM Groups

/* 
TASKS
OBS: 
- We have a clustered index automatically created for the aid column from Students
- We have a nonclustered index automatically created for the a2 column from Students
- We have a clustered index automatically created for the bid column from Teachers
- We have a clustered index automatically created for the cid column from Groups
*/

-- a) Write queries on Students such that their execution plans contain the following operators:
-- clustered index scan - scan the entire table 
-- Cost: 0.0176709
SELECT *
FROM Students

-- clustered index seek - return a specific subset of rows from a clustered index
-- Cost: 0.0034481
SELECT *
FROM Students
WHERE aid < 152

-- nonclustered index scan - scan the entire nonclustered index
-- Cost: 0.0147079
SELECT a2
FROM Students
ORDER BY a2

-- nonclustered index seek - return a specific subset of rows from a nonclustered index
-- Cost: 0.0032891
SELECT a2
FROM Students
WHERE a2 BETWEEN 120 AND 130

-- key lookup - nonclustered index seek + key lookup - the data is found in a nonclustered index, but additional data is needed
-- Cost: 0.0065704
SELECT a3, a2
FROM Students
WHERE a2 = 544

-- b) Write a query on table Teachers with a WHERE clause of the form WHERE b2 = value and analyze its execution plan. Create a nonclustered index that can speed up the query. Examine the execution plan again.
SELECT *
FROM Teachers
WHERE b2 = 154

-- Before creating a nonclustered index we have a clustered index scan with the cost: 0.0226431
DROP INDEX Teachers_b2_index ON Teachers
CREATE NONCLUSTERED INDEX Teachers_b2_index ON Teachers(b2)

-- After creating the nonclustered index on b2, we have a noclustered index seek with the cost: 0.0032974

-- c) Create a view that joins at least 2 tables. Check whether existing indexes are helpful; 
--if not, reassess existing indexes / examine the cardinality of the tables.

GO
CREATE OR ALTER VIEW View1 AS
	SELECT A.aid, B.bid, C.cid
	FROM Groups C
	INNER JOIN Students A ON A.aid = C.aid
	INNER JOIN Teachers B ON B.bid = C.bid
	WHERE B.b2 > 500 AND A.a3 < 150

GO
SELECT *
FROM View1

-- With existing indexes(the automatically created ones + nonclustered index on b2): 0.135151
-- When adding a nonclustered index on a3 to the existing indexes: 0.126723
-- Without the nonclustered index on b2 and the nonclustered index on a3: 0.157526
-- Automatically created indexes + nonclustered index on b2 + nonclustered index on a3 + nonclustered index on (aid, bid) from Groups: 0.125982

DROP INDEX Students_a3_index ON Students
CREATE NONCLUSTERED INDEX Students_a3_index ON Students(a3)

DROP INDEX Groups_index ON Groups
CREATE NONCLUSTERED INDEX Groups_index ON Groups(aid, bid)