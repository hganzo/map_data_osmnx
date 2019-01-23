#%%
import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from shapely.geometry import Point,LineString


#%%
def get_nearest_point(G_projected, point):
    edges = ox.graph_to_gdfs(G_projected, nodes=False, edges=True)
    min_distance=9999999.999999
    min_point_onRoad=[0,0]
    min_index=999
    for i in range(len(edges["geometry"])):
        distance=edges["geometry"][i].project(point)
        point_onRoad=edges["geometry"][i].interpolate(distance).coords[0]
        point.distance(Point(point_onRoad[0],point_onRoad[1]))
        if point.distance(Point(point_onRoad[0],point_onRoad[1])) < min_distance:
            min_point_onRoad=point_onRoad
            min_distance=point.distance(Point(point_onRoad[0],point_onRoad[1]))
            min_index=i
    return min_distance \
          ,min_point_onRoad \
          ,(edges["geometry"][min_index].coords[:][0][0], edges["geometry"][min_index].coords[:][0][1]) \
          ,(edges["geometry"][min_index].coords[:][-1][0], edges["geometry"][min_index].coords[:][-1][1])


#%%
point_x=139.749946; point_y=35.749867
point=Point(point_x,point_y)

G = ox.graph_from_bbox(north=35.7556,south=35.7495,west=139.7441,east=139.7531,network_type="drive")
G_projected = ox.project_graph(G, to_crs={'init': 'epsg:4301'})

distance, point_onRoad, node1, node2 = get_nearest_point(G_projected, point) 

fig, ax = ox.plot_graph(G_projected, show=False, close=False)
ax.scatter(point_x, point_y, c='red')
ax.scatter(node1[0], node1[1], c='pink')
ax.scatter(node2[0], node2[1], c='green')
ax.scatter(point_onRoad[0], point_onRoad[1], c='blue')



