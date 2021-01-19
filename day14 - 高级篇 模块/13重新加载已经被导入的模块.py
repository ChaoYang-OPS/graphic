"""重新加载已经被导入的模块"""

"""
    使用import语句导入某个模块后，如果对该模块做了修改，然后再次使用import语句导入该模块，
那么对模块的修改不会起任何作用。
    在交互式命令行中
    import mod
    mod.v
    修改mod.py，在交互式命令行中:
    import mod
    mod.v

"""

"""
    使用import语句导入某个模块后，如果对该模块做了修改，可以调用标准库函数reload重新加载
已经被导入的模块。

    在交互式命令行中:
    >>> import importlib
    >>> importlib.reload(mod)
    >>> mod.v
"""















