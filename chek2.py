import collections
import requests
import re
import nltk

from collections import Counter
from nltk import pos_tag


url = "https://www.w3.org/DesignIssues/TimBook-old/History.html"

html = requests.get(url)
result = html.content.decode("utf-8")
text = re.findall(r"[\w']+|[.,!?;]", result)

tokensTag = pos_tag(text)
# print(nltk.help.upenn_tagset())

counts = Counter(y for _,y in tokensTag)
top5 = collections.Counter(counts).most_common(5)

nameTags = {
    "NN" : "Существительное, единственное число",
    "IN" : "Предлог",
    "DT" : "Определитель",
    "NNP" : "Имя собственное, единственное число",
    "JJ" : "Прилагательное"
}

for i in range(5):
    name =  nameTags[top5[i][0]]
    print(str(i+1) + ". "+ name + ": " + str(top5[i][1]))
