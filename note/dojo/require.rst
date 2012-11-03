====================
dojo.require流程解析
====================

.. contents::
   :depth: 3

函数原型解释
============

require函数可以接受多种参数变体
    * require(moduleId), 加载moduleId指定的模块, 并返回module的返回值。
    * require(dependencies, callback), 加载dependencies代表的模块, 加载完成后调用callback。
    * require(config, dependencies, callback), 先整合config到系统，然后完成上面所述的那一步

函数流程跟踪
============

由于 require(config, dependencies, callback)这个原型包含的过程比较完整，我们就
以此为依据来跟踪其运行情况。

    * require
      * contextRequire(config/* a1 */ , dependencies, callback, 0, req)

