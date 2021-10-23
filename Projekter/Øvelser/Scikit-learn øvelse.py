import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn import datasets, cluster

# Generate dataset
x,y = datasets.make_moons(n_samples=1000, noise=.05)

# Create and fit model
model = cluster.KMeans(n_clusters=2)
model.fit(x)

# Create 1x2 side-by-side plot
fig, axs = plt.subplots(1,2)

# Plot in the two figures
axs[0].scatter(x[:,0], x[:,1], s=5.0, c=y,   #x[:,0], x[:,1] betyder at x værdierne tages fra færste kolonne og y værdierne tages fra 2. kolonne
               cmap=cm.get_cmap('Accent'))
axs[1].scatter(x[:,0], x[:,1], c=model.labels_,
               s=5.0, cmap=cm.get_cmap('Accent'))   #s
plt.show()