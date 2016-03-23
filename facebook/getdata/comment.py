from facepy import GraphAPI
import json

accessToken = 'CAACEdEose0cBANE2yD02zcfYsZCVTkssucVOe8GYmcOVlppuZCAVT68RdKh92lSQVyCB0cORVCTq8CmA7ovHA8WaNaSUstiht9XKrHDmu1IlorymQo8LRg0kSdT9bfkCfRgb8pOb30h4v8v2C5ohpsC2IcX6cfeDnA2j4IYBmSWZAOJsjZBigVAPoe7lVZAFqA3DODBVLNrtrIyxzXcB0'
graph = GraphAPI(accessToken)

id = 'me/feed'
consulta = 'comments.fields(message)'
url = id+'?fields='+consulta
pages = graph.get(url, 'paginate=True')
print url
messages = []
for page in pages:
    for commDict in page['data']:
        if 'comments' in commDict:
            for messDict in commDict['comments']['data']:
                messages.append(messDict['message'].encode('utf8'))

print 'Number of messages is '+str(len(messages))
print json.dumps(messages[:20], indent=1)
