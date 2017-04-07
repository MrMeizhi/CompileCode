#!/usr/bin/env python
#-*- coding:utf-8 -*-

import optparse
import os

def inputArgparse(filename):

    inputArg = optparse.OptionParser()

    inputArg.add_option('-s',dest = "sourceCode",help = "Your source code")
    inputArg.add_option('-l',dest = "lexRuleFile",help = "Your lex words rule file")
    inputArg.add_option('-g',dest = "grammarRuleFile",help = "Your grammar rule file")
    options,args = inputArg.parse_args()

    if options.sourceCode is None or options.lexRuleFile is None or options.grammarRuleFile is None:

        command = 'python %s -h' % filename
        os.system(command)

        exit(0)

    else:

        return options.sourceCode,options.lexRuleFile,options.grammarRuleFile
