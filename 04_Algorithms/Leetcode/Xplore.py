import json

def hIndex(citations):
    if citations != []:  # think about empty
        citations.sort(reverse=True)
        idx = 0
        while (idx < len(citations)):
            if citations[idx] < idx + 1:
                break
            else:
                idx += 1
    else:
        return 0
    # print(idx)
    return idx

def main():
    items = int(input())
    authorCitation = {}
    for i in range(items):
        item = json.loads(input())
        citation = item['citing_paper_count']
        for i in range(len(item['authors']['authors'])):
            if authorCitation.__contains__(item['authors']['authors'][i]["full_name"]):
                authorCitation[item['authors']['authors'][i]["full_name"]].append(citation)
            else:
                authorCitation[item['authors']['authors'][i]["full_name"]] = [citation]
    # print(authorCitation)
    authorHindex = []
    for key in authorCitation:
        ahindex = hIndex(authorCitation[key])
        authorHindex.append([key,ahindex])
    authorHindex.sort(reverse= False,key = lambda node: node[0])
    # print(authorHindex)
    authorHindex.sort(reverse=True,key = lambda node: node[1])
    # print(authorHindex)
    for item in authorHindex:
        print(item[0],end='')
        print(' ',end='')
        print(item[1])
    return 0

main()




