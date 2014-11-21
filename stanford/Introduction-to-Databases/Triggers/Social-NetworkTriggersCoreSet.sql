1. Write a trigger that makes new students named 'Friendly' automatically like everyone else in their grade. That is, after the trigger runs, we should have ('Friendly', A) in the Likes table for every other Highschooler A in the same grade as 'Friendly'.

CREATE TRIGGER Q1Core
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (New.name = 'Friendly')
BEGIN
  INSERT INTO Likes 
  SELECT New.ID, ID FROM Highschooler WHERE New.grade = grade AND ID != new.ID;
END;
----------------------------------------
2. Write one or more triggers to manage the grade attribute of new Highschoolers. If the inserted tuple has a value less than 9 or greater than 12, change the value to NULL. On the other hand, if the inserted tuple has a null value for grade, change it to 9. 
Your triggers are created in SQLite, so you must conform to the trigger constructs supported by SQLite.
To create more than one trigger, separate the triggers with a vertical bar (|).

CREATE TRIGGER Q2aCore
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (New.grade < 9 OR New.grade > 12)
BEGIN
  UPDATE Highschooler SET grade = NULL WHERE ID = New.ID;
END;
|
CREATE TRIGGER Q2bCore
AFTER INSERT ON Highschooler
FOR EACH ROW
WHEN (New.grade IS NULL)
BEGIN
  UPDATE Highschooler SET grade = 9 WHERE ID = New.ID;
END;
----------------------------------------
3. Write a trigger that automatically deletes students when they graduate, i.e., when their grade is updated to exceed 12. 

CREATE TRIGGER Q3Core
AFTER UPDATE ON Highschooler
FOR EACH ROW
WHEN (New.grade > 12)
BEGIN
  DELETE FROM Highschooler WHERE ID = New.ID;
END;
----------------------------------------
