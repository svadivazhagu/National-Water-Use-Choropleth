# Assignment 4 - Visualization Remix
## Per-Country Fresh Water Consumption, 2015
### [Surya Vadivazhagu](users.wpi.edu/~svadivazhagu), CS-480X'C19 @ WPI
### Spring 2019

---
## What?
I created a choropleth map of the United States that displayed data from each county for the attributes of 

- County population
- County's daily use of water for domestic purposes, in gallons
- County's daily use of water for domestic purposes, per capita

All this data was obtained from a United States government data release from 2015 and cleaned using Python (Pandas) and visualized in the web using d3.js.

Check it out [here!](https://svadivazhagu.github.io/04-Remix/)

## Why?

[This](https://www.washingtonpost.com/news/energy-environment/wp/2015/03/17/the-incredibly-stupid-way-that-america-wastes-1-trillion-gallons-of-water-each-year/?noredirect=on&utm_term=.6d0a8d035822) New York Times article from 2015, titled *"The incredibly stupid way that Americans waste 1 trillion gallons of water each year"* proclaims how historically Americans have been very wasteful of fresh water, a precious resource that many countries globally have extremely limited access to. I was upset by this, as access to clean water is a struggle that one in ten Indians deal with. Being an Indian, I wanted to see the distribution of water use throughout the USA to gain a better understanding of what the *Times* article was discussing. In order to do this, there were three major phases of this project to make it possible.


## Inspiration Visualization

The graph I chose to "remix" was constructed by the USGS ([United States Geological Survey](https://www.usgs.gov/)) using a data release supplied by them in 2015 for water consumption records by sector of water use per county. The original graph is shown here:

![usgs_graph](https://water.usgs.gov/watuse/images/category-pages/2015/total-withdrawals.png)

---



## How?

### Obtaining the data


### Cleaning the data

### Visualizing the data

#### About the `Log()`
I used a logarithmic scaler when calculating shades of color (in the `d3.scale`). This is because in this particular dataset, the values would often scale quite rapidly- for the `groundwater_per_day` attribute (county water use per day) the data would be distributed quite unevenly, with a large amount of small values, few values close to the average, and several extremely high values. Los Angeles County, the county drawing the most water for 2015, had close to 820 million gallons drawn a day, while the average water consumption was only 211,000 gallons. To prevent disparities in the shading of these data points, I used a `Math.log()` when calculating the domain to be passed on to the continuously mapping color scale. This ensured that **larger values would be emphasized less to allow for smaller differences between data points to become more visible through the color.**


#### About the <span style="color:steelblue">Colormaps</span>


- [*Cubehelix*](https://www.mrao.cam.ac.uk/~dag/CUBEHELIX/) - County population
  - This scheme was developed by Dave Green for implementation in the astronomy field. This scheme was developed out of a lack of color schemes that had an increase in "the perception of the brightness of the colours used". The cubehelix scheme is studied extensively in Dave Green's 2011 [paper](http://astron-soc.in/bulletin/11June/289392011.pdf) at Cambridge University. The breakthrough in color perception that Green brought on is introducing a color scale that monotonically increased in perceived brightness in response to values in the data. According to Green's research, the cubehelix scale is extremely efficient when it comes to noting the difference in items across a large set of items. I used it in this project for this very case. I knew that there are a lot of counties in the USA(~3000 are represented in my visualization) and thus understanding differences in population(an attribute that typically stays the same within given regions of land) would be made far easier. Users can examine the difference in perceived brightness and understand the meaning of the graph easier, as it has been shown that humans are able to perceive light and color very well. Translating the challenge in cognition to just mapping the differences in brightness out makes the amount of time spent understanding the relationship between county populations across America much faster.
-   [*Magma*](https://bids.github.io/colormap/) - Groundwater consumption
    - The magma color scheme was designed by Stéfan van der Walt and Nathaniel Smith for the `matplotlib` graphing library. These two scientists presented a [talk](https://www.youtube.com/watch?v=xAoljeRJ3lU) in 2015 regarding Scientific Computing with Python wherein they discussed the merits of their new color schemes. Essentially, their presentation was about designing a set of color scales that would not only be perceptually simple to measure differences in data but also comprehendable by people with color blindness. For the magma colormap specifically, they wanted to design a blue to red to yellow sequence as they found it was easy for those with colorblindness to read. Furthermore, they designed the scale such that it is 
    > analytically perfectly perceptually-uniform, both in regular form and also when converted to black-and-white.
This makes the interpretation of the scale feasible across many dimensions, which is why I chose it for this project. 

---


## Takeaways

---

## Achievements

### Technical



### Design


---

## Dataset Information & Citation

Dataset was obtained by downloading the .csv from the USGS website. A citation to the dataset used is presented as following:

Version 2.0:  Dieter, C.A., Linsey, K.S., Caldwell, R.R., Harris, M.A., Ivahnenko, T.I., Lovelace, J.K., Maupin, M.A., and Barber, N.L., 2018, Estimated use of water in the United States county-level data for 2015 (ver. 2.0, June 2018): U.S. Geological Survey data release, https://doi.org/10.5066/F7TB15V5.



