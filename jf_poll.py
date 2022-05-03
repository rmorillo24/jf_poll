import requests
import time
import os

from requests.structures import CaseInsensitiveDict

improvement_id = "690875a6-2ac9-46bc-99f1-de195a326eae"
improvement_slug ="improvement-improvement-test-4166174"
bearer = os.environ['JF_TOKEN']
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

        content = resp.json()
        #newprogress = content['data'][0]['data']['milestonesPercentComplete']
        newstatus = newprogress = content['data'][0]['data']['status']
        print("STATUS: %s" % newstatus)

        if status == "":
            print("Registering initial status value")
            status = newstatus
        else:
            if status != newstatus:
                print("Recording new status")
                status = newstatus
                if status == "completed":
                    print("IMPROVEMENT COMPLETE")
                    #make the call to trrrBird
        time.sleep(5)
    except Exception as e:
        print(e)
        quit()

    

'''
    {
  "id": "690875a6-2ac9-46bc-99f1-de195a326eae",
  "data": {
    "status": "proposed",
    "description": "This is an improvement test for trrrBird",
    "specification": "## Intro\n\n\n#### Problem to be solved/ User story\n\n> *Start this section with a succinct problem statement or user story that describes who this is for and what problem it helps them overcome. Some examples.*\n> \n> \n> \n> *   *The device team wants to be able to test and release the OS for every supported device whenever a new meta-balena version is released.*\n> *   *As a Fleet Owner, I would like to be able to search for a specific device across all of my applications.*\n> *   *As a new balena employee, I would like to know what I should do in my first week on the job.*\n> \n> *This user/problem statement can be as short or as long as needed, but should ultimately be a litmus test or way to check if the project is still on track and solving the problem it set out to solve. It’s important for the team working on the project to know who is ideal user and what that user is trying to accomplish. This section should also “sell” why this project is important. Listing who it impacts and by how much.*\n\n\n#### Define your User/Customer/Consumer\n\n> Be sure to figure out who you are building this for and make sure the team all has the same target user(s) in mind.\n\n\n#### How is it currently solved?\n\n> Next describe how the user “Solves this currently”, whether it is via a workaround, building it themselves or going to a competitive product.\n\n\n#### The New Solution\n\n> Here we will describe the solution. In this section try focus purely on the feature or process the user will follow and how they will interact with the new solution. This is the time to link to any rough wireframes, drawings or documentation. \n> \n> In theory this section could ultimately be turned into a blog post or press release on the new change. Is important **NOT** to go into technical implementation at this point.\n\n\n## Implementation\n\n\n#### Proposed Implementation (1 or multiple)\n\n> This is where it gets technical. This section should describe how we actually go about making the new change to the system. We should detail the required model or process changes that need to take place and describe the added or changed interfaces that will be needed.\n\n\n#### Migration Plan\n\n> It should also take into account how we handle transitioning from what we currently have “in production” to the new solution and any dependencies or processes that need to be up and running before hand.\n\n\n#### Release Plan\n\n> Here we layout how this project is released to the world. Does it need a blog post, does it need docs. Who are the people that are interested in hearing about it and how do we let them know about it.\n\n\n#### Resources Need\n\n> Estimate of engineers needed and time.\n\n\n#### Potential Issues/Risk/Blockers\n\n> Detail things that could cause delay or unpredictability in the proposed implementation plan.\n\n\n## Milestones\n\n> The milestones should layout core pieces of work that need to be achieved, this will vary from project to project, but something like “Design wireframes” for a UI related spec is an obvious milestone. Milestones should be ordered and if possible try indicate where one milestone has dependencies on others.\n> \n> Ideally it should be possible to group the milestones in to a set that achieves a Minimal Viable Product (MVP) and then additional nice to have or stretch milestones can be listed below.\n\n\n## Links & References\n\n> Add links to recorded video brainstorms or discussions in flowdock",
    "milestonesPercentComplete": 0
  },
  "loop": "loop-balena-io@1.0.0",
  "name": "Improvement Test",
  "slug": "improvement-improvement-test-4166174",
  "tags": [],
  "type": "improvement@1.0.0",
  "links": {},
  "active": true,
  "markers": [],
  "version": "1.0.0",
  "requires": [],
  "linked_at": {
    "has attached": "2022-05-03T14:11:29.515Z",
    "is implemented by": "2022-05-03T14:10:05.545Z",
    "has attached element": "2022-05-03T14:10:03.181Z"
  },
  "created_at": "2022-05-03T14:09:57.186Z",
  "updated_at": null,
  "capabilities": []
}
'''