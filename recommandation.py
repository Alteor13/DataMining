from PIL import Image
import numpy
import math
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

imgfile = Image.open("images/images/pichu.png")

numarray = numpy.array(imgfile, numpy.uint8)

numarray = numarray.reshape(-1, 9)

n_clusters = 4
clusters = KMeans(n_clusters=n_clusters, n_init=20)
clusters.fit(numarray)

couleurs = []
for i in range(len(clusters.cluster_centers_)):
    print(clusters.cluster_centers_[i])
    couleurs.append([numpy.sum(clusters.labels_==i),"#%02x%02x%02x" % (
        math.ceil(clusters.cluster_centers_[i][0]),
        math.ceil(clusters.cluster_centers_[i][1]),
        math.ceil(clusters.cluster_centers_[i][2]),
    )])
    
print (couleurs)