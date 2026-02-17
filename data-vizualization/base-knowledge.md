# Retrieving and Visualizing Data

## Many Data Mining Technologies
* https://hadoop.apache.org/
* http://spark.apache.org
* https://aws.amazon.com/redshift/
* http://community.pentaho.com/

---

## OpenGeo
* Makes an annotated Open Street Map from user entered data
* Uses the proxied GeoAPI API
* Caches data in a database to avoid rate limiting and allow restarting
* Visualized in a browser using the Open Street Map
---
```
                       where.data
                           |
Open Street Map data -> geoload.py -> geodata.sqlite
                                            |
                                      geodump.py -> where.js -> where.html
```
---
[Worked Example: OpenGeo]()
