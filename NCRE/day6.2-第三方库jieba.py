# jieba：中文分词
import jieba  # 导入 jieba 库

ls = jieba.lcut("国家计算机")  # 精确模式，返回列表
print(ls)  # 输出分词结果

ls_all = jieba.lcut("国家计算机", cut_all=True)  # 全模式
print(ls_all)  # 输出结果

ls_search = jieba.lcut_for_search("国家计算机")  # 搜索引擎模式
print(ls_search)  # 输出结果

jieba.add_word("计算机")  # 添加自定义词
ls_add = jieba.lcut("国家计算机")  # 再次分词
print(ls_add)  # 输出结果

jieba.del_word("计算机")  # 删除自定义词
ls_del = jieba.lcut("国家计算机")  # 再次分词
print(ls_del)  # 输出结果

from jieba import analyse  # 导入关键词提取模块
tags = analyse.extract_tags("国家计算机技术发展很快")  # 提取关键词
print(tags)  # 输出关键词列表

# 考点：lcut() 返回列表，cut() 返回生成器
# 考点：cut_all=True 表示全模式
# 考点：lcut_for_search() 表示搜索引擎模式
# 考点：add_word() 添加词，del_word() 删除词
