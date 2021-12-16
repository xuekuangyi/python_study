# markdown 语法

## 标题
| 标题级别 | 效果 |
| ------ | --- |
| # | <h1> 一级标题 <h1/> |
| ## | <h2> 二级标题 <h2/> |

# #一级标题左侧1个#号
## #二级标题左侧2个#号
**……**
##### ###### 5级标题和6级标题颜色有区别，字号相同
###### ####### 最多可以在行最左侧6个#——六级标题

## 1.列表
无序列表
- 列表项1


## 字体
### 加粗
使用`**要加粗的文本**`方式来加粗，等同于html的`<b>加粗</b>`
### 倾斜
使用`*要倾斜的文本*`方式来倾斜，等同于html的`<i>倾斜</i>`
### 加粗倾斜
使用`***需加粗倾斜的文本***`方式来加粗且倾斜，等同于`<b><i>加粗且倾斜</i></b>`
### 删除线
使用 `~~需加删除线的文本~~`的方式来对文字使用删除线
### 其它的字体格式化方法
由于仅仅使用，使用html标签及其属性来控制字体显示，可以使用`<text><span>`等行内元素即可  

| 语法 | 效果 |
| ------ | --- |
| `<span style="color:red">颜色</span>` |<span style="color:red">颜色</span>|
|`<text style="font-size:30px">字号</text>`|<text style="font-size:30px">字号</text>|
|`<span style="font-size:30px; color:red; font-family:'仿宋'">多重控制</span>`|<span style="font-size:30px; color:red; font-family:'仿宋'">多重控制</span>|

>附:常用字体格式化的css属性

<table style="font-size:12px;color:#999999;width:100%;border-width: 1px;border-color: #729ea5;border-collapse: collapse">
<tr><th>Header 1</th><th>Header 2</th><th>Header 3</th><th>Header 4</th><th>Header 5</th></tr>
<tr><td>Row:1 Cell:1</td><td>Row:1 Cell:2</td><td>Row:1 Cell:3</td><td>Row:1 Cell:4</td><td>Row:1 Cell:5</td></tr>
<tr><td>Row:2 Cell:1</td><td>Row:2 Cell:2</td><td>Row:2 Cell:3</td><td>Row:2 Cell:4</td><td>Row:2 Cell:5</td></tr>
<tr><td>Row:3 Cell:1</td><td>Row:3 Cell:2</td><td>Row:3 Cell:3</td><td>Row:3 Cell:4</td><td>Row:3 Cell:5</td></tr>
<tr><td>Row:4 Cell:1</td><td>Row:4 Cell:2</td><td>Row:4 Cell:3</td><td>Row:4 Cell:4</td><td>Row:4 Cell:5</td></tr>
<tr><td>Row:5 Cell:1</td><td>Row:5 Cell:2</td><td>Row:5 Cell:3</td><td>Row:5 Cell:4</td><td>Row:5 Cell:5</td></tr>
<tr><td>Row:6 Cell:1</td><td>Row:6 Cell:2</td><td>Row:6 Cell:3</td><td>Row:6 Cell:4</td><td>Row:6 Cell:5</td></tr>
</table>

## 2.引用
使用 `>需要展示为引用的文本` 来实现，效果：
>这是一段引用的文本

**说明**：引用后必须要空一行才能结束引用块；  
**引用还能嵌套且与其它元素组合使用**：    
**嵌套**：>后再跟>即可，注意，跳出当前嵌套也是必须要加一空行；
<div>
>引用的第一层<br />
> >引用的第二层  <br /><!--注意加两个空格换行-->
>还在第二层<br />
> >>引用的第三层  <br />
> 还在第三层 <br />
> <br /><!--注意加一个空行跳出嵌套-->
> 引用的第一层<br />
</div>

**效果**：
>引用的第一层
> >引用的第二层  
> 还在第二层
> 
> >>引用的第三层
> 还在第三层
>
> 引用的第一层

**与其它元素叠加**
先写其它元素再最后再加引用的“>”

>引用与列表
> - 无序列表1级
>  - 无序列表2级
>1. 有序列表1级
>   1. 有序列表2级
> 代码块：
> ```python
> print("Hello World")
> ```

## 3.代码

**行内代码：**
使用 \`需要展示为行内的代码\` 来实现，效果：`行内代码`  
**段落代码：**
>\```python  
print('Hello World')  
\```

## 3.列表
**无序列表**
使用 `- 需要展示为无序列表的文字` 来实现，“-”也可用“+” 代替，注意“-”后要加空格，效果：
- 无序列表项1
+ 无序列表项2
列表可以缩进，使用“tab”，效果：
+ 无序列表一级
  + 无序列表二级
    + 无序列表三级
    + 无序列表三级

**有序列表**






### 表格
| 快捷键                                        | 作用                                   |
| --------------------------------------------- | -------------------------------------- |
| `ctrl + j`                                 | 显示可用的代码模板                     |



