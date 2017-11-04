// 左侧菜单点击效果

$("#sidlenav .list_dt").on("click", function () {

    $('#sidlenav').perfectScrollbar();
    $('#sidlenav .list_dd').stop();

    // $('.scroll').perfectScrollbar();
    // $('.list_dd').stop();

    $(this).siblings("dt").removeAttr("id");

    if ($(this).attr("id") == "open") {
        $(this).removeAttr("id").siblings("dd").slideUp();
    } else {
        $(this).attr("id", "open").next().slideDown().siblings("dd").slideUp();
    }

});