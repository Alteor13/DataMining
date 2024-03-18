from PIL import Image
import numpy
import math
import matplotlib.pyplot as plot
from sklearn.cluster import KMeans

imgfile = Image.open("images/images/pichu.png")
numarray = numpy.array(imgfile.getdata(), numpy.uint8)
if numarray.ndim == 1 :
    numarray = numarray.reshape(-1,9)
clusters = KMeans(n_clusters=8, n_init=2)
clusters.fit(numarray)

unique_colors = numpy.unique(clusters.labels_)
cluster_centers = clusters.cluster_centers_[:len(unique_colors)]

npbins = numpy.arange(0, 9)
histogram = numpy.histogram(clusters.labels_, bins=npbins)
labels = numpy.unique(clusters.labels_)
barlist = plot.bar(labels, histogram[0])
for i in range(8):
    barlist[i].set_color(
        "#%02x%02x%02x"
        % (
            math.ceil(clusters.cluster_centers_[i][0]),
            math.ceil(clusters.cluster_centers_[i][1]),
            math.ceil(clusters.cluster_centers_[i][2]),
        )
    )
plot.show()