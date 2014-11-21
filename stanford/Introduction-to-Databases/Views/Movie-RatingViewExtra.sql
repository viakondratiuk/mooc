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

1. Write an instead-of trigger that enables deletions from view NoRating. 

Policy: Deletions from view NoRating should delete the corresponding movie from the Movie table.

CREATE TRIGGER Q1ViewExtra
INSTEAD OF DELETE ON NoRating
FOR EACH ROW
BEGIN
  DELETE FROM Movie WHERE mID = Old.mID;
END;
----------------------------------------
2. Write an instead-of trigger that enables deletions from view NoRating. 

Policy: Deletions from view NoRating should add a new rating for the deleted movie with rID = 201, stars = 1, and NULL ratingDate.

CREATE TRIGGER Q2ViewExtra
INSTEAD OF DELETE ON NoRating
FOR EACH ROW
BEGIN
  INSERT INTO Rating VALUES (201, Old.mID, 1, NULL);
END;
----------------------------------------
