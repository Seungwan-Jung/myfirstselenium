class Webtoon:
    def __init__(self, number, name, url):
        self.number = number
        self.name = name
        self.url = url
        print(str(number) + ": " + name)


print("choose your webtoon to watch automatically")
webtoonList = []
webtoonList.append(Webtoon(1, "tutoring", "naver.com"))
webtoonList.append(Webtoon(2, "inbus", "naver.com"))
webtoonList.append(Webtoon(3, "secretlesson", "naver.com"))
webtoonList.append(Webtoon(4, "godstagram", "naver.com"))
webtoonList.append(Webtoon(5, "masterdaughter", "naver.com"))
webtoonList.append(Webtoon(6, "fitness", "naver.com"))

chooseNum = input("choose with number: ")

for n in range(0, len(webtoonList)):
    if int(chooseNum) == webtoonList[n].number:
        playUrl = webtoonList[n].url
        break
print(playUrl)
# chooseNum in webtoonList.:
#     print(str(key[0]) + ": " + key[1])
