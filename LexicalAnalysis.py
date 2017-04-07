#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re
from CustomError import CustomError


class Main:

    def __init__(self,yamlDict):
        '''
        一个可能以后会用到的初始化方法
        '''
        self.yamlDict = yamlDict



    def isType(self,char,typeChar):
        '''
        判断一个字符是否是届符或者操作符,是的话返回True
        否则返回False
        '''
        if char in self.yamlDict[typeChar].iterkeys():

            return True

        else:

            return False


    def getId(self,char,typeChar):
        '''
        返回一个某个字符的种别码
        '''
        return self.yamlDict[typeChar][char]

    def checkConstant(self,judgeString):

        if judgeString.isdigit():

            return 'Constant','intConstant'

        elif judgeString.startswith('"') and judgeString.endswith('"'):

            return 'Constant','charConstant'

        elif judgeString == 'true' or judgeString == 'false':

            return 'Constant','boolConstant'

        elif judgeString[0].isdigit():

            raise CustomError('Invalid variable or Invalid constant:Near \'%s\'' % judgeString)

        else:

            return 'Identifier','id'


    def judgeChar(self,index,inputString):

        lineResultCode = []
        cacheString = ''
        inputString = inputString.rstrip('\n').lstrip(' ')
        typeId = 'Identifier'
        anId = 'id'

        '''
        inputString变量表示传入一行的字符串
        rstrip方法是为了去掉最右边的换行符
        lstrip方法是为了去掉最左边的空格符
        '''


        for char in inputString:

            try:

                if self.isType(char,'Delimiter'):
                    '''
                    判断是否界符,如果是就向lineResultCode中增加一个种别码
                    另外增加一种情况万一如果没有空格来当分解符的话,要把缓存变量
                    (cacheString)中的字符串存入列表这当中,然后清空cacheString
                    在要解析界符之前首先要先看cacheString变量当中是否有内容,有的
                    话则需要进行种别码识别,种别码识别之前也要做两步工作首先是要判断
                    是都为关键字,如果不是关键字则进入常两判断函数checkConstant()
                    '''
                    if cacheString is not '':

                        if self.isType(cacheString,'KeyWord') is not True:

                            typeId,anId = self.checkConstant(cacheString)

                        else:

                            typeId,anId = 'KeyWord',cacheString

                        lineResultCode.append([cacheString,str(self.getId(anId,typeId))])

                        cacheString = ''

                    lineResultCode.append([char,str(self.getId(char,'Delimiter'))])




                elif self.isType(char,'Operator'):
                    '''
                    判断是否操作符,如果是就向lineResultCode中增加一个种别码
                    另外增加一种情况万一如果没有空格来当分解符的话,要把缓存变量
                    (cacheString)中的字符串存入列表这当中,然后清空cacheString
                    种别码识别之前也要做两步工作首先是要判断是否都为关键字,如果不
                    是关键字则进入常两判断函数checkConstant()
                    '''
                    if cacheString is not '':

                        typeId,anId = self.checkConstant(cacheString)

                        lineResultCode.append([cacheString,str(self.getId(anId,typeId))])

                        cacheString = ''

                    lineResultCode.append([char,str(self.getId(char,'Operator'))])




                elif char == ' ':
                    '''
                    如果为空格,则可认为遇到了界符,然后判断缓存变量中的字符串是否为
                    关键字,是的话就直接写入,否则就当成普通变量来写入结果,然后清空
                    缓存字符串变量cacheString,种别码识别之前也要做两步工作首先是要判断
                    是都为关键字,如果不是关键字则进入常两判断函数checkConstant()
                    '''
                    if self.isType(cacheString,'KeyWord'):

                        lineResultCode.append([cacheString,str(self.getId(cacheString,'KeyWord'))])

                    elif cacheString != '':

                        typeId,anId = self.checkConstant(cacheString)

                        lineResultCode.append([cacheString,str(self.getId(anId,typeId))])

                    cacheString = ''



                else:
                    '''
                    如果前面几种的清空都不符合,则表明这个字符串还不是完整的,应该让它
                    继续遍历后面的字符,直到遇到上面的字符为止
                    '''
                    cacheString += char

            except CustomError,e:

                print 'Errors had been exist on line ' + index

                print ''.join(e)

                exit(0)


        if lineResultCode is not None:

            '''
            判断这一行返回的编码结果是否为空,不会空的话则返回
            '''

            return lineResultCode
