import os
import pandas as pd

result_dict = {}
for file_name in os.listdir("./result/"):
  df = pd.read_csv("./result/" + file_name, names=["file_name", "load_rate", "time_consume"])
  result_dict[file_name.replace(".txt", "")] = df
result_tabel = ""