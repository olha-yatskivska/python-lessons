# Web Services

---

## Data on the Web

* Serialization is the process of converting an object in memory (e.g., a Python Dictionary, Java HashMap) into a stream of bytes (the "wire format") to be stored or transmitted. Deserialization is the reverse process.
* There are two commonly used formats: XML and JSON
* Agreeing on a "wire format": Flow: Python Dictionary -> Serialize  -> <XML/JSON> -> Network/Storage -> De-serialize -> Java HashMap 
---
## XML (eXtensible Markup Language)
* XML is designed to store and transport data, focusing on what data is rather than how it looks.
* Primary purpose is to help information system share structured data
* Structure: Hierarchical tree structure:
   * Root Element: The single parent element that contains all other elements.
   * Simple Element (Node): Contains only text, no child tags (Within one simple node you can only have one text element).
   * Complex Element (Node): Contains other elements (child tags) and/or attributes.
* Syntax Rules:
  *  **Tags** indicate the beginning and ending of elements
  *  **Attributes** - keyword/value pairs on the opening tag of XML
  *  **Whitespace** Generally ignored between elements (used for indentation/readability).  
---
## XML Schema
* Description of the legal format of an XML document
* Expressed in terms of constraints on the structure and content of documents
* Often used to specify a "contract" between systems
* If a paticular piece of XML meets the specification of the Schema - it is said to "validate"
---

## Many XML Schema Languages

* An XML Schema describes the legal format and structure of an XML document. It acts as a "contract" between two systems.

* Validation:
  * **Validate:** If an XML document meets the rules defined in the Schema, it is considered "valid".
  * **Purpose:**
    * Defines constraints on the structure (order of elements).
    * Defines constraints on the content (data types, values).

* **Schema Languages Types:**
   * Document Type Definition (DTD): Older, simpler syntax.
   * Standard GeneralizedbMarkup Language (ISO 8879:1986 SGML): The parent of XML (ISO 8879:1986).
   * XML Schema from W3C - (XSD): The W3C standard, written in XML syntax.

---
## W3C XSD (XML Schema Definition)
* The modern standard for defining XML structure. It is more powerful than DTD because it supports data types and namespaces.

## The Web Service Stack (SOAP)

> Hierarchy of Definitions: SOAP (Simple Object Access Protocol) -> XML (eXtensible Markup Language) ->
> XSD (XML Schema Definition) -> WSDL (Web Services Description Language)
---
## Key XSD Components
* **Structure Definitions:**
  *  xs:element : Defines an element.
  *  xs:sequence : Specifies that child elements must appear in a specific order.
  *  xs:complexType : Defines elements that contain attributes or other elements.

* **Cardinality Constraints (Occurrence):**
  * minOccurs: Minimum number of times an element must appear (Default is 1).
  * maxOccurs: Maximum number of times an element can appear.
  * ***Example:*** minOccurs="1" maxOccurs="1" means the element is required and unique.

* **Data Types:**
  * xs:string, xs:decimal, xs:integer, xs:boolean.
  * **Dates:** Follows [ISO 8601](https://www.w3.org/TR/NOTE-datetime) format (e.g., YYYY-MM-DDTHH:MM:SS).

* Enumeration: (xs:enumeration) Limits a value to a specific set of options.

## Code Examples:
* [Python parsing XML (One Element)](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/ex-xml1.py)
*  [Python parsing XML (Two Elements)](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/ex-xml2.py)
---

## [JSON](https://www.json.org/json-en.html) (JavaScript Object Notation)
* A lightweight data-interchange format that is easier for humans to read and write, and easier for machines to parse and generate than XML.
* **Structure:** Represents data as nested:
  * **Dictionaries (Objects):** Key/value pairs enclosed in {}.
  * **Lists (Arrays):** Ordered values enclosed in [].
* **Comparison:** JSON is less verbose than XML (no end tags) and maps directly to data structures in modern languages (JavaScript, Python).

## Code Examples:
* [Python with JSON dictionaries](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/json1.py) 
* [Python with JSON lists](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/json2.py)
---
## Service-Oriented Architecture (SOA) & APIs
* Most modern applications rely on a distributed network of services rather than being a single monolithic block.
* **Role of Services:** Applications consume data/functionality from other applications.
  * ***Examples:*** Credit Card processing (Stripe, PayPal), Hotel Reservation systems (Booking.com engine).
* **The API Contract:** Services publish an **API (Application Programming Interface)** which serves as the "rules" that consumers must follow to access the service.

## API & Geocoding References
[Google Maps API](https://developers.google.com/maps/documentation/geocoding/start)
[Geoapify Geocoding API](https://www.geoapify.com/geocoding-api/)
[OpenStreetMap](https://www.openstreetmap.org/#map=6/52.02/19.14)

## Code Examples:
[Heavily rate limited proxy of https://www.geoapify.com/ api](https://github.com/olha-yatskivska/python-lessons/blob/main/using-web-services/exercises/opengeo.py)
---

