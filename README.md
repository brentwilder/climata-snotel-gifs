# climata-snotel-gifs
Tweets a GIF every time there is substantial snowfall at Banner Summit SNOTEL site in Idaho, USA.

In summary, this python code runs at 11:55PM MST each day on a Raspberry 4 Pi and checks whether or not there has been more than 0.2 inch (0.5 cm) of snowfall during the course of the day as measured by https://wcc.sc.egov.usda.gov/nwcc/site?sitenum=312. There is also a check to see if SWE increased. If both of these conditions are met, a GIF is posted on the Twitter page (https://twitter.com/GusBus14325867).


![312](https://www.wcc.nrcs.usda.gov/siteimages/312.jpg)
