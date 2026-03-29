'''
pip 工具安装：

win + r -> cmd

pip install jieba      # 安装
pip uninstall jieba    # 卸载
pip download jieba     # 下载但不安装
pip show jieba         # 查看第三方库信息
pip list               # 查看当前第三方库列表

自定义安装：
文件安装（扩展名 .whl）
'''

import jieba

print(jieba.lcut("国家计算机二级python"))
