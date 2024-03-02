use Lab1

go
DROP TABLE Trains
DROP TABLE TrainTypes



GO

CREATE TABLE TrainTypes
	(TrainTypeID INT PRIMARY KEY,
	TTName Varchar(50),
	TTDescription Varchar(50));

go

CREATE TABLE Trains
	([TrainID] INT PRIMARY KEY,
	TName Varchar(50),
	TrainTypeId INT FOREIGN KEY REFERENCES TrainTypes(TrainTypeID));

go 

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


select* from Trains
select* from TrainTypes
select* from Routes
select* from RoutesStations
select* from Stations
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


