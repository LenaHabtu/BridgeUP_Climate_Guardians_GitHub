import setup
import xarray as xr
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
if __name__ == "__main__":
	setup.dataPath
	filename = 'HadISST_sst.nc'
	data = xr.open_dataset(filename)
	mean = data.sst.mean("time")
	print(mean)
	plt.figure()
	plt.contourf(mean["longitude"], mean["latitude"], mean)
	plt.show()