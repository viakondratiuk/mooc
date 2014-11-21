1. Return the title of the course with the largest enrollment.
 
doc("courses.xml")//Course[
@Enrollment 
and 
not(@Enrollment > following::*/data(@Enrollment)) 
and 
not(@Enrollment > preceding::*/data(@Enrollment))
]/Title
----------------------------------------
2. Return course numbers of courses that have the same title as some other course. (Hint: You might want to use the "preceding" and "following" navigation axes for this query, which were not covered in the video or our demo script; they match any preceding or following node, not just siblings.) 

doc("courses.xml")//Course[
preceding::Title = Title or following::Title =Title
]/data(@Number)
----------------------------------------
3. Return the number (count) of courses that have no lecturers as instructors.

count(doc("courses.xml")//Course[Instructors[count(Lecturer) = 0]]/Title)
----------------------------------------
4. Return titles of courses taught by the chair of a department. For this question, you may assume that all professors have distinct last names.

doc("courses.xml")//Course[
Instructors/Professor/Last_Name = //Department/Chair/Professor/Last_Name
]/Title
----------------------------------------
5. Return titles of courses taught by a professor with the last name "Ng" but not by a professor with the last name "Thrun". 

doc("courses.xml")//Course[
Instructors/Professor/Last_Name = 'Ng' 
and 
count(Instructors/Professor[Last_Name = 'Thrun']) = 0
]/Title
----------------------------------------
6. Return course numbers of courses that have a course taught by Eric Roberts as a prerequisite. 

doc("courses.xml")//Course[
Prerequisites/Prereq = 
doc("courses.xml")//Course[Instructors//Last_Name = 'Roberts']/data(@Number)
]/data(@Number)
----------------------------------------
7. Create a summary of CS classes: List all CS department courses in order of enrollment. For each course include only its Enrollment (as an attribute) and its Title (as a subelement).

let $catalog := doc('courses.xml'),
$courses := $catalog//Department[@Code = 'CS']/Course
return <Summary> 
  {
    for $course in $courses
      order by xs:int($course/@Enrollment)
      return <Course Enrollment = "{$course/data(@Enrollment)}">{$course/Title}</Course>
  }
</Summary>
----------------------------------------
8. Return a "Professors" element that contains as subelements a listing of all professors in all departments, sorted by last name with each professor appearing once. The "Professor" subelements should have the same structure as in the original data. For this question, you may assume that all professors have distinct last names. Watch out -- the presence/absence of middle initials may require some special handling. (This problem is quite challenging; congratulations if you get it right.)

let $catalog := doc('courses.xml'),
  $professors := $catalog//Professor

let $distinct_prof := (
      $professors except (
        for $p in $professors
          where ($p/Last_Name = $p/following::*/Last_Name and $p/First_Name = $p/following::*/First_Name)
          return $p
      )
    )

return <Professors>
  {
    for $p in $distinct_prof
    order by $p/Last_Name
    return $p
  }
  </Professors>
----------------------------------------
----------------------------------------
----------------------------------------
