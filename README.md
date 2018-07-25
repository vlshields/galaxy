## Galaxy: A way to Print Pretty Regression Tables

A small side project aiming to use python to print regression tables similar to the Stargazer library in R. It is not nearly finished yet, but its on its way. It currently can only take 3 regressions at the moment, but the plan for now is to scale it up to 9 regressions.

#### Installing dependencies

```
pip install -r requirements.txt
```

#### Running the program

There is some test data provided for demonstration, "test_data.csv". To see how the resulting table looks so far, just run

```
python galaxy.py
```
If you want to use your own regressions, just modify the main() funtion.