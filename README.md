# Policy Bear

Our contribution to the Hack The Arctic Hackathon

+ We developed a prototype for a web interface to generate short and relatable sentences  from climate data sets to use them in the next conference or meeting (that starts in only 10 minutes).

+ The web interface enables policy-makers to create nice looking text graphics with a short sentence about the data and a comparison to a day to day measurement.

## Policy-makers can pick...

+ a dataset (we included a methane and a carbon dioxide data set from Barrow Atmospheric Baseline Observatory https://www.esrl.noaa.gov/gmd/dv/iadv/graph.php?code=BRW&program=ccgg&type=ts())
+ a timeframe to compare the values (in what range years are available depends on the dataset)
+ a wording (we included three different wordings)
+ a day to day measurement to compare to (we included cows and cars ;D)
+ a styling theme (we included three beautiful themes!)

## Technical details

### Backend

+ The data is processed in a flask-powered Python backend that we hosted on a Heroku server.
+ The flask server can process API-calls to access specific values from the chosen dataset.
+ Our python-based backend makes it easy to add all of your favorite datasets in the future.

### Frontend

+ The frontend is a Vue.js web app with Bootstrap styling hosted on a netlify server.
+ All relevant information about available datasets, timeframes and other options are retrieved vie API-calls so that no editing in the frontend is needed to add new data!
+ The API-calls are made dynamically so that changes to the generated sentences can be seen instantly!

### Data

+ We processed the data by taking annual means over all datapoints of a year to make it simple.
+ The day to day measurements comparisons are very rough estimates on the basis of general data so don't expect the most meanigful values. ;)



image source: https://perditus.blog/2020/11/05/the-ice-kingdom/


