import csv
import matplotlib.pyplot as plt
import numpy as np

metrics = ["SimCnt", "CompileTime", "KeyGenerationTime", "EncryptionTime", "ExecutionTime", "DecryptionTime", "ReferenceExecutionTime"]
data = []
columns = []

with open(f"results.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    for j, row in enumerate(csv_reader):
      if j == 0: 
        columns = row
      else: 
        r = np.array(row)
        data.append(dict(zip(columns, r.T)))

for metric in metrics: 
  res = {}
  for d in data:
    if d["NodeCount"] not in res:
      res[d["NodeCount"]] = float(d[metric])/100
    else:
      res[d["NodeCount"]] = res[d["NodeCount"]] + float(d[metric])/100

  x_values = res.keys()
  y_values = list(res.values())
  plt.xlabel("Node Count for every Experiment")
  plt.ylabel(f"{metric} Miliseconds")
  plt.title(f"Average {metric}")
  plt.bar(x_values, y_values)
  plt.savefig(f"results/{metric}.png")

  fig = plt.figure()
  plt.figure().clear()
  plt.close()

