import pandas as pd
import numpy as np
import random
import os
from box import Box
from solve_method import brickwork

def eval(file_path):
  # 数据输入
  data = pd.read_csv(file_path)
  
  # 箱与盒
  container = data[data["label"] == "C"].loc[0, ["length", "width", "height"]].values
  boxes_list = []
  for _, row in data[data["label"] == "B"].iterrows():
    (l, w, h) = row[["length", "width", "height"]].values
    boxes_list.extend([Box(l, w, h) for _ in range(row["count"])])
  assert(len(boxes_list) == np.sum(data["count"].values) - 1)

  # 解题方法
  random.shuffle(boxes_list)
  loaded_boxes = brickwork.solve(container, boxes_list)
  
  # 合法性检查
  # 将箱子看做一个三位数组，有盒子的地方则加1，查看是否存在大于1的地方，即发生碰撞
  container_array = np.zeros([container[0], container[1], container[2]])
  for (loaded_box, x, y, z) in loaded_boxes:
    container_array[x:loaded_box.x+x, y:loaded_box.y+y, z:loaded_box.z+z] += 1
  assert(np.sum(container_array <= 1))

  # 结果评价
  loaded_v = 0
  for (loaded_box, _, _, _) in loaded_boxes:
    loaded_v += loaded_box.l * loaded_box.w * loaded_box.h
  V = container[0] * container[1] * container[2]
  return loaded_v / V, len(loaded_boxes) / len(boxes_list)

if __name__ == "__main__":
  for file_name in os.listdir("./dataset/"):
    if "-" in file_name and "E" in file_name and ".csv" in file_name:
      load_rates = []
      for _ in range(10):
        load_rate, _ = eval("./dataset/" + file_name)
        load_rates.append(load_rate)
      print("{}:{:.4f}".format(file_name, np.mean(load_rates)))