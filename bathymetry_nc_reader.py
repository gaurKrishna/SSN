from pprint import pprint
from tracemalloc import start
import netCDF4 as nc
import time

file_path = "E:/IIITV/Isro Safe Ship Nav/Bathymetry Nc/GEBCO_25_May_2022_f0a20f3b5391/gebco_2021_n26.26171714067459_s-8.191405177116394_w49.78125_e101.95313358306885.nc"
data = nc.Dataset(file_path)

nodes = {}
adjacency_list = {}

latitudes_len = data["lat"].size
longitude_len = data["lon"].size

latitudes_len = 4
longitude_len = 2

start_time = time.time()
for i in range(latitudes_len):
    for j in range(longitude_len):
        key = str(data["lat"][i]) + "-" + str(data["lon"][j])
        nodes[key] = data["elevation"][i, j].data.item()
        adjacency_list[key] = []
        if i - 1 >= 0 :
            adjacency_list[key].append(str(data["lat"][i - 1]) + "-" + str(data["lon"][j]))
            if j - 1 >= 0 :
                adjacency_list[key].append(str(data["lat"][i - 1]) + "-" + str(data["lon"][j - 1]))
            if j + 1 < longitude_len:
                adjacency_list[key].append(str(data["lat"][i - 1]) + "-" + str(data["lon"][j + 1]))
        if i + 1 < latitudes_len:
            adjacency_list[key].append(str(data["lat"][i + 1]) + "-" + str(data["lon"][j]))
            if j - 1 >= 0 :
                adjacency_list[key].append(str(data["lat"][i + 1]) + "-" + str(data["lon"][j - 1]))
            if j + 1 < longitude_len:
                adjacency_list[key].append(str(data["lat"][i + 1]) + "-" + str(data["lon"][j + 1]))
        if j - 1 >= 0:
            adjacency_list[key].append(str(data["lat"][i]) + "-" + str(data["lon"][j - 1]))
        if j + 1 < longitude_len:
            adjacency_list[key].append(str(data["lat"][i]) + "-" + str(data["lon"][j + 1]))
end_time = time.time()
pprint(nodes)
pprint(adjacency_list)
print("Total Time Taken", (end_time - start_time) / 60)