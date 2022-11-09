import googletrans

text3 = "神在軸遠的天上守望莉人間, 時不時派出天使, 幫助人位更好地生活。"

print(googletrans.LANGUAGES)
translator = googletrans.Translator()
result = translator.translate(text3, src='zh-tw', dest='pt')
print(result.text)


