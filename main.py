import uuid
import json
import os
import shutil
import jsonF
print(jsonF.jsonCode)

path_builds = '/home/runner/MCBEAddonCreatorPY/builds'
path_rp = '/home/runner/MCBEAddonCreatorPY/builds/rp'
path_bp = '/home/runner/MCBEAddonCreatorPY/builds/bp'
if not os.path.isdir(path_builds):
  os.mkdir(path_builds)
else:
  shutil.rmtree(path_builds)
  os.mkdir(path_builds)

if not os.path.isdir(path_bp):
  os.mkdir(path_bp)
else:
  shutil.rmtree(path_bp)
  os.mkdir(path_bp)

if not os.path.isdir(path_rp):
  os.mkdir(path_rp)
else:
  shutil.rmtree(path_rp)
  os.mkdir(path_rp)
  
with open('/home/runner/MCBEAddonCreatorPY/builds/rp/manifest.json', 'w') as f:
  json.dump(jsonF.jsonCode, f)