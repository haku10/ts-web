import logging
import json
import csv

logger = logging.getLogger('development')

class parse_csv:
  @staticmethod
  def csv_parse_speechtext(file):
    csvdata = csv.reader(file)
    number = 0
    mylist = {}
    mylinest = []
    for row in csvdata:
      mynest = {}
      mynest['id'] = number
      mynest['text'] = row[0]
      mylinest.append(mynest)
      number += 1
    mylist["data"] = mylinest
    json_data = json.dumps(mylist)
    logger.info(file)
    return json_data
