ou've started a new movie-rating website, and you've been collecting data on reviewers' ratings of various movies. Here's the schema: 

Movie ( mID, title, year, director ) 
English: There is a movie with ID number mID, a title, a release year, and a director. 

Reviewer ( rID, name ) 
English: The reviewer with ID number rID has a certain name. 

Rating ( rID, mID, stars, ratingDate ) 
English: The reviewer rID gave the movie mID a number of stars rating (1-5) on a certain ratingDate. 

In addition to the base tables, you've created three views: 

View LateRating contains movie ratings after January 20, 2011. The view contains the movie ID, movie title, number of stars, and rating date. 

create view LateRating as 
  select distinct R.mID, title, stars, ratingDate 
  from Rating R, Movie M 
  where R.mID = M.mID 
  and ratingDate > '2011-01-20' 

View HighlyRated contains movies with at least one rating above 3 stars. The view contains the movie ID and movie title. 

create view HighlyRated as 
  select mID, title 
  from Movie 
  where mID in (select mID from Rating where stars > 3) 

View NoRating contains movies with no ratings in the database. The view contains the movie ID and movie title. 

create view NoRating as 
  select mID, title 
  from Movie 
  where mID not in (select mID from Rating) 

1. Write a single instead-of trigger that enables simultaneous updates to attributes mID, title, and/or stars in view LateRating. Combine the view-update policies of the questions 1-3 in the core set, with the exception that mID may now be updated. Make sure the ratingDate attribute of view LateRating has not also been updated -- if it has been updated, don't make any changes.

CREATE TRIGGER Q2ViewChlg
INSTEAD OF UPDATE ON LateRating
FOR EACH ROW
WHEN Old.mID IN (SELECT mID FROM Rating WHERE ratingDate = new.ratingDate)
BEGIN
  UPDATE Movie SET title = New.title, mID = New.mID WHERE Old.mID = mID;
  UPDATE Rating SET stars = New.stars WHERE Old.mID = mID and ratingDate = Old.ratingDate;
  UPDATE Rating SET mID = New.mID WHERE  Old.mID = mID;
END;
----------------------------------------
2. Write an instead-of trigger that enables insertions into view HighlyRated. 

Policy: An insertion should be accepted only when the (mID,title) pair already exists in the Movie table. (Otherwise, do nothing.) Insertions into view HighlyRated should add a new rating for the inserted movie with rID = 201, stars = 5, and NULL ratingDate.

CREATE TRIGGER Q2ViewChlg
INSTEAD OF INSERT ON HighlyRated
FOR EACH ROW
WHEN EXISTS (SELECT mID, title FROM Movie WHERE mID = New.mID AND title = New.title)
BEGIN
  INSERT INTO Rating VALUES (201, New.mID, 5, NULL);
END;
----------------------------------------
3. Write an instead-of trigger that enables insertions into view NoRating. 

Policy: An insertion should be accepted only when the (mID,title) pair already exists in the Movie table. (Otherwise, do nothing.) Insertions into view NoRating should delete all ratings for the corresponding movie.

CREATE TRIGGER Q3ViewChlg
INSTEAD OF INSERT ON NoRating
FOR EACH ROW
WHEN EXISTS (SELECT mID, title FROM Movie WHERE mID = New.mID AND title = New.title)
BEGIN
  DELETE FROM Rating WHERE mID = New.mID;
END;
----------------------------------------
