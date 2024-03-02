USE Marvel_Universe;

--a. modify the type of a column
GO
CREATE OR ALTER PROCEDURE setDateOfBirthForBActorsFromDateToVarchar
AS
	ALTER TABLE BActors ALTER COLUMN Date_Of_Birth VARCHAR(50)

GO
CREATE OR ALTER PROCEDURE setDateOfBirthForBActorsFromVarcharToDate
AS
	ALTER TABLE BActors ALTER COLUMN Date_Of_Birth DATE


--b. add / remove a column

GO
CREATE OR ALTER PROCEDURE removeSalaryFromBActors
AS
	ALTER TABLE BActors DROP COLUMN Salary

GO
CREATE OR ALTER PROCEDURE addSalaryToBActors
AS
	ALTER TABLE BActors ADD Salary INT



-- c. add/remove a DEFAULT constraint

GO
CREATE OR ALTER PROCEDURE addDefaultToSalaryFromGActors
AS
	ALTER TABLE GActors ADD CONSTRAINT default_salary DEFAULT(1000) FOR salary

GO
CREATE OR ALTER PROCEDURE removeDefaultToSalaryFromGActors
AS
	ALTER TABLE GActors DROP CONSTRAINT default_salary


--g. create / drop a table
GO
CREATE OR ALTER PROCEDURE addSeries
AS
	CREATE TABLE Series
	(SID INT
	CONSTRAINT SERIES_PRIMARY_KEY PRIMARY KEY(SID),
	Release_year VARCHAR(50),
	BID INT NOT NULL,
	NameSeries VARCHAR(100) NOT NULL
	)

GO 
CREATE OR ALTER PROCEDURE dropSeries
AS
	DROP TABLE Series



-- d. add/remove a primary key

GO
CREATE OR ALTER PROCEDURE addNameSeriesPrimaryKeySeries
AS
	ALTER TABLE Series
		DROP CONSTRAINT SERIES_PRIMARY_KEY
	ALTER TABLE Series
		ADD CONSTRAINT SERIES_PRIMARY_KEY PRIMARY KEY(NameSeries)

GO 
CREATE OR ALTER PROCEDURE removeNameSeriesPrimaryKeySeries
AS
	ALTER TABLE Series
		DROP CONSTRAINT SERIES_PRIMARY_KEY
	ALTER TABLE Series
		ADD CONSTRAINT PK_Series PRIMARY KEY (SID);


-- e. add/remove a candidate key
GO
CREATE OR ALTER PROCEDURE newCandidateKeyFan 
AS	
	ALTER TABLE Fan
		ADD CONSTRAINT FAN_CANDIDATE_KEY UNIQUE(fan_name, fan_age, fan_country)

GO
CREATE OR ALTER PROCEDURE removeCandidateKeyFan
AS
	ALTER TABLE Fan
		DROP CONSTRAINT FAN_CANDIDATE_KEY


-- f. add / remove a foreign key
GO
CREATE OR ALTER PROCEDURE addForeignKeySeries
AS
	ALTER TABLE Series
		ADD CONSTRAINT SERIES_FOREIGN_KEY FOREIGN KEY(BID) REFERENCES Directors(DID)

GO
CREATE OR ALTER PROCEDURE removeForeignKeySeries
AS
	ALTER TABLE Series
		DROP CONSTRAINT SERIES_FOREIGN_KEY






-- a table that contains the current version of the database schema

CREATE TABLE versionTable (
	version INT
)


INSERT INTO versionTable 
VALUES
	(1) -- this is the initial version


-- a table that contains the initial version, the version after the execution of the procedure and the procedure that changes the table in this way
CREATE TABLE procedureTable (
	initial_version INT,
	final_version INT,
	procedure_name VARCHAR(MAX),
	PRIMARY KEY (initial_version, final_version)
)


INSERT INTO procedureTable
VALUES
	(1, 2, 'setDateOfBirthForBActorsFromDateToVarchar'),
	(2, 1, 'setDateOfBirthForBActorsFromVarcharToDate'),
	(2, 3, 'removeSalaryFromBActors'), 
	(3, 2, 'addSalaryToBActors'),
	(3, 4, 'addDefaultToSalaryFromGActors'),
	(4, 3, 'removeDefaultToSalaryFromGActors'),
	(4, 5, 'addSeries'),
	(5, 4, 'dropSeries'),
	(5, 6, 'addNameSeriesPrimaryKeySeries'),
	(6, 5, 'removeNameSeriesPrimaryKeySeries'),
	(6, 7, 'newCandidateKeyFan'),
	(7, 6, 'removeCandidateKeyFan'),
	(7, 8, 'addForeignKeySeries'),
	(8, 7, 'removeForeignKeySeries')
	



-- procedure to bring the database to the specified version
GO
CREATE OR ALTER PROCEDURE goToVersion(@newVersion INT) 
AS
	DECLARE @current_version INT
	DECLARE @procedureName VARCHAR(MAX)
	SELECT @current_version = version FROM versionTable

	IF (@newVersion > (SELECT MAX(final_version) FROM procedureTable) OR @newVersion < 1)
		RAISERROR ('Bad version', 10, 1)
	ELSE
	BEGIN
		IF @newVersion = @current_version
			PRINT('You are already on this version!');
		ELSE
		BEGIN
			IF @current_version > @newVersion
			BEGIN
				WHILE @current_version > @newVersion 
					BEGIN
						SELECT @procedureName = procedure_name FROM procedureTable WHERE initial_version = @current_version AND final_version = @current_version-1
						PRINT('Executing ' + @procedureName);
						EXEC (@procedureName)
						SET @current_version = @current_version - 1
					END
			END

			IF @current_version < @newVersion
			BEGIN
				WHILE @current_version < @newVersion 
					BEGIN
						SELECT @procedureName = procedure_name FROM procedureTable WHERE initial_version = @current_version AND final_version = @current_version+1
						PRINT('Executing ' + @procedureName);
						EXEC (@procedureName)
						SET @current_version = @current_version + 1
					END
			END

			UPDATE versionTable SET version = @newVersion
		END
	END

EXEC goToVersion 1

SELECT*
FROM BActors

SELECT *
FROM versionTable

SELECT *
FROM procedureTable