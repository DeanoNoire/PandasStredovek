import pandas as pd

epizody = pd.read_json('epizody.json')

epizodyDS = pd.DataFrame.from_dict(epizody)
epizodyDS["dat"] = pd.to_datetime(epizodyDS["datum"],format="%Y%m%d")
epizodyDS["datPrev"] = epizodyDS["dat"].shift(1)
epizodyDS["datDiff"] = epizodyDS["dat"].diff()
epizodyDS["datediffDny"] = pd.to_numeric(epizodyDS["datDiff"].dt.days, downcast='integer')

prumerDS = epizodyDS["datediffDny"].mean()

print(epizodyDS)
print(prumerDS)


