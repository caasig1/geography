import io, os, geojson, json
from app import app

# ADJUSTING COORDINATES
# fp = os.path.join(app.static_folder, 'country_outlines')
# fp = os.path.join(fp, 'oc')
# fp = os.path.join(fp, '.geojson')
# print(fp)
# with open(fp, 'r') as f:
#     data = geojson.load(f)

# coords = data.features[0].geometry.coordinates
# for t1 in coords:
#     for t2 in t1:
#         for t3 in t2:
#             t3[0] += 180*2



# CREATING A WORLD FILE FROM COUNTRY OUTLINES
# with open(fp, 'w') as f:
#     json.dump(data, f)
    
def helper(continent):
    folder = os.path.join(app.static_folder, 'country_outlines')
    folder = os.path.join(folder, continent)
    geodata = []

    for filename in os.listdir(folder):
        fp = os.path.join(folder, filename)
        if os.path.isfile(fp):
            with open(fp, 'r') as f:
                data = geojson.load(f)
            
            if data['type'] == 'FeatureCollection':
                geodata.extend(data['features'])
            elif data['type'] == 'Feature':
                geodata.append(data)

    geodata = geojson.FeatureCollection(geodata)
    return geodata

geodata = []

temp = helper('na')
geodata.extend(temp['features'])

temp = helper('sa')
geodata.extend(temp['features'])

temp = helper('europe') # remove turkey cyprus and russia dupes
temp['features'].pop(86)
temp['features'].pop(70)
temp['features'].pop(16)
geodata.extend(temp['features'])

temp = helper('africa')
geodata.extend(temp['features'])

temp = helper('asia')
geodata.extend(temp['features'])

temp = helper('oc')
geodata.extend(temp['features'])

geodata = geojson.FeatureCollection(geodata)

fp = os.path.join(app.static_folder, 'world.geojson')
with open(fp, 'w') as f:
    json.dump(geodata, f)


##################


# import geopandas as gpd
# from shapely.geometry import Polygon, MultiPolygon
# from shapely.validation import make_valid

# # Load the GeoJSON file
# fp = os.path.join(app.static_folder, 'world.geojson')
# input_geojson = fp
# output_geojson = fp

# # Load the data into a GeoDataFrame
# gdf = gpd.read_file(input_geojson)

# # Ensure the GeoDataFrame is using a projected coordinate system
# gdf = gdf.to_crs(epsg=3395)  # Mercator projection (meters)

# # Function to make geometries valid
# def fix_geometry(geom):
#     try:
#         # Ensure the geometry is valid
#         return make_valid(geom)
#     except Exception as e:
#         print(f"Error fixing geometry: {e}")
#         return geom

# # Apply the fix_geometry function to each geometry
# gdf['geometry'] = gdf['geometry'].apply(fix_geometry)

# gdf = gdf[gdf.geometry.apply(lambda x: isinstance(x, (Polygon, MultiPolygon)))]

# # Add a new column for neighbors
# gdf['neighbors'] = ''

# # Create a spatial index for the GeoDataFrame
# sindex = gdf.sindex

# def find_neighbors(geometry, index):
#     """Find neighboring geometries for a given geometry."""
#     possible_matches_index = list(index.intersection(geometry.bounds))
#     possible_matches = gdf.iloc[possible_matches_index]
#     precise_matches = possible_matches[possible_matches.intersects(geometry)]
#     return precise_matches

# # Iterate through each feature and find neighbors
# for idx, row in gdf.iterrows():
#     geom = row['geometry']
#     neighbors = find_neighbors(geom, sindex)
#     # Exclude the feature itself from the neighbors list
#     neighbors = neighbors[neighbors.index != idx]
#     # Get neighbor names or IDs
#     neighbor_names = neighbors['name'].tolist()  # Adjust 'name' to your field
#     # Update the neighbors field
#     gdf.at[idx, 'neighbors'] = ', '.join(neighbor_names)

# # Save the updated GeoDataFrame to a new GeoJSON file
# gdf.to_file(output_geojson, driver='GeoJSON')

# # with open(fp, 'w') as f:
# #     json.dump(data, f)