use practic2
DROP TABLE Exhibition
CREATE TABLE Producer
	(ProducerID INT PRIMARY KEY,
	PName Varchar(50),
	PhoneNr Varchar(50),
	Website Varchar(50));

CREATE TABLE Model
	(ModelID INT PRIMARY KEY,
	MName Varchar(50),
	MDescription Varchar(50),
	ProducerID INT FOREIGN KEY REFERENCES Producer(ProducerID));

CREATE TABLE Client
	(ClientID INT PRIMARY KEY,
	CName Varchar(50),
	CPhoneNr Varchar(50),
	Age INT);

CREATE TABLE Purchase
	(PurchaseID INT PRIMARY KEY,
	PDate DATE,
	Price INT,
	ProducerID INT FOREIGN KEY REFERENCES Producer(ProducerID),
	ClientID INT FOREIGN KEY REFERENCES Client(ClientID));

CREATE TABLE Showroom
	(ShowroomID INT PRIMARY KEY,
	SName Varchar(50),
	SPhoneNr Varchar(50),
	SWebsite Varchar(50));

	
CREATE TABLE Exhibition
	(ExhibitionD INT PRIMARY KEY,
	Availability INT,
	ShowroomID INT FOREIGN KEY REFERENCES Showroom(ShowroomID),
	ModelID INT FOREIGN KEY REFERENCES Model(ModelID));

insert into Producer values
(2 ,'Name2', 'ceswcd','vcfeds');

insert into Model values
(1,'Name1', 'Descr1',1),
(2,'Name2', 'Descr2',1);




SELECT * FROM Model
SELECT * FROM Producer

