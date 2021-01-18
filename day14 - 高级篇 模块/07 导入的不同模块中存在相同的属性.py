"""导入的不同模块中存在相同的属性"""
"""
    当导入的不同模块中存在相同的属性时，比如: 当导入的两个模块moda和modb中存在同名的变量v时，

一、错误的导入方式
    from modb import v
    from moda import v
    
    后面导入的属性会把前面导入的属性覆盖掉。
二、两种正确的导入方式
    1. 给导入的属性起一个别名
        from moda import v as va
        from modb import v as vb
    2. 导入整个模块
        import moda
        import modb
"""
