"""import语句的执行流程"""

"""
    当使用import语句导入模块时，解释器会根据sys模块的modules属性值来查找模块是否已经被导入了。
    
"""
import pprint, sys

print(sys.modules)
pprint.pprint(sys.modules)

"""
    1. 如果模块已经被导入了，解释器什么都不做。
    2. 如果模块没有被导入，
        （1） 解释器按照某种路径搜索模块;
         (2) (可选)将搜索的模块编译为pyc字节码文件；
         (3) 执行编译生成的字节码文件从而运行模块。
         
"""
