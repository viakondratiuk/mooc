1. Return the names of all countries that have at least three cities with population greater than 3 million.

let $countries := doc("countries.xml")/countries
for $country in $countries/country
where count($country/city[population > 3000000]) > 2
return $country/data(@name)
----------------------------------------
2. Create a list of French-speaking and German-speaking countries. The result should take the form:
<result>
  <French>
    <country>country-name</country>
    <country>country-name</country>
    ...
  </French>
  <German>
    <country>country-name</country>
    <country>country-name</country>
    ...
  </German>
</result>

<result>
<French>
{
for $country in doc("countries.xml")//country
where $country/language = 'French'
return <country>{$country/data(@name)}</country>
}
</French>
<German>
{
for $country in doc("countries.xml")//country
where $country/language = 'German'
return <country>{$country/data(@name)}</country>
}
</German>
</result>
----------------------------------------
3. Return the names of all countries containing a city such that some other country has a city of the same name. (Hint: You might want to use the "preceding" and/or "following" navigation axes for this query, which were not covered in the video or our demo script; they match any preceding or following node, not just siblings.)

let $countries := doc('countries.xml')/countries/country,
  $cities := $countries//city
  for $c in $cities
    where $c/data(name) = $c/following::*/data(name) or
      $c/data(name) = $c/preceding::*/data(name)
    return $c/parent::country/data(@name)
----------------------------------------
4. Return the average number of languages spoken in countries where Russian is spoken.

let $countries := doc('countries.xml')/countries/country
return avg($countries[language = 'Russian']/count(language))
----------------------------------------
5. Return all country-language pairs where the language is spoken in the country and the name of the country textually contains the language name. Return each pair as a country element with language attribute, e.g.,
<country language="French">French Guiana</country>

let $countries := doc('countries.xml')/countries/country
for $country in $countries
  for $lang in $country/language
    where contains($country/data(@name), $lang)
    return <country language="{data($lang)}">{$country/data(@name)}</country>
----------------------------------------
6. Return all countries that have at least one city with population greater than 7 million. For each one, return the country name along with the cities greater than 7 million, in the format:
<country name="country-name">
  <big>city-name</big>
  <big>city-name</big>
  ...
</country>

let $countries := doc('countries.xml')/countries/country
for $c in $countries
  where count($c/city[population > 7000000]) > 0
  return 
    <country name="{$c/data(@name)}">
    {
      for $city in $c/city
        where $city[population > 7000000]
        return <big>{$city/data(name)}</big>
    }
    </country>
----------------------------------------
7. Return all countries where at least one language is listed, but the total percentage for all listed languages is less than 90%. Return the country element with its name attribute and its language subelements, but no other attributes or subelements.

let $countries := doc('countries.xml')/countries/country
for $c in $countries[language]
  where sum($c/language/data(@percentage)) < 90
  return 
    <country name="{$c/data(@name)}">
    {
      for $l in $c/language
      return $l
    }
    </country>
----------------------------------------
8. Return all countries where at least one language is listed, and every listed language is spoken by less than 20% of the population. Return the country element with its name attribute and its language subelements, but no other attributes or subelements.

let $countries := doc('countries.xml')/countries/country
for $c in $countries[language]
  where every $l in $c/language satisfies $l/data(@percentage) < 20
  return 
    <country name="{$c/data(@name)}">
    {
      for $l in $c/language
      return $l
    }
    </country>
----------------------------------------
9. Find all situations where one country's most popular language is another country's least popular, and both countries list more than one language. (Hint: You may need to explicitly cast percentages as floating-point numbers with xs:float() to get the correct answer.) Return the name of the language and the two countries, each in the format:
<LangPair language="lang-name">
  <MostPopular>country-name</MostPopular>
  <LeastPopular>country-name</LeastPopular>
</LangPair>

let $countries := doc('countries.xml')/countries/country,
  $most_popular := 
    for $c in $countries[count(language) > 1]
      for $l in $c/language
        where xs:float($l/data(@percentage)) = xs:float(max($c/language/data(@percentage)))
        return $l,

  $least_popular := 
    for $c in $countries[count(language) > 1]
      for $l in $c/language
        where xs:float($l/data(@percentage)) = xs:float(min($c/language/data(@percentage)))
        return $l

  for $m in $most_popular
    for $l in $least_popular
      where data($m) = data($l)
        return
          <LangPair language="{data($l)}">
            <MostPopular>{$m/parent::country/data(@name)}</MostPopular>
            <LeastPopular>{$l/parent::country/data(@name)}</LeastPopular>
          </LangPair>
----------------------------------------
10. For each language spoken in one or more countries, create a "language" element with a "name" attribute and one "country" subelement for each country in which the language is spoken. The "country" subelements should have two attributes: the country "name", and "speakers" containing the number of speakers of that language (based on language percentage and the country's population). Order the result by language name, and enclose the entire list in a single "languages" element. For example, your result might look like:
<languages>
  ...
  <language name="Arabic">
    <country name="Iran" speakers="660942"/>
    <country name="Saudi Arabia" speakers="19409058"/>
    <country name="Yemen" speakers="13483178"/>
  </language>
  ...
</languages>

let $countries := doc('countries.xml')/countries/country,
  $languages := $countries/language,
  $language_names := distinct-values($countries/data(language))
  return 
  <languages>
  {
    for $l_name in $language_names
      order by $l_name
      return 
        <language name="{$l_name}">
        {
          for $l in $languages
            where data($l) = $l_name
            return <country name="{data($l/parent::country/@name)}" speakers="{xs:int($l/parent::country/@population * $l/@percentage div 100) }"/>
        }
        </language>
  }
  </languages>
----------------------------------------
----------------------------------------
