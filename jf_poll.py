import requests
import time
import os

from requests.structures import CaseInsensitiveDict


def notification(content, date="20220505", check_grammar=False):
  #replace print with, or add the call to the trrrBird block
  print(content)


try:
  # improvement_id = "690875a6-2ac9-46bc-99f1-de195a326eae"
  # improvement_slug ="improvement-improvement-test-4166174"
  improvement_id = os.environ['IMPROVEMENT_ID']
  improvement_slug = os.environ['IMPROVEMENT_SLUG']
  bearer = os.environ['JF_TOKEN']
except:
  print("ENVIRONMENT VARIABLES NOT AVAILABLE")
  quit()

progress = -1
status = ""

# Configuring JF call
url = "https://api.ly.fish/api/v2/query"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = "Bearer " + bearer
headers["Content-Type"] = "application/json"

data = """
{
        "query":{"description":"Fetch all contracts linked to """ + improvement_slug + """","type":"object","required":["id","type"],"properties":{"id":{"const":\"""" + improvement_id + """"}},"$$links":{"is implemented by":{"type":"object","required":["type"],"additionalProperties":false,"properties":{"type":{"const":"project@1.0.0"}}}}},"options":{"limit":1,"mask":{"type":"object","required":["loop"],"properties":{"loop":{"enum":["loop-balena-io@1.0.0",null],"type":"string"}}}}
}
"""



#looping queries to JF to detect progress changes
while(1):
    try:
        resp = requests.post(url, headers=headers, data=data)
    except Exception as e:
        print("EXCEPTION accesing JF.")
        print(e)
        quit()

    try:
        content = resp.json()
        #newprogress = content['data'][0]['data']['milestonesPercentComplete']
        newstatus = content['data'][0]['data']['status']
        name = content['data'][0]['name']
        description = content['data'][0]['data']['description']
        print("Read status: %s" % newstatus)

        if status == "":
            print("Registering initial status value: %s" %newstatus)
            status = newstatus
        else:
            if status != newstatus:
                print("Recording new status: %s" %newstatus)
                status = newstatus
                if status == "completed":
                    print("IMPROVEMENT COMPLETE")
                    notification("We have completed the %s improvement!! %s" %(name, description)  )
        time.sleep(5)
    except Exception as e:
        print("EXCEPTION accesing data. ")
        print(e)
        quit()

    