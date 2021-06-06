# Policy Bear: Creating simple arguments from complex data.

[//]: # (Problem)
Finding concrete information on specific topics on the internet can be difficult: Facts and figures are poorly researched, taken out of context, manipulated, outdated or just in relation to a completely different time or place. What if there was a way to create arguments in no time by yourself, completely customised but with high scientific standard?

[//]: # (Description,)
Policy Bear is a simple, yet efficient tool for policymakers to get information on climatic environmental factors in a very compact and plain form.
We developed a prototype for a web interface to generate short and relatable sentences from climate data sets. It creates nice looking text graphics with a short sentence about the data and a comparison to a day to day measurement.
With our tool, users have the possibility to investigate environmental changes for desired regions and periods without any help or prior knowledge.   

Policy Bear began as a contribution to the *Hack the Arctic* hackathon and is now up and running at www.policybear.gregl.it.

[//]: # (Pathway)
Up to now it is possible to compare concentrations of greenhouse gases (carbon dioxide and methane) between different dates and observation stations within the ICOS Atmosphere network (Integrated Carbon Observation System). However, in the future it should also be possible to analyse gridded datasets.
Our simple structure allows us to easily integrate further parameters, which do not have to be limited to gases only, as long as meaningful comparisons are possible. For example, it is conceivable to compare changes in sea ice concentrations of certain regions with country areas or soccer fields.


[//]: # (Technical structure)
Data is directly loaded via Python Api of the ICOS data portal and processed in a flask-powered Python backend that is currently hosted on a Heroku server. The frontend is a Vue.js web app with Bootstrap styling hosted on a netlify server. API-calls are made dynamically so that changes to the generated
sentences can be seen instantly. Text graphics can be exported as images or shared via weblink.

[//]: # (Summery)
Policy Bear is a powerful, versatile and easy-to-use tool to quickly support statements with facts and figures.
With high scientific standard, users can easily create custom made arguments for their next conference meeting or the heated evening debate at the bar.
