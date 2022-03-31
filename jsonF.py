import uuid

uuid1 = uuid.uuid4()
uuid2 = uuid.uuid4()

jsonCode = {
  "format_version": 2,
  "header": {
    "name": "MCBE Addon Creator PY Addon RP",
    "description": "This addon was made using MCBE Addon Creator PY",
    "uuid": "{0}".format(uuid1),
    "version": [
      1,
      0,
      0
    ],
    "min_engine_version": [
      1,
      17,
      0
    ]
  },
  "modules": [
    {
      "type": "resources",
      "uuid": "{0}".format(uuid2),
      "version": [
        1,
        0,
        0
      ]
    }
  ],
  "metadata": {
    "authors": [
      "Noinkin#5026, ElectronicPlayz#3809"
    ],
    "url": "MCBEAddons.tk"
  }
}
  