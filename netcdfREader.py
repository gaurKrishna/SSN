import netCDF4 as nc

file_path = 'E:/IIITV/Isro Safe Ship Nav/data_iiit-varoda/uv.nc'
data = nc.Dataset(file_path)

print(data)