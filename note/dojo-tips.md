在学习dojo过程中，发现的一些东西：
1. 在for-in循环中，有的浏览器会略过在对象的prototype中存在的properties。
	比如
	for(var i in {toString: 1}) {
		alert('here');
	}
	在ie6中就不会弹出对话框，而在firefox中则可以。
	dojo中用has("bug-for-in-skips-shadowed")来测试这个特性。
2. dojo._lang._mixin 单个
   dojo._lang.mixin 复制多个(参数指定)
3. mixin 复制属性到对象，extend 复制属性到对象的prototype
