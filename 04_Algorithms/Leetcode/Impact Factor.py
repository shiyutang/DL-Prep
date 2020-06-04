import json 


RecordNum = int(input().split()[0])
records = []
for i in range(RecordNum):
	record = input()
	records.append(record)

publicationIDcite = {} # {ID:[TITLE,CITATIONSUM,CITESUM]}
x = json.loads(records[0])
for publication in x["publications"]:
	publicationIDcite[publication["publicationNumber"]] = \
	                      [publication["publicationTitle"]]
	CITATIONSUM = 0
	for item in publication["articleCounts"]:
		if item['year'] == '2017' or item['year'] == '2018':
			CITATIONSUM += int(item["articleCount"])

	publicationIDcite[publication["publicationNumber"]].extend([CITATIONSUM,0,0])

# print('publicationIDcite',publicationIDcite)
	

for record in records[1:]:
	record = json.loads(record)
	for article in record["paperCitations"]["ieee"]:
		if (article['year'] == '2018' or article['year'] == '2017')\
		   and article['publicationNumber'] in publicationIDcite:
			publicationIDcite[article['publicationNumber']][-2] += 1

res = []
for key in publicationIDcite:
	restmp = publicationIDcite[key][-2]/publicationIDcite[key][-3]
	restmp = round(restmp,2)
	publicationIDcite[key][-1] = restmp
	res.append([publicationIDcite[key][-1],publicationIDcite[key][0]])

res.sort(key = lambda x: (x[0],x[1]),reverse = True)

for item in res:
	print(item[1],end = '')
	print(': ',end = '')
	print("%.2f" % item[0])




