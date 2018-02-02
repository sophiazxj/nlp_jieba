# encoding = utf-8
import jieba

#主要功能
'''
#全模式
seg_list = jieba.cut('我来到北京清华大学',cut_all = True)
print('Full mode:'+"/".join(seg_list))
#制定精准模式
seg_list = jieba.cut("我来到北京清华大学",cut_all = False)
print('Default mode:'+'/'.join(seg_list))
#默认模式:精准模式
seg_list = jieba.cut('他来到了网易杭研大厦')
print(','.join(seg_list))
#搜索引擎模式
seg_list = jieba.cut_for_search('小明硕士毕业于中国科学院计算所，后在日本京都大学深造')
print(','.join(seg_list))
'''
#调整词典
print('\n'+'/'.join(jieba.cut('如果放到post中将出错。',HMM = False))+'\n')
jieba.suggest_freq(('中','将'),True)
print('='*8+'调整词频'+'='*8)
print('\n'+'/'.join(jieba.cut('如果放到post中将出错。',HMM = False)))
print('-'*80)
print('/'.join(jieba.cut('「台中」正确应该不会被切开',HMM = False)))
print('='*8+'调整词频'+'='*8)
jieba.suggest_freq('台中',tune = True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开',HMM = False)))
print('-'*80)
jieba.suggest_freq('君意',True)
print('/'.join(jieba.cut('"大连美容美发学校中君意是你值得信赖的选择" ')))
