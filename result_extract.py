import os
import pandas as pd
import numpy as np

result_dict = {}
for file_name in os.listdir("./result/"):
  df = pd.read_csv("./result/" + file_name, names=["file_name", "load_rate", "time_consume"])
  result_dict[file_name.replace(".txt", "")] = df
print(np.mean(result_dict["brickwork_10000000"]["load_rate"].values))
print(np.mean(result_dict["ourmethod_10000000"]["load_rate"].values))
print(np.mean(result_dict["brickwork_annealing_10000000"]["load_rate"].values))
print(np.mean(result_dict["ourmethod_annealing_10000000"]["load_rate"].values))
print(np.mean(result_dict["brickwork_10000000"]["time_consume"].values))
print(np.mean(result_dict["ourmethod_10000000"]["time_consume"].values))
print(np.mean(result_dict["brickwork_annealing_10000000"]["time_consume"].values))
print(np.mean(result_dict["ourmethod_annealing_10000000"]["time_consume"].values))
result_tabel = ""