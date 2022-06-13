-- TABLE
CREATE TABLE City (
    Cityid int NOT NULL,
    Name varchar(255) NOT NULL,
  	Countryid Int NOT NULL,
    PRIMARY KEY (Cityid)
  	FOREIGN KEY (Countryid) REFERENCES Country(Countryid)
);
CREATE TABLE County (
    Countryid int NOT NULL,
    Name varchar(255) NOT NULL,
    PRIMARY KEY (Countryid)
);
CREATE TABLE demo (ID integer primary key, Name varchar(20), Hint text );
 
-- INDEX
 
-- TRIGGER
 
-- VIEW
 
