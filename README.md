# Policy Bear

[![](/img/policybear_v1.2.png)](https://www.policybear.gregl.it)

Our contribution to [*Hack the Arctic*](https://hackthearctic.com), a hackathon to design solutions for environmental challenges.

The **Policy Bear** is up and running at [www.policybear.gregl.it](https://policybear.gregl.it).

+ We developed a prototype for a web interface to generate short and relatable sentences  from climate data sets to use them in the next conference or meeting (that starts in only 10 minutes).
+ The web interface enables policy-makers to create nice looking text graphics with a short sentence about the data and a comparison to a day to day measurement.

## Policy-makers are able to ...

+ compare concentrations of greenhouse gases (carbon dioxide and methane) between different dates and observation stations within the [ICOS Atmosphere network](https://www.icos-cp.eu/observations/atmosphere/stations) (Integrated Carbon Observation System).
+ select a timeframe with either annual or monthly steps (range depends on the dataset availability)
+ compare absolute or relative changes
+ compare change with day-to-day measurements (we included cows and cars)
+ export results as pdf or jpeg in three different beautiful themes
+ share results with colleges and friends

## Technical details

### Backend

+ The data is processed in a flask-powered Python backend that we hosted on a Heroku server.
+ The data is loaded directly via a [Python Api](https://icos-carbon-portal.github.io/pylib/) of the [ICOS data portal](https://data.icos-cp.eu/portal/#{%22filterCategories%22%3A{%22project%22%3A[%22icos%22]}}).
+ The flask server can process API-calls to access specific values from the chosen dataset.
+ Our python-based backend makes it easy to add all of your favourite datasets in the future.

### Frontend

+ The frontend is a Vue.js web app with Bootstrap styling hosted on a netlify server.
+ All relevant information about available datasets, timeframes and other options are retrieved vie API-calls so that no editing in the frontend is needed to add new data!
+ The API-calls are made dynamically so that changes to the generated sentences can be seen instantly!

### Data

+ We processed the data by taking means over all datapoints within the target period.
+ Although data is available at different heights our algorithm is currently still limited to the measurement at lowest height.
+ The day to day measurements comparisons are very rough estimates on the basis of general values so don't expect the most meaningful values.

## Further Development

+ Select available ICOS stations via map viewer.
+ Adding more and improving the currently available parameters to compare to.
+ Including gridded datasets and more parameters (such as sea ice cover)
+ Better algorithm to make comparisons more reliable.
+ Improving interface and user experience of our website.
