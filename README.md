# climata-snotel-gifs
Tweets a GIF every time there is substantial snowfall at Banner Summit SNOTEL site in Idaho, USA.

In summary, this python code runs at 11:55 each day on a Raspberry 4 Pi and checks whether or not there has been more than 1 inch (2.54 cm) of precipitation during the course of the day as measured by https://wcc.sc.egov.usda.gov/nwcc/site?sitenum=312. There is also a check to see this precipitation was actually snow. This is done by ensuring there has been at least 1 inch of snowdepth change for the day as well. If both of these conditions are met, a GIF is posted on Twitter page (https://twitter.com/GusBus14325867).
