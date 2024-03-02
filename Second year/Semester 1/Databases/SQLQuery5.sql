USE practic_seminar
--1.c
--2.c
--3.b

--Each train has a name and
--belongs to a type. A train type has a name and a description. Each station has a name. Station names are unique.
--Each route has a name, an associated train, and a list of stations with arrival and departure times in each station.
--Route names are unique. The arrival and departure times are represented as hour:minute pairs, e.g., train arrives
--at 5 pm and leaves at 5:10 pm.

DROP TABLE RoutesStations
DROP TABLE Stations
DROP TABLE Routes
DROP TABLE Trains
DROP TABLE TrainTypes

GO

CREATE TABLE TrainTypes
	(TrainTypeID INT PRIMARY KEY,
	TTName Varchar(50),
	TTDescription Varchar(50))

CREATE TABLE Trains
	(TrainID INT PRIMARY KEY,
	TName Varchar(50),
	TrainTypeID INT REFERENCES TrainTypes(TrainTypeID))

CREATE TABLE Routes
	(RouteID INT PRIMARY KEY,
	RName Varchar(50) UNIQUE,
	TrainID INT REFERENCES Trains(TrainID))

CREATE TABLE Stations
	(StationID INT PRIMARY KEY,
	SName Varchar(50) UNIQUE)

CREATE TABLE RoutesStations
	(RouteID INT REFERENCES Routes(RouteID),
	StationID INT REFERENCES Stations(StationID),
	Arrival TIME,
	Departure TIME)

GO

insert into TrainTypes values
(1,'A',null),
(2,'B',null),
(3,'C',null);

insert into Trains values
(1,'TA',1),
(2,'TB',2),
(3,'TC',3),
(4,'TA2',1);

insert into Stations values
(1,'S1'),
(2,'S2'),
(3,'S3');

insert into Routes values
(1,'R1',1),
(2,'R2',2),
(3,'R3',3),
(4,'R4',4),
(5,'R5',1),
(6,'R6',1),
(7,'R7',2);

insert into RoutesStations values
(1,1,'5:10','5:30'),
(2,1,'5:10','6:10'),
(3,1,'6:10','7:10'),
(2,2,'6:10','6:40'),
(3,3,'10:20','10:40');

GO

CREATE OR ALTER PROC uspUpdateStationOnRoute
	(@RName VARCHAR(50), @SName VARCHAR(50), @Arrival TIME, @Departure TIME)
AS
	DECLARE @RouteID INT, @StationID INT
	IF NOT EXISTS (SELECT* FROM Routes WHERE RName = @RName)
	BEGIN
		RAISERROR('Invalid route name.',16,1)
		RETURN
	END
	IF NOT EXISTS (SELECT* FROM Stations WHERE SName = @SName)
	BEGIN
		RAISERROR('Invalid station name.',16,1)
		RETURN
	END

	SELECT @RouteID = (SELECT RouteID FROM Routes WHERE RName=@RName),
			@StationID = (SELECT StationID FROM Stations WHERE SName=@SName)

	IF EXISTS (SELECT * FROM RoutesStations WHERE RouteID=@RouteID AND StationID=@StationID)
		UPDATE RoutesStations
		SET Arrival=@Arrival,Departure=@Departure
		WHERE RouteID=@RouteID AND StationID=@StationID
	ELSE
		INSERT RoutesStations(RouteID,StationID,Arrival,Departure)
		VALUES(@RouteID,@StationID,@Arrival,@Departure)

--uspUpdateStationOnROute('r4', 's1', '7:00 AM', '7:10 AM') -- error
--uspUpdateStationOnROute('r1', 's4', '7:00 AM', '7:10 AM') -- error

EXEC uspUpdateStationOnROute 'r1', 's1', '7:00 AM', '7:10 AM'
EXEC uspUpdateStationOnROute 'r1', 's2', '7:20 AM', '7:30 AM'
EXEC uspUpdateStationOnROute 'r1', 's3', '7:40 AM', '7:50 AM'


SELECT * FROM TrainTypes
SELECT * FROM Trains
SELECT * FROM RoutesStations
SELECT * FROM Stations

GO

CREATE OR ALTER VIEW vRoutesWithAllStations
AS
SELECT R.RName
FROM Routes R
WHERE NOT EXISTS
	(SELECT StationID
	FROM Stations
	EXCEPT
	SELECT StationID
	FROM RoutesStations
	WHERE RouteID = R.RouteID)

GO

SELECT * FROM vRoutesWithAllStations

GO

CREATE OR ALTER FUNCTION ufFilterStationsByRoutes(@R INT)
RETURNS TABLE
RETURN
	SELECT SName
	FROM Stations
	WHERE StationID IN
		(SELECT StationID
		FROM RoutesStations
		GROUP BY StationID
		HAVING COUNT(*) > @R)

GO
 
 SELECT * FROM ufFilterStationsByRoutes (3)


		

