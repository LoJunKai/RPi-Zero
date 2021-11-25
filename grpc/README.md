
## Graph Plotting

for python script found at:
`./grpc/plot_metrics.py`

### Setup

need these packages
```
pip install pandas
pip install matplotlib
```

edit filename (.csv) 
```
log_filename = "mqtt_1000.csv"`
```
### Running

```
python plot_metrics.py
```

#### Note

functions:

`reformat_log_csv(log_fp) `
>-creates a temporary file:  `./grpc/temp.csv`
>-only need to run 1x 
>(once reformat function called > overwrites csv previous content)
<img width="657" alt="reformatted_log_csv" src="https://user-images.githubusercontent.com/49429691/142929066-0885b77b-0dd4-41ae-beb4-a545d06c32e3.png">

`plotAllMetricsGraph(log_fp)`
`plotCpuGraph(log_fp)`
`plotMemGraph(log_fp)`
`plotNetworkIn(log_fp)` (can remove outliers to visualise plots better)
`plotNetworkOut(log_fp)`
