1. Return the course number of the course that is cross-listed as "LING180".

doc("courses.xml")//Course[contains(Description, 'LING180')]/data(@Number)
----------------------------------------
2. Return course numbers of courses taught by an instructor with first name "Daphne" or "Julie".

doc("courses.xml")//Course[
Instructors//First_Name = 'Daphne' or Instructors//First_Name = 'Julie'
]/data(@Number)
----------------------------------------
3. Return titles of courses that have both a lecturer and a professor as instructors. Return each title only once.

doc("courses.xml")//Department//*[
    count(Instructors/Lecturer) > 0 and count(Instructors/Professor) > 0
]/Title
----------------------------------------
