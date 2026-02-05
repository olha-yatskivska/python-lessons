# Web Services

---

## Data on the Web
* There are two commonly used formats: XML and JSON
* Agreeing on a "wire format": python dictionary -> serialize  -> <person> -> de-serialize -> Java HashMap (XML, JSON)
---
## XML - eXtensible Markup Language
* Primary purpose is to help information system share structured data
*  **Tags** indicate the beginning and ending of elements
*  **Attributes** - keyword/value pairs on the opening tag of XML
*  **Serialize/De-Serialize** - Convert data in on program into a common format that can be stored and/or transmitted between systems in a programming language-independent manner
*  White space is generally discarded on test elements/ We indent only to be readable
* There is a hierarchical stucture within an XML document: simple element (node), complex element (node) with child tags
* Within one simple node you can only have one text element.
---
## XML Schema
* Description of the legal format of an XML document
* Expressed in terms of constraints on the structure and content of documents
* Often used to specify a "contract" between systems
* If a paticular piece of XML meets the specification of the Schema - it is said to "validate"
---

## Many XML Schema Languages
* Description of the legal format of an XML document
* Expressed in terms of constraints on the structure and content of documents 
* Types:
   * Document Type Definition (DTD)
   * Standard GeneralizedbMarkup Language (ISO 8879:1986 SGML)
   * XML Schema from W3C - (XSD)

---
## XML Schema from W3C - (XSD) 

> SOAP (Simple Object Access Protocol) -> XML (eXtensible Markup Language) ->
> XSD (XML Schema Definition) -> WSDL (Web Services Description Language)
---
* **XSD Structure:** xs:element, xs:sequence, xs:complexType
* **XSD Constraints:** minOcuurs & maxOccurs (if  minOcuurs="1" maxOccurs="1" - it's required)
* **XSD Data Types:** string, date, dateTime, decimal, integer
* [ISO 8601 Date/Time Format](https://www.w3.org/TR/NOTE-datetime) in [Wiki](https://en.wikipedia.org/wiki/ISO_8601)
* Have items and attributes [Program with one element](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/ex-xml1.py) [Program with two elements](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/ex-xml2.py)
---

## JSON 
* JSON represents dta as nested "lists" and "dictionaries"
[Program with dictionaries](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/json1.py) , [Program with lists](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/json2.py)
---
## Srvice Oriented Approach
* Most non-trivial web applications use services
* They use services from other applications:
   * Credit Card Charge
   * Hotel Reservation systems
* Services publish the "rules" applications must follow to make use of the service (API)

---

