1. Return all Title elements (of both departments and courses).
doc("courses.xml")//Title
----------------------------------------
2. Return last names of all department chairs.
doc("courses.xml")/Course_Catalog/Department/Chair/Professor/Last_Name
----------------------------------------
3. Return titles of courses with enrollment greater than 500. 
doc("courses.xml")//Course[@Enrollment > 500]/Title
----------------------------------------
4. Return titles of departments that have some course that takes "CS106B" as a prerequisite.
doc("courses.xml")//Department[Course/Prerequisites/Prereq = "CS106B"]/Title
----------------------------------------
5. Return last names of all professors or lecturers who use a middle initial. Don't worry about eliminating duplicates.
doc("courses.xml")//(Professor|Lecturer)[Middle_Initial]/Last_Name
----------------------------------------
6. Return the count of courses that have a cross-listed course (i.e., that have "Cross-listed" in their description).
count(doc("courses.xml")//Course_Catalog/Department/Course[contains(Description,"Cross-listed")])
----------------------------------------
7. Return the average enrollment of all courses in the CS department.
sum(doc("courses.xml")//Course_Catalog/Department[@Code="CS"]/Course/@Enrollment) 
div 
count(doc("courses.xml")//Course_Catalog/Department[@Code="CS"]/Course/@Enrollment)
----------------------------------------
8. Return last names of instructors teaching at least one course that has "system" in its description and enrollment greater than 100.
doc("courses.xml")//Course[contains(Description, 'system') and @Enrollment > 100]//Last_Name
----------------------------------------
