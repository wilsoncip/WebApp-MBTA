# Project Writeup and Reflection

### Project Overview
[~1 paragraph]
<!-- Write a short abstract describing your project. Include all the extensions to the basic requirements. -->

This project utilized Flask to create a website that returned the nearest station to the user's location and whether it is wheelchair accessible or not. The basic extension requirements are render_template and request. To begin with, we need to request API key for finding the coordinates (longitude and latitude) of a place and another API key for searching the nearest station based on the location provided. Next, we need to build the necessary functions under "mbta_helper.py"  Finally, we build the templates for the website and code to build the website under "app.py". 

### Project Reflection

<!-- After you finish the project, Please write a short document for reflection [~2 paragraphs]

From a process point of view, what went well? What could you improve? Other possible reflection topics: Was your project appropriately scoped? Did you have a good plan for unit testing? What self-studying did you do? How will you use what you learned going forward? What do you wish you knew before you started that would have helped you succeed?\


Also discuss your team process in your reflection. How did you plan to divide the work (e.g. split by class, always pair program together, etc.) and how did it actually happen? Were there any issues that arose while working together, and how did you address them? What would you do differently next time? -->

During the process of building the code, the hardest part was being able to retrieve data from the MBTA and finding the url to call in the data. Once we figured that out, it was pretty easy to index the correct data. Creating the map was also another challenging part of the project, as the source we used was javascript based and required us to figure out another programming language. And even after the code works, the source we used sometimes did not load the map data.

Our team finished this assignment by splitting the work and helping one another whenever one member was unable to proceed to the next stage. There were several issues that arose when working together, but the main issue that we faced was merge conflict. It was relatively difficult to work on the same function at the same time in two different devices. We addressed them by asigning each other different part to work on and discussing before merging the code. Another problem that arose was the usage of different variable names. This resulted in our code not working out at the end even if we re-confirmed multiple times. Another lesson learned here was to make an agreement on the variables names at the beginning if we are given the opportunity to work together the next time. 
