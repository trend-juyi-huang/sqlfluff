--Create Datasource Table with all optional syntax
CREATE TABLE IF NOT EXISTS table_identifier
( test STRING COMMENT "col_comment1" )
USING PARQUET
OPTIONS ( "key1" = "val1", "key2" = "val2")
PARTITIONED BY ( col_name1, col_name2 )
CLUSTERED BY ( col_name3, col_name4)
SORTED BY ( col_name3 ASC, col_name4 DESC)
INTO 4 BUCKETS
LOCATION 'root/database/table'
COMMENT 'this is a comment'
TBLPROPERTIES ( "key1" = "val1", "key2" = "val2" )
AS SELECT * FROM student;

--Use data source
CREATE TABLE student (id INT, student_name STRING, age INT) USING CSV;

--Use data from another table
CREATE TABLE student_copy USING CSV
AS SELECT * FROM student;

--Omit the USING clause
--uses the default data source (parquet by default)
CREATE TABLE student (id INT, student_name STRING, age INT);

--Specify table comment and properties
CREATE TABLE student (id INT, student_name STRING, age INT) USING CSV
COMMENT 'this is a comment'
TBLPROPERTIES ('foo' = 'bar');

--Create partitioned and bucketed table
CREATE TABLE student (id INT, student_name STRING, age INT)
USING CSV
PARTITIONED BY (age)
CLUSTERED BY (id) INTO 4 BUCKETS;
