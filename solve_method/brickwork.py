from box import Box

import numpy as np

# ref: http://www.jos.org.cn/1000-9825/18/2083.pdf（论文的算法1）
def if_could_place(b_min_x, b_min_y, b_min_z, b:Box, loaded_boxes_list, container):
  if_could_place = True
  b_max_x = b.x + b_min_x
  b_max_y = b.y + b_min_y
  b_max_z = b.z + b_min_z

  # 超出容器范围
  L, W, H = container[0], container[1], container[2]
  if b_max_x > L or b_max_y > W or b_max_z > H:
    return False
  
  # 与其他已经放置的物品相碰撞
  x_intersection, y_intersection, z_intersection = -1, -1, -1
  for (loaded_box, min_x, min_y, min_z) in loaded_boxes_list:
    max_x = loaded_box.x + min_x
    max_y = loaded_box.y + min_y
    max_z = loaded_box.z + min_z
    # 计算每个维度的重合的比例，若所有维度均有重合且比例大于0，那么认为碰撞
    # x-axis
    x_intersection = -1
    if b_min_x >= min_x and b_min_x <= max_x:
      x_intersection = min(max_x, b_max_x) - b_min_x
    elif min_x >= b_min_x and min_x <= b_max_x:
      x_intersection = min(max_x, b_max_x) - min_x
    # y-axis
    y_intersection = -1
    if b_min_y >= min_y and b_min_y <= max_y:
      y_intersection = min(max_y, b_max_y) - b_min_y
    elif min_y >= b_min_y and min_y <= b_max_y:
      y_intersection = min(max_y, b_max_y) - min_y
    # z-axis
    z_intersection = -1
    if b_min_z >= min_z and b_min_z <= max_z:
      z_intersection = min(max_z, b_max_z) - b_min_z
    elif min_z >= b_min_z and min_z <= b_max_z:
      z_intersection = min(max_z, b_max_z) - min_z
    if x_intersection > 0 and y_intersection > 0 and z_intersection > 0:
      if_could_place = False
  return if_could_place

def solve(container, boxes_list):
  I = [(0, 0, 0)]
  Lz, Lx = 0, 0
  loaded_boxes_list = []

  i = 0
  L, _, H = container[0], container[1], container[2]
  while i < len(boxes_list):
    b:Box = boxes_list[i]
    flag = False
    # 寻找第一个可以放置的位置
    for (x, y, z) in I:
      if if_could_place(x, y, z, b, loaded_boxes_list, container) and (x + b.x <= Lx) and (z + b.z <= Lz):
        flag = True
        break
    # 如果没找到
    if flag == False:
      if Lx == 0 or Lx == L:
        if if_could_place(0, 0, Lz, b, loaded_boxes_list, container): 
          x, y, z = 0, 0, Lz
          flag = True
          Lz += b.z
          Lx = b.x
        elif Lz < H:  # 放宽参考线
          Lz = H
          Lx = L
          continue
      else:
        for (x, y, z) in I:
          if not (x == Lx and y == 0):
            continue
          if if_could_place(x, y, z, b, loaded_boxes_list, container) and (z + b.z <= Lz):
            flag = True
            Lx += b.x
            break
        if flag == False: # 放宽参考线
          Lx = L
          continue
    # 如果找到了
    if flag:
      I.remove((x, y, z))
      # 平移盒子，分别沿着x、y、z方向平移，使得坐标尽可能的小
      # x-axis
      prev_x = x
      x_candidates = [loaded_x + loaded_box.x for (loaded_box, loaded_x, _, _) in loaded_boxes_list]
      x_candidates = sorted(list(set(x_candidates)))
      x_candidates.insert(0, 0)
      for x_candidate in x_candidates:
        if if_could_place(x_candidate, y, z, b, loaded_boxes_list, container):
          x = x_candidate
          break
      assert(x <= prev_x)
      # y-axis
      prev_y = y
      y_candidates = [loaded_y + loaded_box.y for (loaded_box, _, loaded_y, _) in loaded_boxes_list]
      y_candidates = sorted(list(set(y_candidates)))
      y_candidates.insert(0, 0)
      for y_candidate in y_candidates:
        if if_could_place(x, y_candidate, z, b, loaded_boxes_list, container):
          y = y_candidate
          break
      assert(y <= prev_y)
      # z-axis
      prev_z = z
      z_candidates = [loaded_z + loaded_box.z for (loaded_box, _, _, loaded_z) in loaded_boxes_list]
      z_candidates = sorted(list(set(z_candidates)))
      z_candidates.insert(0, 0)
      for z_candidate in z_candidates:
        if if_could_place(x, y, z_candidate, b, loaded_boxes_list, container):
          z = z_candidate
          break
      assert(z <= prev_z)
      # 添加到对应位置
      loaded_boxes_list.append((b, x, y, z))
      # 维护列表的有序性
      for (append_x, append_y, append_z) in [(x + b.x, y, z), (x, y + b.y, z), (x, y, z + b.z)]:
        append_index = len(I)
        for index, (exist_x, exist_y, exist_z) in enumerate(I):
          if append_y < exist_y:
            append_index = index
            break
          elif append_y == exist_y and append_x < exist_x:
            append_index = index
            break
          elif append_y == exist_y and append_x == exist_x and append_z < exist_z:
            append_index = index
            break
        I.insert(append_index, (append_x, append_y, append_z))
    i += 1
  return loaded_boxes_list

# TODO 这个地方是可以通过一个参数控制和上面的算法合二为一的，其实我是有点想写一个基类
# 然后这个基类是包含多种方法的，外面通过参数控制调用就行
def solve_with_revolve(container, boxes_list):
  I = [(0, 0, 0)]
  Lz, Lx = 0, 0
  loaded_boxes_list = []

  i = 0
  L, _, H = container[0], container[1], container[2]
  while i < len(boxes_list):
    b:Box = boxes_list[i]
    flag = False
    # 寻找第一个可以放置的位置
    for (x, y, z) in I:
      if if_could_place(x, y, z, b, loaded_boxes_list, container) and (x + b.x <= Lx) and (z + b.z <= Lz):
        flag = True
        break
    # 如果没找到
    if flag == False:
      if Lx == 0 or Lx == L:
        if if_could_place(0, 0, Lz, b, loaded_boxes_list, container): 
          x, y, z = 0, 0, Lz
          flag = True
          Lz += b.z
          Lx = b.x
        elif Lz < H:  # 放宽参考线
          Lz = H
          Lx = L
          continue
      else:
        for (x, y, z) in I:
          if not (x == Lx and y == 0):
            continue
          if if_could_place(x, y, z, b, loaded_boxes_list, container) and (z + b.z <= Lz):
            flag = True
            Lx += b.x
            break
        if flag == False: # 放宽参考线
          Lx = L
          continue
    # 如果找到了
    if flag:
      I.remove((x, y, z))
      # 平移盒子，分别沿着x、y、z方向平移，使得坐标尽可能的小
      # x-axis
      prev_x = x
      x_candidates = [loaded_x + loaded_box.x for (loaded_box, loaded_x, _, _) in loaded_boxes_list]
      x_candidates = sorted(list(set(x_candidates)))
      x_candidates.insert(0, 0)
      for x_candidate in x_candidates:
        if if_could_place(x_candidate, y, z, b, loaded_boxes_list, container):
          x = x_candidate
          break
      assert(x <= prev_x)
      # y-axis
      prev_y = y
      y_candidates = [loaded_y + loaded_box.y for (loaded_box, _, loaded_y, _) in loaded_boxes_list]
      y_candidates = sorted(list(set(y_candidates)))
      y_candidates.insert(0, 0)
      for y_candidate in y_candidates:
        if if_could_place(x, y_candidate, z, b, loaded_boxes_list, container):
          y = y_candidate
          break
      assert(y <= prev_y)
      # z-axis
      prev_z = z
      z_candidates = [loaded_z + loaded_box.z for (loaded_box, _, _, loaded_z) in loaded_boxes_list]
      z_candidates = sorted(list(set(z_candidates)))
      z_candidates.insert(0, 0)
      for z_candidate in z_candidates:
        if if_could_place(x, y, z_candidate, b, loaded_boxes_list, container):
          z = z_candidate
          break
      assert(z <= prev_z)
      # 添加到对应位置
      loaded_boxes_list.append((b, x, y, z))
      # 维护列表的有序性
      for (append_x, append_y, append_z) in [(x + b.x, y, z), (x, y + b.y, z), (x, y, z + b.z)]:
        append_index = len(I)
        for index, (exist_x, exist_y, exist_z) in enumerate(I):
          if append_y < exist_y:
            append_index = index
            break
          elif append_y == exist_y and append_x < exist_x:
            append_index = index
            break
          elif append_y == exist_y and append_x == exist_x and append_z < exist_z:
            append_index = index
            break
        I.insert(append_index, (append_x, append_y, append_z))
    else:
      state = b.revolve()
      if state != 0:
        continue
    i += 1
  return loaded_boxes_list

# TODO 这个算法有一个可见的改进，就是旋转的问题，可以考虑以遗传算法的模式，选择旋转的策略