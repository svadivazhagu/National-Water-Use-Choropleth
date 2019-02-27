# Assignment 4 - Visualization Remix
## Water Consumption in the United States, 2015
### [Surya Vadivazhagu](users.wpi.edu/~svadivazhagu), CS-480X'C19 @ WPI
### Spring 2019

---
## What?
I created an interactive choropleth map of the United States that displayed data from each county for the attributes of 

- County population
- County's daily use of water for domestic purposes, in gallons
- County's daily use of water for domestic purposes, per capita

All this data was obtained from a United States government data release from 2015 and cleaned using Python (Pandas) and visualized in the web using d3.js.

Check it out [here!](https://svadivazhagu.github.io/04-Remix/)

## Why?

[This](https://www.washingtonpost.com/news/energy-environment/wp/2015/03/17/the-incredibly-stupid-way-that-america-wastes-1-trillion-gallons-of-water-each-year/?noredirect=on&utm_term=.6d0a8d035822) New York Times article from 2015, titled *"The incredibly stupid way that Americans waste 1 trillion gallons of water each year"* proclaims how historically Americans have been very wasteful of fresh water, a precious resource that many countries globally have extremely limited access to. I was upset by this, as access to clean water is a struggle that one in ten Indians deal with. Being an Indian, I wanted to see the distribution of water use throughout the USA to gain a better understanding of what the *Times* article was discussing. In order to do this, there were three major phases of this project to make it possible.


## Inspiration Visualization

The map I chose to "remix" was constructed by the USGS ([United States Geological Survey](https://www.usgs.gov/)) using a data release supplied by them in 2015 for water consumption records by sector of water use per county. The original map is shown here:

![usgs_map](https://water.usgs.gov/watuse/images/category-pages/2015/total-withdrawals.png)

I chose this vis to remix because I didn't like how they didn't utilize the county-level data at all, instead only preferring to average the values and display it across a state-level. It really limits the amount of information that this dataset could communicate to a reader and doesn't have any interactivity at all. Plus, they used the basic `steelblue` color scale and while it is a valid sequential scheme, I thought (and made possible) there were better ways to color this data in response to the trends. 

---



## How?

### Obtaining the data

 I obtained the data from [here](https://www.sciencebase.gov/catalog/item/get/5af3311be4b0da30c1b245d8). It was downloadable as a csv.


### Cleaning the data

Cleaning the data was made possible using the `DataFrame` data structure in the Pandas Python 3 module. Essentially, I used the included Data Dictionary workbook in the Excel spreadsheet presented to me to determine which columns were of interest for this visualization project. Basically, I determined that I wanted to keep the population, daily groundwater use, and a few other columns (this is for the topoJSON module so that d3 would be able to know where each county was on the USA country map.) 

Another important thing I did was ensure that the data was used in the same scale- for example, originally the `population` attribute as measured by USGS was given in the unit of thousands of people, while the `daily_groundwater` attribute(and any other attribute dealing with water consumption) dealt in millions of gallons. This meant that in order to calculate the `per_capita` column that I created, I had to manipulate the water use columns and the population such that they were multiplied by 1 million and 1 thousand, respectively, such that they would be normalized down to 1 person and 1 gallon. 
Here's what the `head()` of the dataframe looked like before and after I cleaned it:

#### Before
![beforeCleaning](https://i.imgur.com/Hu4kSWw.png)
#### After
![afterCleaning](https://i.imgur.com/1UnbVHh.png)

Long story short, I cut the amount of data from 143 attributes to 6 attributes, and normalized all the metrics to be down to the single unit (from M/gal to gal and thousand of person to just person) and added my own column of water use per capita by using 2 other columns.

### Visualizing the data
I decided to do a choropleth map after taking a look at Mike Bostock's choropleth [map](https://observablehq.com/@d3/d3-choropleth) of unemployment rate in the USA in 2016. I realized that choropleth maps were great ways to show a large amount of data across a limited spatial axis. Since the country is the map itself, the other important thing was finding an accurate color scale/scheme that made perceptual differences in the data easy to visualize. Because of this, I took much care in choosing color maps that would accurately depict the data while preserving high perceptual differences between quantities. 

### Why I don't like border lines
You may notice that border lines for each county are missing in this visualization. I decided to remove them because the purpose of this choropleth map is to examine the distribution of water consumption across the United States; not to individually look at each county's water consumption. While this is possible thanks to the interactive tooltip, removing the border lines makes comprehending the graph's trends a lot easier. For example, with the population one you can see cities like the New York area and other cities(like Philadelphia, Atlanta, etc.) that stand out amongst neigbhoring, smaller counties are easily visible this way. Had borders been introduced, this perception would be much more challenging as the user would be examining the map county-by-county and failing to understanding the country-wide implications of the water consumption.

#### About the `Log()`
I used a logarithmically scaling function when calculating shades of color (in the `d3.scale`). This is because in this particular dataset, the values would often scale quite rapidly- for the `groundwater_per_day` attribute (county water use per day) the data would be distributed quite unevenly, with a large amount of small values, few values close to the average, and several extremely high values. Los Angeles County, the county drawing the most water for 2015, had close to 820 million gallons drawn a day, while the average water consumption was only 211,000 gallons. To prevent disparities in the shading of these data points, I used a `Math.log()` when calculating the domain to be passed on to the continuously mapping color scale. This ensured that **larger values would be emphasized less to allow for smaller differences between data points to become more visible through the color.**


#### About the <span style="color:steelblue">Colormaps</span>


- [*Cubehelix*](https://www.mrao.cam.ac.uk/~dag/CUBEHELIX/) - County population
  - This scheme was developed by Dave Green for implementation in the astronomy field. This scheme was developed out of a lack of color schemes that had an increase in "the perception of the brightness of the colours used". The cubehelix scheme is studied extensively in Dave Green's 2011 [paper](http://astron-soc.in/bulletin/11June/289392011.pdf) at Cambridge University. The breakthrough in color perception that Green brought on is introducing a color scale that monotonically increased in perceived brightness in response to values in the data. According to Green's research, the cubehelix scale is extremely efficient when it comes to noting the difference in items across a large set of items. I used it in this project for this very case. I knew that there are a lot of counties in the USA(~3000 are represented in my visualization) and thus understanding differences in population(an attribute that typically stays the same within given regions of land) would be made far easier. Users can examine the difference in perceived brightness and understand the meaning of the map easier, as it has been shown that humans are able to perceive light and color very well. Translating the challenge in cognition to just mapping the differences in brightness out makes the amount of time spent understanding the relationship between county populations across America much faster.
-   [*Magma*](https://bids.github.io/colormap/) - Groundwater consumption
    - The magma color scheme was designed by Stéfan van der Walt and Nathaniel Smith for the `matplotlib` maping library. These two scientists presented a [talk](https://www.youtube.com/watch?v=xAoljeRJ3lU) in 2015 regarding Scientific Computing with Python wherein they discussed the merits of their new color schemes. Essentially, their presentation was about designing a set of color scales that would not only be perceptually simple to measure differences in data but also comprehendable by people with color blindness. For the magma colormap specifically, they wanted to design a blue to red to yellow sequence as they found it was easy for those with colorblindness to read. Furthermore, they designed the scale such that it is 
    > analytically perfectly perceptually-uniform, both in regular form and also when converted to black-and-white.
    
This makes the interpretation of the scale feasible across many dimensions, which is why I chose it for this project. 

- [*Sinebow*](http://basecase.org/env/on-rainbows)
  - The sinebow is an interesting color scheme. While Munzner, in *Visualization Analysis & Design* does state that choropleth maps need to be represented by "sequentially segmented colormaps" (Munzner, p.181), I chose this color scheme, regardless of the fact that it is a cyclical scheme. This scheme came about Charlie Lloyd, one of its creators, realizing that on typical monitors, certain colors are harder to distinguish than others. In Lloyd's words, 
  > So we can’t use HSV like this when we want the colored elements to have anything close to equal visual weight against any solid background.

  Typically, the cyclical rainbow scheme is draw using the HSV colorspace however with the sinebow the transitions between colors are mapped much smoother and allow for a gradual difference in the data. I wanted to use this color scheme despite it being a cyclical one because according to Lloyd and the comparison between HSV and Sinebow that he created (shown below):

![hsv_sinebow](https://i.imgur.com/BiSdKWQ.png)

Essentially, the point that got me interested was with how the variances between each color is so smooth in Sinebow- look at the transition between the cyan and the blue, for example. In HSV it's very easy to see how they're segregated, but in Sinebow the transition is so smooth it's hard to spot this sort of boundary line. This means that variances of interest (variances between data points that are large enough to be of interest to the data scientist) are much easily noticed using the Sinebow pattern. I was able to prove this ease of visualization when the map showed that Utah as a state was the most using of fresh water, and [this](https://www.ksl.com/article/46345981/each-utahn-uses-an-average-of-242-gallons-of-water-per-day) article explains how the average Utahn uses the most amount of water per day than any other state. Both our datasets were different, and yet this observation was extremely simple to be made using my visualization through this sinebow scheme.

---


## Takeaways

There are a *lot* of takeaways from this visualization project. First and foremost is that the majority of Americans do in fact waste domestic water on a significant level. It was found that the most wasteful of counties was Rich County, UT, with an average of 710 gallons of water per capita every day. 
While these values are shocking and the trends easily visualizable through the choropleth map I made, there are definitely some next steps that could have been taken with this project had there been more time for its completion. First and foremost, I would have done some "next-steps" work in researching and attemping to visualize a breakdown of how people use their domestic water. This would require a much more specific dataset as the one provided by the USGS for 2015 only broke the consumption down to domestic, industrial, agricultural, etc. categories. Further insights could be drawn about how we as Americans use our water and ways we could lessen our water use responsibly.

I believe that my set of visualizations definetly reveals more information than the original USGS graph and allows for even more insights to be made through the use of my data synthesis and the unique colormaps I made use of for this project.


---

## Achievements

### Technical
- Complete data reshaping: I took a dataset that had over 140 columns and determined which ones I needed, stripped those from the original datset, and then created a new column, `per_capita` using the columns I had extracted.

- Interactivity through tooltips: I created an `onhover`-based tooltip system that helped users interact with the graphs to hover over the particular county they're interested in to reveal the value for that county, per the attribute whose graph they are currently on.
- Website runs smoothly- operations only run when the user calls for it. This means that the loading time for the website is extremely fast despite it rendering 3 d3 graphs.
  
- Data shaping of units to normalize to one standard unit: In the dataset the values were not equal in terms of the unit, they should be based around one unit of whatever metric was based off of; for example M/gal to gal or thousand people/individual person. I rewrote this and created a new csv using this system. 
- Creation of new column (not previously in USGS dataset) USGS should have done some research into water use per capita and strategies for minimizing water consumption. While I didn't have time to do the latter,  I definitely did the former and extracted daily water use alongside with population statistics to determine water use per capita per day for more insights to be drawn from the graphs.
- Minification of code to prevent security flaws/expose vulnerabilities and making it HTTPS by default: Security concerns are huge with web development and two things I did with my project- minifying the JavaScript code within the HTML to prevent external attackers reading it, and making it HTTPS to enhance the security and verifiability of the site.
- Creating logarithmic scaling for each data point to make interpretation of the vis more sensible and to ensure large quantities wouldn't be expressed so pronouncedly and emphasize the differences between small quantities. 




### Design
- Colormaps tailored to attribute: I spent a lot of time identifying colormaps whose scaling was most correlational to the scaling in the dataset I was working with. For example, data that fluctuates rapidly does not befit a cyclical colormap, which is why I didn't use Sinebow for the Daily Water Use category, but for the Per Capita graph instead, as the data is more balanced in terms of distribution with that column. 
  
- Scale for understanding: I provided a scale with the 0%, 50%, and 100% quantiles included to give a visual mapping to the data so viewers could generally get a feeling of what the quantifiable values were for the colors. While they can just hover over it to see the individual measurement, including a legend is important so they can get a general feel of how the data is shaped in overall.
  
- Text changing automatically in response to map selected: All the text ranging from the title to the subheading change in response to what option the user selects, ensuring that they see only relevant information.
- Research in perceptual differences in color channels to discover most efficient color scale with respect to variances in data: Going from the previous achievement about color scales, the actual scaling technique was also different in each colorscale. For example, the Cubehelix scaling is much slower in respect to the blues and greens than the magma color scale, which aims to make the differences between those colors more well known. 
- History of interaction with the visualization: So that the user can keep an interactive history of their interaction with the visualization, I added a black border around counties they have hovered on, as a sort of history for the user. They can keep track of where they've looked or make the border of the county well-defined this way. This solves the problem of being unable to individually distinguish a county's values due to the lack of border lines. The user can interact with the graph to select and highlight the border of the counties they've interacted with.

---

## Dataset Information & Citation

Dataset was obtained by downloading the .csv from the USGS website. A citation to the dataset used is presented as following:

Version 2.0:  Dieter, C.A., Linsey, K.S., Caldwell, R.R., Harris, M.A., Ivahnenko, T.I., Lovelace, J.K., Maupin, M.A., and Barber, N.L., 2018, Estimated use of water in the United States county-level data for 2015 (ver. 2.0, June 2018): U.S. Geological Survey data release, https://doi.org/10.5066/F7TB15V5.


Other papers referenced include:
"A colour scheme for the display of astronomical intensity
images" by D.A. Green (2011) accessible [here](http://astron-soc.in/bulletin/11June/289392011.pdf)

"Interactive maps for visual data exploration" by Andrienko et al. (1999) accessible [here](https://www.tandfonline.com/doi/pdf/10.1080/136588199241247?needAccess=true) that discuss how choropleth maps are very good for the analysis of data across geograpical locations, and the merits of strong color scales for this purpose.

"Mapping Mortality: Evaluating Color Schemes for Choropleth Maps" by Brewer et al. accessible [here](https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-8306.00061) that helped me determine what qualities were essential when finding a color map for choropleth maps in particular.