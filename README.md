# COVID-19 TRENDS

## Data
Data ordered per country is managed by [this resource](https://github.com/pomber/covid19) <br>
Data ordered per Italian Province is managed by [this resource](https://github.com/pcm-dpc/COVID-19) 

## What
* Country: All available data is an historical of number of cases and deaths per country. <br>
* Italian Provinces: The available data is more detailed. <br>
In order to understand trends we look at the slope of the number of cases in log scale and the how the growth rate changes over time.

## How
* It works with python >= 3.5
* ```pip install -r requirements.txt ```
* By defaul the graphs will show the numbers for 
    * `Italy`, `US`, `Germany`, `Norway` and `Spain`. <br>
    * `VA`, `BG`, `MI`, `CO`, `RO` <br>

You can include other countries or provinces, if available, by just adding the name after the script's name
* ```python run_countries.py Japan```
* ```python run_italy.py VE```

## Results as of March 22nd 2020

### COUNTRIES
![Cases](https://github.com/dariocazzani/COVID-19-trends/blob/master/images/image1.png)
![Growth Rate](https://github.com/dariocazzani/COVID-19-trends/blob/master/images/image2.png)

### PROVINCES
![Cases](https://github.com/dariocazzani/COVID-19-trends/blob/master/images/image3.png)
![Growth Rate](https://github.com/dariocazzani/COVID-19-trends/blob/master/images/image4.png)
