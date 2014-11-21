You've started a new movie-rating website, and you've been collecting data on reviewers' ratings of various movies. Here's the schema: 

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

1. Write an instead-of trigger that enables updates to the title attribute of view LateRating. 

Policy: Updates to attribute title in LateRating should update Movie.title for the corresponding movie. (You may assume attribute mID is a key for table Movie.) Make sure the mID attribute of view LateRating has not also been updated -- if it has been updated, don't make any changes. Don't worry about updates to stars or ratingDate.

CREATE TRIGGER Q1ViewCore
INSTEAD OF UPDATE OF title ON LateRating
FOR EACH ROW
WHEN New.mID = Old.mID
BEGIN
  UPDATE Movie
  SET title = New.title
  WHERE mID = Old.mID;
END;
----------------------------------------
2. Write an instead-of trigger that enables updates to the stars attribute of view LateRating. 

Policy: Updates to attribute stars in LateRating should update Rating.stars for the corresponding movie rating. (You may assume attributes [mID,ratingDate] together are a key for table Rating.) Make sure the mID and ratingDate attributes of view LateRating have not also been updated -- if either one has been updated, don't make any changes. Don't worry about updates to title.

CREATE TRIGGER Q2ViewCore
INSTEAD OF UPDATE OF stars ON LateRating
FOR EACH ROW
WHEN (New.mID = Old.mID AND New.ratingDate = Old.ratingDate)
BEGIN
  UPDATE Rating
  SET stars = New.stars
  WHERE mID = Old.mID AND ratingDate = Old.ratingDate;
END;
----------------------------------------
3. Write an instead-of trigger that enables updates to the mID attribute of view LateRating. 

Policy: Updates to attribute mID in LateRating should update Movie.mID and Rating.mID for the corresponding movie. Update all Rating tuples with the old mID, not just the ones contributing to the view. Don't worry about updates to title, stars, or ratingDate.

CREATE TRIGGER Q3ViewCore
INSTEAD OF UPDATE OF mID ON LateRating
FOR EACH ROW
WHEN (New.mID != Old.mID)
BEGIN
  UPDATE Movie SET mID = New.mID WHERE mID = Old.mID;
  UPDATE Rating SET mID = New.mID WHERE mID = Old.mID;
END;
----------------------------------------
4. Write an instead-of trigger that enables deletions from view HighlyRated. 

Policy: Deletions from view HighlyRated should delete all ratings for the corresponding movie that have stars > 3.

CREATE TRIGGER Q4ViewCore
INSTEAD OF DELETE ON HighlyRated
FOR EACH ROW
BEGIN
  DELETE FROM Rating WHERE stars > 3 AND mID = Old.mID;
END;
----------------------------------------
5. Write an instead-of trigger that enables deletions from view HighlyRated. 

Policy: Deletions from view HighlyRated should update all ratings for the corresponding movie that have stars > 3 so they have stars = 3.

CREATE TRIGGER Q5ViewCore
INSTEAD OF DELETE ON HighlyRated
FOR EACH ROW
BEGIN
  UPDATE Rating SET stars = 3 WHERE mID = Old.mID AND stars > 3;
END;
----------------------------------------
