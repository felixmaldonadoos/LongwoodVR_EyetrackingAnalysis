### analysis 

very basic so far, building on lit papers. 

### setup 

1. download extract data file to main project directory and rename folder to ```data/``` 

2. install venv dependencies inside ```python/``` 

```
cd python
source venvLW/bin/activate
pip install -r requirements.txt
```

# to do: 

1. correlation between head acceleration and gaze direction variance 
2. correlation between eye-openness and gaze variability? 
3. more metrics.. 

# issues

1. gaze depth in unreal units does not have a standar way of being found
2. filtering can be made more advanced (currently ussing gaussian filter with sigma=0.1)

