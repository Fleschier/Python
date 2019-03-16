// $(document).ready(function(){
//     // alert("good");
//     $("#login").click(function(){
//         var user = $("#username").val();
//         var pwd = $("#password").val();
//         alert("username: "+user);
//     });
// });

//采用ajax技术
$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var us_pwd = {"username":user, "password":pwd};     //将user 和 pwd 值，放到一个 json 对象中
        $.ajax({
            type:"post",
            url:"/login.html",
            data:us_pwd,
            cache:false,
            success:function(data){
                alert(data);
            },
            error:function(){
                alert("error!");
            },
        });
    });
});

// type：post还是get。
// url：post或者get的地址
// data：传输的数据，包括三种：（1）html拼接的字符串；（2）json数据；（3）form表单经serialize()序列化的。上面传输的就是json数据，这也是经常用到的一种方式。
// cache：默认为true，如果不允许缓存，设置为false.
// success：请求成功时执行回调函数。上面将返回的data用alert方式弹出来
// error：如果请求失败所执行的函数。