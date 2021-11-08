# Project Writeup and Reflection

### Project Overview

This project utilized Flask to create a website that returned the nearest station to the user's location and whether it is wheelchair accessible or not. To begin with, we requested an API key for finding the coordinates (longitude and latitude) of a place and another API key for searching the nearest station based on the location provided. Next, we built the necessary functions under "mbta_helper.py".  After that, we built the templates for the website, including the main page, form page, and result page. Finally, we typed the code to merge the templates while importing Flask, render_template, and request in order to create the website. The extension that we added to the basic requirements is the maps API, where the user could see the location of the station itself.

### Project Reflection

During the process of building the code, the hardest part was being able to retrieve data from the MBTA and finding the URL to call in the data. Once we figured that out, it was pretty easy to index the correct data. Creating the map was also another challenging part of the project, as the source we used was javascript based and required us to figure out another programming language. And even after the code works, the source we used sometimes did not load the map data.

Our team finished this assignment by splitting the work and helping one another whenever one member was unable to proceed to the next stage. There were several issues that arose when working together, but the main issue that we faced was merging conflict. It was relatively difficult to work on the same function at the same time on two different devices. We addressed them by assigning each other different parts to work on and discussing before merging the code. Another problem that arose was the usage of different variable names. This resulted in our code not working out at the end even if we re-confirmed it multiple times. Another lesson learned here was to make an agreement on the variables' names at the beginning if we are given the opportunity to work together the next time.
