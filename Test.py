import grequests

urls = ['https://www.menti.com/core/objects/vote_keys/']
rs = (grequests.get(u) for u in urls)
requests = grequests.map(rs)
for response in requests:
    print(response.content)
