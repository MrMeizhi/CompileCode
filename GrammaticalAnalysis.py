#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

class Grammar:

    def __init__(self,tokenString,tokenSign,yamlLexDict,yamlGrammarDict):

        self.tokenString = tokenString
        self.tokenSign = tokenSign
        self.yamlLexDict = yamlLexDict
        self.yamlGrammarDict = yamlGrammarDict



    def dealString(self):
        '''
        首先处理字符串,将字符串得关键字后面都加一个空格
        以便匹配和识别,并且返回处理完得字符串

        '''
        tokenString = self.tokenString

        yamlDict = self.yamlLexDict

        newString = list()

        for index in range(len(tokenString)):

            if tokenString[index] in yamlDict['KeyWord']:

                newString.append(tokenString[index] + ' ')

            else:

                newString.append(tokenString[index])

        return newString




    def funcDefine(self,wholeString):
        '''
        判断该句是否有函数 'void XXX(){}'这种结构
        当然,你也可以自己定义,我这里只是做了一个简单
        的示范而已.若不能匹配到则抛出一个错误,并且打印错误且推出
        若能匹配到则返回函数{}中间的所有字符
        '''
        try:

            regex = self.yamlGrammarDict['funcDefine']

            word = re.compile(regex).findall(wholeString)

            if word == []:

                raise ValueError("Error: Invalid function define")

            return word

        except ValueError as err:

            print err

            exit(0)




    def varDefine(self,expr):
        '''
        判断是否为一般变量定义,可以匹配到
        (例如int a;或者int a=1;)
        遍历规则yamlGrammarDict若能找到相应得匹配则返回True
        否则返回False
        '''

        yamlGrammarDict = self.yamlGrammarDict

        for regex in yamlGrammarDict['varDefine']:

            word = re.compile(r'{}'.format(regex)).findall(expr)

            if word != []:

                return True

        return False




    def operatorExpr(self,expr):
        '''
        判断是否为运算符得表达式,遍历规则
        '''

        yamlGrammarDict = self.yamlGrammarDict

        for regex in yamlGrammarDict['Assignment']:

            word = re.compile(r'{}'.format(regex)).findall(expr)

            if word != []:

                return True

        return False



    def isStartWithKeyWord(self,expr):
        '''
        判断是否为关键字,如果是的话返回True,否则False
        '''

        yamlLexDict = self.yamlLexDict

        exprList = expr.split(' ')

        if exprList[0] in yamlLexDict['KeyWord']:

            return True

        else:

            return False




    def mainAnalysis(self):
        '''
        总控制器,先判断函数得框架是否正确
        接着判断第一个字符是否为关键字,决定是否进行变量
        定义的判断,如果不是关键字则进行常规表达式得运算
        '''
        string = self.dealString()

        string = ''.join(self.funcDefine(''.join(string)))

        string = string.split(';')

        for index,expr in enumerate(string):

            if expr != '':

                expr += ';'

                errorMsg = "Error: Invalid Line " + str(index+2)

                try:

                    if self.isStartWithKeyWord(expr):

                        if self.varDefine(expr) == False:

                            raise ValueError(errorMsg)

                    elif expr != '':

                        if  self.operatorExpr(expr) == False:

                            raise ValueError(errorMsg)

                    elif expr == ' ;':

                        print ''

                    else:

                        raise ValueError(errorMsg)

                except ValueError as err:

                    print err

                    exit(0)

        print "Msg:Successfully!!!"
