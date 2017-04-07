# CompileCode
  本学期编译原理课程的实验:词法分析+语法分析

  分成了两个模块LexicalAnalysis和GrammarticalAnalysis
  CodeCompile.py是主控制器,装载程序的主要逻辑,并且调用前面提到的两个模块

  WordsTable.yaml是词法分析部分的保留字的表,用于匹配
  GrammarTable.yaml是语法分析部分的保留字的表(主要形式为正则表达式)
  (注意:yaml的语法请自行百度)

  InputArgparse.py是接受命令行传入值的模块

  HelloWorld.c是c语言源程序模块

  CustomError.py当初是想写个自定义错误模块,不知道后面有没有用上
