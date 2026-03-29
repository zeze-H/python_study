# jieba：中文分词
import jieba

# lcut()：精确模式
ls = jieba.lcut("国家计算机考试python学科")
print(ls)

# lcut(cut_all=True)：全模式
ls = jieba.lcut("国家计算机考试python学科", cut_all=True)
print(ls)

# lcut_for_search：搜索模式（先精确模式再细分）
ls = jieba.lcut_for_search("国家计算机考试python学科")
print(ls)

# add_word：向分词词典中增加新词
jieba.add_word("python学科")
ls = jieba.lcut("国家计算机考试python学科")
print(ls)
