1. Return all countries with population between 9 and 10 million. Retain the structure of country elements from the original data. 

Your solution should fill in the following stylesheet: 
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match=...>
            ... template body ...
        </xsl:template>
        ... more templates as needed ...
    </xsl:stylesheet>

<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="country[@population &gt; 9000000 and @population &lt; 10000000]">
        <xsl:copy-of select="." />
    </xsl:template>
    <xsl:template match="text()"/>
</xsl:stylesheet>
----------------------------------------
2. Find all country names containing the string "stan"; return each one within a "Stan" element. (Note: To specify quotes within an already-quoted XPath expression, use quot;.) 

Your solution should fill in the following stylesheet: 
    <?xml version="1.0" encoding="ISO-8859-1"?>
    <xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <xsl:template match=...>
            ... template body ...
        </xsl:template>
        ... more templates as needed ...
    </xsl:stylesheet>

<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet version="2.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="country[contains(@name, 'stan')]">
        <Stan><xsl:value-of select="@name" /></Stan>
    </xsl:template>
    <xsl:template match="text()"/>
</xsl:stylesheet>
----------------------------------------
