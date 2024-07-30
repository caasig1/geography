import io, os, geojson, json
from app import app

fp = os.path.join(app.static_folder, 'country_outlines')
fp = os.path.join(fp, 'oc')
fp = os.path.join(fp, '.geojson')
print(fp)
with open(fp, 'r') as f:
    data = geojson.load(f)

coords = data.features[0].geometry.coordinates
for t1 in coords:
    for t2 in t1:
        for t3 in t2:
            t3[0] += 180*2


with open(fp, 'w') as f:
    json.dump(data, f)
    
