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


