from .AsahiNewsArchives.api import AsahiNewsAPI
import json

def main(argv):
  api = AsahiNewsAPI('869388c0968ae503614699f99e09d960f9ad3e12')
  result = {}
  for keyword in input().strip().split(','):
    response = api.search(query='Body:{}'.format(keyword))
    if 'response' in response and 'result' in response['response']:
      result[keyword] = int(response['response']['result']['numFound'])

  sorted_result = sorted(result.items(), key=lambda x:-x[1])
  dict_result = {
    "name": sorted_result[0][0],
    "count": sorted_result[0][1]
  }
  output = json.dumps(dict_result, separators=(', ',':'), ensure_ascii=False)
  print(output)

