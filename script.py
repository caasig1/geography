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
    
# def helper(continent):
#     folder = os.path.join(app.static_folder, 'country_outlines')
#     folder = os.path.join(folder, continent)
#     geodata = []

#     for filename in os.listdir(folder):
#         fp = os.path.join(folder, filename)
#         if os.path.isfile(fp):
#             with open(fp, 'r') as f:
#                 data = geojson.load(f)
            
#             if data['type'] == 'FeatureCollection':
#                 geodata.extend(data['features'])
#             elif data['type'] == 'Feature':
#                 geodata.append(data)

#     geodata = geojson.FeatureCollection(geodata)
#     return geodata

# geodata = []

# temp = helper('na')
# geodata.extend(temp['features'])

# temp = helper('sa')
# geodata.extend(temp['features'])

# temp = helper('europe') # remove turkey cyprus and russia dupes
# temp['features'].pop(43)
# temp['features'].pop(35)
# temp['features'].pop(8)
# geodata.extend(temp['features'])

# temp = helper('africa')
# geodata.extend(temp['features'])

# temp = helper('asia')
# geodata.extend(temp['features'])

# temp = helper('oc')
# geodata.extend(temp['features'])

# geodata = geojson.FeatureCollection(geodata)

# fp = os.path.join(app.static_folder, 'trial.geojson')
# with open(fp, 'w') as f:
#     json.dump(geodata, f)