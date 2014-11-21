1. Write one or more triggers to maintain symmetry in friend relationships. Specifically, if (A,B) is deleted from Friend, then (B,A) should be deleted too. If (A,B) is inserted into Friend then (B,A) should be inserted too. Don't worry about updates to the Friend table.

CREATE TRIGGER Q1aChl
AFTER DELETE ON Friend
FOR EACH ROW
BEGIN
  DELETE FROM Friend WHERE ID1 = Old.ID2 AND ID2 = Old.ID1;
END;
|
CREATE TRIGGER Q1bChl
AFTER INSERT ON Friend
FOR EACH ROW
BEGIN
  INSERT INTO Friend VALUES (New.ID2, New.ID1);
END;
----------------------------------------
2. Write a trigger that automatically deletes students when they graduate, i.e., when their grade is updated to exceed 12. In addition, write a trigger so when a student is moved ahead one grade, then so are all of his or her friends.

CREATE TRIGGER Q2aChl
AFTER UPDATE ON Highschooler
FOR EACH ROW
WHEN (New.grade > 12)
BEGIN
  DELETE FROM Highschooler WHERE ID = New.ID;
END;
|
CREATE TRIGGER Q2bChl
AFTER UPDATE ON Highschooler
FOR EACH ROW
WHEN (New.grade = Old.grade + 1)
BEGIN
  UPDATE Highschooler SET grade = grade + 1
  WHERE ID IN (
    SELECT DISTINCT ID2 FROM Friend WHERE ID1 = New.ID
  );
END;
----------------------------------------
3. Write a trigger to enforce the following behavior: If A liked B but is updated to A liking C instead, and B and C were friends, make B and C no longer friends. Don't forget to delete the friendship in both directions, and make sure the trigger only runs when the "liked" (ID2) person is changed but the "liking" (ID1) person is not changed.  

CREATE TRIGGER Q3Chl
AFTER UPDATE OF ID2 ON LIKES
FOR EACH ROW
WHEN (Old.ID1 = New.ID1)
BEGIN
  DELETE FROM Friend 
  WHERE (ID1 = Old.ID2 AND ID2 = New.ID2) OR (ID1 = New.ID2 AND ID2 = Old.ID2);
END;
----------------------------------------
