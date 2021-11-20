// window.alert("Hello JS")
// 变量学习
var var_str = '字符串';
var var_number = 1;
var var_number_02 = 3.24;
var var_boolean = true;
var var_object = new Object();
var var_list = ["Porsche", "Volvo", "BMW"];
var var_undefined;
var var_null = null;
function fun(){

}

// alert("变量var_str的类型是："+typeof var_str + "，值是：" + var_str)
// alert("变量var_number的类型是："+typeof var_number + "，值是：" + var_number)
// alert("变量var_number_02的类型是："+typeof var_number_02 + "，值是：" + var_number_02)
// alert("变量var_boolean的类型是："+typeof var_boolean + "，值是：" + var_boolean)
// alert("变量var_object的类型是："+typeof var_object + "，值是："+ var_object)
// alert("变量var_list的类型是："+typeof var_list + "，值是：" + var_list)
// alert("变量var_undefined的类型是："+typeof var_undefined + "，值是：" + var_undefined)


// onload(document.getElementById('showResult').innerHTML='22')

// 注意：在 HTML 文档完全加载后使用 document.write() 将删除所有已有的 HTML ：
onload(

    document.write(
                    "变量var_str的类型是："+typeof var_str + "，值是：" + var_str + "<br />",
                    "变量var_number的类型是："+typeof var_number + "，值是：" + var_number + "<br />",
                    "变量var_number_02的类型是："+typeof var_number_02 + "，值是：" + var_number_02 + "x`<br />",
                    "变量var_boolean的类型是："+typeof var_boolean + "，值是：" + var_boolean + "<br />",
                    "变量var_object的类型是："+typeof var_object + "，值是："+ var_object + "<br />",
                    "变量var_list的类型是："+typeof var_list + "，值是：" + var_list + "<br />",
                    "变量var_undefined的类型是："+typeof var_undefined + "，值是：" + var_undefined + "<br />",
                    "变量var_null的类型是："+typeof var_null + "，值是：" + var_null + "<br />",
                    "函数fun()的类型是："+typeof fun() + "，值是：" + fun() + "<br />"
                    )
)
doc