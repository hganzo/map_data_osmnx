#%%
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

place_name = 'Ogu, Tokyo, Japan'
#%%
G = ox.graph_from_bbox(north=35.7556,south=35.7495,west=139.7441,east=139.7531,network_type="drive")
G_projected = ox.project_graph(G, to_crs={'init': 'epsg:4301'})
fig, ax = ox.plot_graph(G_projected, show=False, close=False)
ax.scatter(139.749536,35.746767, c='red')
#%%
basic_stats = ox.basic_stats(G)
print(basic_stats)

#%%
edges = ox.graph_to_gdfs(G_projected, nodes=False, edges=True)
edges.head()
#%%



#%%
