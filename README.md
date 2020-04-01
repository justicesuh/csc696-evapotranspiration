# csc696-evapotranspiration

Estimated Mean Annual Ratio of Actual Evapotranspiration (ET) to Precipitation (P) for the Conterminous U.S. for the Period 1971-2000

*Sanford WE, Selnick DL (2013) Estimation of evapotranspiration across the conterminous United States using a regression with climate and land-cover data. J Am Water Resour Assoc 49(1):217–230*

The dataset included was manually recreated from the source diagram.

U.S. TopoJSON from [topojson/us-atlas](https://github.com/topojson/us-atlas)

`conus.py` removes Alaska and Hawaii from the original TopoJSON file.

Serve using `python -m http.server`