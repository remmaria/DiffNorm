import os
import json

files = os.listdir("curves")

rois = set()

for f in files:

    if not f.endswith(".json"):
        continue

    parts = f.replace("gamlss_", "").split("_bgpdwis_PA")

    roi = parts[0]

    rois.add(roi)

json.dump(
    sorted(list(rois)),
    open("available_rois.json", "w"),
    indent=2
)