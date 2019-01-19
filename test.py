#%%
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import Point,LineString

#%%
G = ox.graph_from_bbox(north=35.7556,south=35.7495,west=139.7441,east=139.7531,network_type="drive")
G_projected = ox.project_graph(G, to_crs={'init': 'epsg:4301'})
edges = ox.graph_to_gdfs(G_projected, nodes=False, edges=True)
distance=edges["geometry"][0].project(point)
point_onRoad=edges["geometry"][0].interpolate(distance).coords[0]

fig, ax = ox.plot_graph(G_projected, show=False, close=False)
point_x=139.749536
point_y=35.746767
ax.scatter(point_x, point_y, c='red')
point=Point(point_x,point_y)
i=1
distance=edges["geometry"][i].project(point)
point_onRoad=edges["geometry"][i].interpolate(distance).coords[0]
ax.scatter(edges["geometry"][i].coords[:][0][0],edges["geometry"][i].coords[:][0][1],c='pink')
ax.scatter(edges["geometry"][i].coords[:][-1][0],edges["geometry"][i].coords[:][-1][1],c='green')
ax.scatter(point_onRoad[0],point_onRoad[1],c='blue')


