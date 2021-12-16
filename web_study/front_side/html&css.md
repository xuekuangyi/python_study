#HTML与CSS笔记


## 一、HTML基础
**HTML 是用来描述网页的一种语言。**

- HTML 指的是超文本标记语言 (**H**yper **T**ext **M**arkup **L**anguage)
- HTML 不是一种编程语言，而是一种**标记语言** (markup language)
- 标记语言是一套**标记标签** (markup tag)
- HTML 使用标记标签来描述网页

**HTML 标签**
HTML 标记标签通常被称为 HTML 标签 (HTML tag)。

- HTML 标签是由**尖括号包围的关键词**，比如 <html>
- HTML 标签**通常是成对出现的**，比如 <b> 和 </b>
- 标签对中的第一个标签是**开始标签**，第二个标签是**结束标签**
- 开始和结束标签也被称为开放标签和闭合标签

**HTML 文档 = 网页**
- HTML 文档描述网页
- HTML 文档包含 HTML 标签和纯文本
- HTML 文档也被称为网页

Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML 标签，而是使用标签来解释页面的内容

- \<html> 与 \<html> 之间的文本描述网页
- \<body> 与 \</body> 之间的文本是可见的页面内容
- \<h1> 与 \</h1> 之间的文本被显示为标题
- \<p> 与 \</p> 之间的文本被显示为段落

## 二、常用HTML元素
1. `<html></html>`标签：
2. `<head></head>`标签：  
`<head> `元素是所有头部元素的容器。`<head>`内的元素可包含脚本，
指示浏览器在何处可以找到样式表，提供元信息，等等。  
这些标签都可以添加到 head 部分：
`<title>`、`<base>`、`<link>`、`<meta>`、`<script>` 以及 `<style>`。
3. **\<title>\</title>**
4. **\<hn>\</hn>标题**  
HTML 标题（Heading）是通过 \<h1> - \<h6> 等标签进行定义的。
5. **\<p>\</p>HTML 段落**  
HTML 段落是通过 <p> 标签进行定义的。
6. **\<a>\</a>超链接**  
\<a href="http://www.baidu.com">百度首页\</a>
7. **\<img src="URL"" />图片**
8. 1. **链接**：
- 链接采用`<a href="URL">链接元素</a>`来实现，其中，链接元素可仅仅是文字，可以是其它的HTML元素
- `<a>`标签的target属性:
<table>
  <tbody>
    <tr style="background: black; color: aliceblue">
        <th>值</th>
        <th>描述</th>
  </tr>  
  <tr>
    <td>_blank</td>
    <td>在新窗口中打开被链接文档。</td>
  </tr>
  <tr>
    <td>_self</td>
    <td>默认。在相同的框架中打开被链接文档。</td>
  </tr>
  <tr>
    <td>_parent</td>
    <td>在父框架集中打开被链接文档。</td>
  </tr>
  <tr>
    <td>_top</td>
    <td>在整个窗口中打开被链接文档。</td>
  </tr>
  <tr>
    <td><i>framename</i></td>
    <td>在指定的框架中打开被链接文档。</td>
  </tr>
</tbody></table>

- 元素的name属性：
name 属性规定锚（anchor）的名称。  
- 您可以使用 name 属性创建 HTML 页面中的书签。

书签不会以任何特殊方式显示，它对读者是不可见的。

当使用命名锚（named anchors）时，
直接创建跳至该命名锚（比如页面中某个小节）的链接，
这样使用者就无需不停地滚动页面来寻找他们需要的信息，页面直接跳转到对应的标签位置；
```html
<html>
    <body>
        <a href="#bookmark_01">点击页面滚动到对应的锚点位置</a>
        <p id="bookmark_01">点击锚点后滚动到的位置</p>
    <div ></div>
    </body>
</html>

```
<font style="color:brown; font-weight:bolder">注意：</font>可以使用 id 属性来替代 name 属性，命名锚同样有效
2. **图像**  
- **`<img>`和源属性：**  
`<img> `是空标签，意思是说，它只包含属性，并且没有闭合标签。<img src="URL" />
- 图片与文字垂直方式对齐：  
`<p>图像 <img src="/i/eg_cute.gif" align="bottom"> 在文本中</p>`,并不提倡使用align属性，而应该是统一使用样式表来接管样式相关配置；
- **alt替换文字属性**  
`<img src="boat.gif" alt="指向图片则展示该提示文字" />`
图片是以文件形式加载，对网页加载速度影响极大，所以应该谨慎使用图片并且采用必要手段进行变通处理，减小流量消耗并提升页面加载速度；  
`<div style="background-image: url("")">`背景图；

提示：  
HTML 标签对大小写不敏感：`<P>` 等同于 `<p>`。许多网站都使用大写的 HTML 标签。  
W3School 使用的是小写标签，因为万维网联盟（W3C）在 HTML 4 中推荐使用小写，而在未来 (X)HTML 版本中强制使用小写。
## 三、HTML元素  
1. **HTML元素**  
HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。

| 开始标签 | 元素内容 | 结束标签 |
| ---- | ---- |-----|
| \<p> | 段落内容 |\</p> |
| \<a href="www.baidu.com">|百度首页| \</a> |
| \<br />||
2. **HTML 元素语法**  
- HTML 元素以开始标签起始
- HTML 元素以结束标签终止 部分标签没有终止标签，如`<img />`、`<br />`
- **元素的内容**是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）,如一部分`<input>`元素
- 空元素在开始标签中进行关闭（以开始标签的结束而结束），如`<br />`
- 大多数 HTML 元素可拥有属性,如`<a href="www.baidu.com">|`
3.HTML元素嵌套
大多数 HTML 元素可以嵌套——在该元素的开始和结束标签之间夹上另外的HTML元素。
```html
<html><!-- <html>标签定义了整个HTML文档 -->
    <title>标题</title>
    <body>
        <p>
            段落1
        </p>
    </body>
</html>
```
HTML 文档由嵌套的 HTML 元素构成。
## 三、HTML属性
HTML 标签可以拥有属性。属性提供了有关 HTML 元素的更多的信息。
属性总是以名称/值对的形式出现，比如：`name="value"`， 用等号连接属性名与属性值，属性值要用引号括起来；  
属性总是在 HTML 元素的**开始标签**中规定。  
`<a href="www.baidu.com">百度首页</a>`
`<img src="/img/logo.png" />`
`<h1 align="center"> `

## 四、样式
1. **内联样式：**  
也称为行内样式，因为它是使用标签内的**style属性**直接写明样式内容，显著的优点是十分的便捷、高效；但是同时也造成了**不能够重用样式的缺点**。通常内联CSS作为测试使用，可以查找代码中bug。
**HTML 的 style 属性提供了一种改变所有 HTML 元素的样式的通用方法**。  
避免使用已被列为废弃的标签和属性
<table>
    <tbody>
    <tr style="background: black; color: aliceblue">
        <th style="width:40%;">标签</th>
        <th>描述</th>
    </tr>
    <tr>
        <td>&lt;center&gt;</td>
        <td>定义居中的内容。</td>
    </tr>
    <tr>
        <td>&lt;font&gt; 和 &lt;basefont&gt;</td>
        <td>定义 HTML 字体。</td>
    </tr>
    <tr>
        <td>&lt;s&gt; 和 &lt;strike&gt;</td>
        <td>定义删除线文本</td>
    </tr>
    <tr>
        <td>&lt;u&gt;</td>
        <td>定义下划线文本</td>
    </tr>
    <tr style="background: black; color: aliceblue">
        <th>属性</th>
        <th>描述</th>
    </tr>
    <tr>
        <td>align</td>
        <td>定义文本的对齐方式</td>
    </tr>
    <tr>
        <td>bgcolor</td>
        <td>定义背景颜色</td>
    </tr>
    <tr>
        <td>color</td>
        <td>定义文本颜色</td>
    </tr>
    </tbody>
</table>

示例：
```html
<html>
    <body style="background-color:yellow">
        <h2 style="background-color:red">二级标题</h2>
        <!-- 多个样式属性和值之间使用分号断句 -->
        <p style="background-color:green; font-size: large">段落</p>
    </body>
</html>

```
2. **内部样式；**  
内部样式也称为页级样式，因为它是形式为`<style>样式表内容</style>`嵌套在HTML页面的`<head></head>`中；
3. **外联样式**：  
外联样式也被称为外部样式，采用独立的.css文件，并使用`<style href="css文件URL"></style>或<head><link rel="stylesheet" type="text/css" href="mystyle.css"></head>`的形式引入HTML中并发生作用。该种方式的css文件可被多个页面引用，进一步提高了复用性和性能；
实际项目中多采



## 五、关键元素

## 表单类标签

3. **表格table：**


## 六、响应式设计





