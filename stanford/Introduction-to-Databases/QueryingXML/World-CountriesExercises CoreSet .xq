1. Return the area of Mongolia. 

for $c in doc("countries.xml")//country[@name = 'Mongolia']/data(@area)
return $c
----------------------------------------
2. Return the names of all cities that have the same name as the country in which they are located. 

for $country in doc("countries.xml")/countries/country
for $city in $country/city
where $country/data(@name) = $city/name
return $city/name
----------------------------------------
3. Return the average population of Russian-speaking countries.

for $avg in avg(doc("countries.xml")/countries/country[language = 'Russian']/data(@population))
return $avg
----------------------------------------
4. Return the names of all countries where over 50% of the population speaks German. (Hint: Depending on your solution, you may want to use ".", which refers to the "current element" within an XPath expression.)

for $country in doc("countries.xml")/countries/country
where $country/language[data(.) = 'German' and @percentage > 50]
return $country/data(@name)
----------------------------------------
5. Return the name of the country with the highest population. (Hint: You may need to explicitly cast population numbers as integers with xs:int() to get the correct answer.)

let $countries := doc("countries.xml")/countries
for $country in $countries/country
where $country[@population = max($countries/country/data(@population))]
return $country/data(@name)
----------------------------------------
