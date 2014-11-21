1. Return the names of all countries with population greater than 100 million.

let $countries := doc("countries.xml")/countries
return $countries/*[@population > 100000000]/data(@name) 
----------------------------------------
2. Return the names of all countries where a city in that country contains more than one-third of the country's population.

let $countries := doc("countries.xml")/countries
return $countries/country[city/population > @population div 3]/data(@name)
----------------------------------------
3. Return the population density of Qatar. Note: Since the "/" operator has its own meaning in XPath and XQuery, the division operator is "div". To compute population density use "(@population div @area)".

let $country := doc("countries.xml")//country[@name='Qatar']
return $country/data(@population div @area) 
----------------------------------------
