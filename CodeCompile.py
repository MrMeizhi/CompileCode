#!/usr/bin/env python
#-*- coding:utf-8 -*-

import yaml
import inspect
import InputArgparse
import CustomError
from  LexicalAnalysis import Main
from GrammaticalAnalysis import Grammar


def main():

    currentFilename =  inspect.getfile(inspect.currentframe())

    sourceCode,lexRuleFile,grammarRuleFile = InputArgparse.inputArgparse(currentFilename)

    '''
    加载yaml模块并且解析yaml成字典类型的数据
    '''

    yamlLexFile = open(lexRuleFile)

    yamlGrammarFile = open(grammarRuleFile)

    yamlLexDict = yaml.load(yamlLexFile)

    yamlGrammarDict = yaml.load(yamlGrammarFile)

    '''
    初始化LexicalAnalysis模块的Main类,
    传入一个存有规则的变量
    '''
    LexAnalysis = Main(yamlLexDict)


    '''
    逐行读取c语言源码程序
    调用Main的judgeChar方法
    '''
    f = open(sourceCode)



    '''
    使用一个变量来保存token串 -> token
    得到一个结果的token以及编号串->tokenSequence
    不要问我tokenSign有什么用,我也不知道,其实没用过
    '''
    tokenSequence = []
    tokenString = []
    tokenSign = []



    for index,line in enumerate(f.readlines()):
        '''
        逐行读取源码并且丢给mainController.judgeChar方法来处理
        '''
        sequence = LexAnalysis.judgeChar(str(index+1),line)

        tokenSequence += sequence



    for oneList in tokenSequence:
        '''
        便利列表中的元素
        不断往两个变量中分别存储种别码和token字符
        '''

        #print oneList
        tokenString.append(oneList[0])
        tokenSign.append(oneList[1])

    '''
    初始化GrammaticalAnalysis模块中得Grammar
    并且调用maimAnalysis方法
    '''
    grammarAnalysis = Grammar(tokenString,tokenSign,yamlLexDict,yamlGrammarDict)

    grammarAnalysis.mainAnalysis()









if __name__ == '__main__':

    main()
