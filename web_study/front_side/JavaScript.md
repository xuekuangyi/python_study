# JavaScript
## 背景
- JavaScript是由网景公司发明的运行在浏览器端的脚本语言，最初叫LiveScript。
- 有了JS后，网页变得丰富多彩动效十足，不再是静态的了，页面更具交互性。
- 因为与sun公司的合作，所以LiveScript改名为了JavaScript。
- JavaScript的“目标程序”以普通的文本形式保存并由浏览器直接执行。
- ECMA组织统一规范化脚本，JS和Jscript都实现了ECMA-Script规范。
---

+ **js可以做什么？**
改变HTML元素属性
```html
<!--通过定位HTML元素,指定元素属性style下的fontSize改变其字体大小-->
<button type="button" onclick="document.getElementById('forChange').style.fontSize='20px'">
   <span id="forChange">文字</span>
```
---
+ **如何“打印”结果？**  
JavaScript 能够以不同方式“显示”数据：
- 使用 `window.alert()` 写入警告框
- 使用 `document.write()` 写入 HTML 输出
- 使用 `innerHTML` 写入 `HTML `元素
- 使用 `console.log()` 写入浏览器控制台

**使用 innerHTML**
```html
<p id="showResult"></p>
<script><!-- 注意要放在后面 -->
  document.getElementById('showResult').innerHTML = '测试'
</script>
```
**使用 document.write()**

```html
onload(document.write(variety_01))
```

<font style="font-weight:bold; color:red">注意</font>：在 HTML 文档完全加载后使用 document.write() 将删除所有已有的 HTML   
**提示**：document.write() 方法仅用于测试。

**使用 console.log()**  
在浏览器中，可使用 console.log() 方法来显示数据。
通过 F12 来激活浏览器控制台，并在菜单中选择“控制台”。
---
**分号分隔 JavaScript 语句**
以分号结束语句不是必需的，但仍然强烈建议应该这么做。
**JavaScript 空白字符**
JavaScript 会忽略多个空格。故可以向脚本添加空格，以增强可读性。
**JavaScript 代码块**
代码块使用`{}`括起来，定义了一同执行的多条语句；

---
**JS注释**
- //单行注释
- /**/多行注释


# JS简介
1. JS是一门事件驱动型的编程语言；
2. 依靠事件去触发执行相应的代码块实现既定功能目标；
3. JS嵌入HTML中有三种方式：
   1. 标签行内方式；
   2. HTML内嵌代码块方式；
   3. 引入外部.js文件方式
4. JS中的语句逐条执行；
## JS代码怎么嵌入到HTML中

### HTML标签行内属性方式
```html
<!doctype html><!-- 行内方式 -->
<html>
    <head>
        <title>HTML中嵌入JS代码的行内方式</title>
    </head>
    <body>
        <input type="button" value="按钮" onclick="alert("点击事件")"/>
    </body>
</html>
```
### 页内代码块方式
```html
<!doctype html><!-- 页内代码块的方式 -->
<html>
    <head>
        <title>HTML中嵌入JS代码的代码块方式</title>
    </head>
    <body>
       <script type="text/javascript">
          /*
            在代码块中的代码会在onload的时候即执行
          * */
          alert("页内代码块方式")
       </script><!--代码必-->
    </body>
</html>
```
### 引用外部JS文件的方式
- 注意`<script src="">`区分`<style href="">`
- 注意该方式虽然与上面的页内代码块方式类似（仅多了标签属性src），但其**开始和结束标签之间即使写了JS代码也不会被执行**
```html
<!doctype html><!-- 页内代引用方式 -->
<html>
    <head>
       <!-- 引入外部文件的方式，依次执行 -->
       <script type="text/javascript" src="js_01.js">
          script标签之间即使写了JS也不会像页内代码块方式那样执行
       </script>
       <title>HTML中嵌入JS代码的代码块方式</title>
    </head>
    <body>
    </body>
</html>
```
```javascript
js_01.js
window.alert("外部独立JS");
```
外部 JavaScript 的优势
在外部文件中放置脚本有如下优势：
+ 分离了 HTML 和代码
+ 使 HTML 和 JavaScript 更易于阅读和维护
+ 已缓存的 JavaScript 文件可加速页面加载
如需向一张页面添加多个脚本文件 - 请使用多个 script 标签


## 一、JS中的变量：
1. **变量声明**：
JS是一种弱类型编程语言，通过右侧的值来确定变量类型，使用“var”关键字+变量名来完成变量声名；
所有 JavaScript 变量必须以唯一的名称的标识。这些唯一的名称称为标识符。JavaScript倾向于使用以小写字母开头的驼峰大小写：
```javascript
var variety_01 = '字符串';
var variety_02 = 1;
var variety_03 = true;
var variety_04 = new Object();
var variety_05 = 3.24;
window.alert("变量variety_01的类型是："+typeof variety_01+ "，值是："+variety_01)
alert("变量variety_02的类型是："+typeof variety_02+"，值是："+variety_02)
alert("变量variety_03的类型是："+typeof variety_03+"，值是："+variety_03)
alert("变量variety_04的类型是："+typeof variety_04+"，值是："+variety_04)
alert("变量variety_05的类型是："+typeof variety_05+"，值是："+variety_05)
```

2. **变量赋值**  
JavaScript 赋值运算符

| 运算符 | 例子     | 等同于      |
|--------|----------|-------------|
| =      | x = y    | x = y       |
| +=     | x += y   | x = x + y   |
| -=     | x -= y   | x = x - y   |
| *=     | x *= y   | x = x * y   |
| /=     | x /= y   | x = x / y   |
| %=     | x %= y   | x = x % y   |
| <<=    | x <<= y  | x = x << y  |
| >>=    | x >>= y  | x = x >> y  |
| >>>=   | x >>>= y | x = x >>> y |
| &=     | x &= y   | x = x & y   |
| ^=     | x ^= y   | x = x ^ y   |
| |=     | x |= y   | x = x | y   |
| **=    | x **= y  | x = x ** y  |

3. **数据类型**：  
JavaScript 是弱类型语言，且是动态类型
- 基本数据类型：
  - string
  - number
  - boolean
  - undefined
- 复杂数据类型

  - object：typeof 运算符把对象、数组或 null 返回 object。
  - function：typeof 运算符把函数返回为function


```javascript

var length = 7;                                 // 数字 number
var pi = 3.14;                                  // 数字 number
var lastName = "Gates";                         // 字符串 string
var cars = ["Porsche", "Volvo", "BMW"];         // 数组 object
var trueOrFalse = false;                        // 布尔 boolean
var x = {firstName:"Bill", lastName:"Gates"};   // 对象 object
var var_undefined;                              // undefined
typeof trueOrFalse                              // 输入结果为 boolean
function func(){}                               // 类型为function
var var_null = null;                            // 值是 null，但是类型仍然是对象




```


``` javascript

function() 
// Undefined 与 null 的值相等，但类型不相等：
```
Null
在 JavaScript 中，null 是 "nothing"。它被看做不存在的事物。
不幸的是，在 JavaScript 中，null 的数据类型是对象。

您可以把 null 在 JavaScript 中是对象理解为一个 bug。它本应是 null。

您可以通过设置值为 null 清空对象：

5. **运算**  
算数运算符：      



| 运算符 | 名称 | 举例|
| ---- | ---- |-----|
| + | 加法 |
| - | 减法 | 
| * | 乘法 |
| / | 除法 |
| % | 取余 |
| ++ | 递加1 | `var i = 5; i++`(i的值为6)
| -- | 递减1 |
| += | 加法赋值运算符 |
| *= | 乘法赋值运算符 |
| ** | 幂运算 | i = 2**4 i的值为16，与 Math.pow(x,y) 相同

**运算符优先级：**

| 值 | 运算符     | 描述             | 实例             |
|----|------------|------------------|------------------|
| 20 | ( )        | 表达式分组       | (3 + 4)          |
| 19 | .          | 成员             | person.name      |
| 19 | []         | 成员             | person["name"]   |
| 19 | ()         | 函数调用         | myFunction()     |
| 19 | new        | 创建             | new Date()       |
| 17 | ++         | 后缀递增         | i++              |
| 17 | --         | 后缀递减         | i--              |
| 16 | ++         | 前缀递增         | ++i              |
| 16 | --         | 前缀递减         | --i              |
| 16 | !          | 逻辑否           | !(x==y)          |
| 16 | typeof     | 类型             | typeof x         |
| 15 | **         | 求幂 (ES7)       | 10 ** 2          |
| 14 | *          | 乘               | 10 * 5           |
| 14 | /          | 除               | 10 / 5           |
| 14 | %          | 模数除法         | 10 % 5           |
| 13 | +          | 加               | 10 + 5           |
| 13 | -          | 减               | 10 - 5           |
| 12 | <<         | 左位移           | x << 2           |
| 12 | >>         | 右位移           | x >> 2           |
| 12 | >>>        | 右位移（无符号） | x >>> 2          |
| 11 | <          | 小于             | x < y            |
| 11 | <=         | 小于或等于       | x <= y           |
| 11 | >          | 大于             | x > y            |
| 11 | >=         | 大于或等于       | x >= y           |
| 11 | in         | 对象中的属性     | "PI" in Math     |
| 11 | instanceof | 对象的实例       | instanceof Array |
| 10 | ==         | 相等             | x == y           |
| 10 | ===        | 严格相等         | x === y          |
| 10 | !=         | 不相等           | x != y           |
| 10 | !==        | 严格不相等       | x !== y          |
| 9  | &          | 按位与           | x & y            |
| 8  | ^          | 按位 XOR         | x ^ y            |
| 7  | |          | 按位或           | x | y            |
| 6  | &&         | 逻辑与           | x && y           |
| 5  | ||         | 逻辑否           | x || y           |
| 4  | ? :        | 条件             | ? "Yes" : "No"   |
| 3  | =          | 赋值             | x = y            |
| 3  | +=         | 赋值             | x += y           |
| 3  | -=         | 赋值             | x -= y           |
| 3  | *=         | 赋值             | x *= y           |
| 3  | %=         | 赋值             | x %= y           |
| 3  | <<=        | 赋值             | x <<= y          |
| 3  | >>=        | 赋值             | x >>= y          |
| 3  | >>>=       | 赋值             | x >>>= y         |
| 3  | &=         | 赋值             | x &= y           |
| 3  | ^=         | 赋值             | x ^= y           |
| 3  | |=         | 赋值             | x |= y           |
| 2  | yield      | 暂停函数         | yield x          |
| 1  | ,          | 逗号             | 7 , 8            |


## 二. 函数

