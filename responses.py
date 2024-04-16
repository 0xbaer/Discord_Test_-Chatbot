from random import choice, randint
import requests
import json


SNAPSHOT_API_URL = "https://api.snapshot.org/graphql"

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'bad, thanks!'
    elif 'bye' in lowered:
        return 'See you!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'

    elif 'p' in lowered:
        # we have imported the requests module
        #import requests
        # defined a URL variable that we will be
        # using to send GET or POST requests to the API
        url = "https://hub.snapshot.org/graphql"

        body = """
        query Proposals {
          proposals(
            first: 2,
            skip: 0,
            where: {
              space_in: ["balancer.eth", "yam.eth"],
              state: "closed"
            },
            orderBy: "created",
            orderDirection: desc
          ) {
            id
            title
            body
            choices
            start
            end
            snapshot
            state
            author
            space {
              id
              name
            }
          }
        }
        """


        response = requests.post(url=url, json={"query": body})
        my_json = response.content.decode('utf8')#.replace("'", '"')
        my_json = json.loads(my_json)
        #print(my_json.content.data.proposals[0].title)
        print("response status code: ", response.status_code)
        if response.status_code == 200:
            print("response : ", response.content)
            #return my_json.content.data.proposals[0].title
            print(my_json)
            return my_json['data']["proposals"][0]['title']
        else:
            return "bad request"



    else:
        return choice(['I dont understand...',
                       'What are u talking about',
                       'Do you mind rephracing that?'])


    def get_snapshot_proposals() -> str:
        query = """
        {
          proposals {
            id
            title
            body
            choices
          }
        }
        """
        try:
            response = requests.post(SNAPSHOT_API_URL, json={"query": query})
            data = response.json()
            proposals = data.get("data", {}).get("proposals", [])
            if proposals:
                proposal_info = "\n".join([f"{proposal['id']}: {proposal['title']}" for proposal in proposals])
                return f"Latest proposals on Snapshot:\n{proposal_info}"
            else:
                return "No proposals found on Snapshot."
        except Exception as e:
            return f"Error fetching proposals: {str(e)}"


