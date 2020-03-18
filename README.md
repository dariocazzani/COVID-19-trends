# COVID-19 TRENDS

## Data
Data is managed by [this resource](https://github.com/pomber/covid19)

## What
All available data is an historical of number of cases and deaths per country. <br>
In order to understand trends we look at the slope of the number of cases in log scale and the how the growth rate changes over time.

## How

* It works with python >= 3.4
* ```pip install -r requirements.txt`
* By defaul the graph will show the numbers for `Italy`, `US`, `Germany`, `Norway` and `Spain`.
You can include other countries, if available, by just adding the name after the script's name

```python
python run.py Japan
```