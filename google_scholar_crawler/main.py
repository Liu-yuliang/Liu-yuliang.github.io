print(1)
from scholarly import scholarly
import jsonpickle
import json
from datetime import datetime
import os
print(1)
author: dict = scholarly.search_author_id(os.environ['GOOGLE_SCHOLAR_ID'])
print(2)
scholarly.fill(author, sections=['basics', 'indices', 'counts', 'publications'])
print(3)
name = author['name']
print(4)
author['updated'] = str(datetime.now())
print(5)
author['publications'] = {v['author_pub_id']:v for v in author['publications']}
print(6)
print(json.dumps(author, indent=2))
os.makedirs('results', exist_ok=True)
with open(f'results/gs_data.json', 'w') as outfile:
    json.dump(author, outfile, ensure_ascii=False)

shieldio_data = {
  "schemaVersion": 1,
  "label": "citations",
  "message": f"{author['citedby']}",
}
with open(f'results/gs_data_shieldsio.json', 'w') as outfile:
    json.dump(shieldio_data, outfile, ensure_ascii=False)
