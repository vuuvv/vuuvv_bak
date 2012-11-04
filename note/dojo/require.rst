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

dojo的默认值:
    has:
        * host-browser
        * dom
        * dojo-amd-factory-scan
        * dojo-loader
        * dojo-has-api
        * dojo-inject-api
        * dojo-timeout-api
        * dojo-trace-api
        * dojo-log-api
        * dojo-dom-ready-api
        * dojo-publish-privates
        * dojo-config-api
        * dojo-sniff
        * dojo-sync-loader
        * dojo-test-sniff
        * config-deferredInstrumentation
        * config-useDeferredInstrumentation
        * config-tlmSiblingOfDojo

    packages:
        * dojo, "."
        * tests, "./tests"
        * dijit, "../dijit"
        * build, "../util/build"
        * doh, "../util/doh"
        * dojox, "../dojox"
        * demos, "../demos"

    async: 0

    waitSeconds: 15

require的全局变量
    * aliases
    * paths
    * pathsMapProg
    * packs
    * map
    * mapProgs, 一个按map中的key排序的数组
    * modules
    * cacheBust
    * cache
    * urlKeyPrefix
    * pendingCacheInsert
    * dojoSniffConfig

require的流程
    * require
      * contextRequire(config, dependencies, callback, 0, req)***contextRequire(a1, a2, a3, referenceModule, contextRequire)
        * 首先分析传入的参数，根据传入的参数确定执行的路线，我们按照前面说的参数走。
        * config(a1, 0, referenceModule) *** config(config, booting, referenceModule)
          * 将waitSeconds转换成毫秒保存在req.waitms中
          * 处理cacheBust参数
          * 保存baseUrl和combo到req的属性中
          * 处理async
          * 所有的参数都会保存在req.rawConfig中，并在has中设置"config-xxx"。
          * 如果baseUrl不存在，设定默认值"./", 并确保baseUrl是以"/"结尾
          * 为config.packages中的每个值调用
            fixupPackageInfo(packageInfo)
              * 如果packageInfo是字符串则视为packageInfo的name
              * 定义packageInfo的name
              * 设定默认值 main: "main"
              * 如果没有location属性则把location设为name
              * 把packageMap存入全局变量map[name]中
              * 如果属性main的值以"./"开头, 则去除"./"
              * 把此packageInfo存入packs[name]中


