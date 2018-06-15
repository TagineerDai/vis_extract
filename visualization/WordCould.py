from wordcloud import WordCloud
import matplotlib.pyplot as plt
def show_img(wc):
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")

wc = WordCloud(font_path=u"./DejaVuSerif.ttf",
               max_words=2000,
               width=1920,
               height=1080,
               background_color="black",
               margin=5)

with open('2010-2018WordTrend.txt', 'r') as frequency:
    frequency = [record.split() for record in frequency.readlines()]
    for year in range(0, 8):
        key_words = {word[0] : float(word[year+1])*1000 for word in frequency }
        wc.generate_from_frequencies(key_words)
        wc.to_file('%sWordCloud.png' % str(2010+year))
        # show_img(wc)