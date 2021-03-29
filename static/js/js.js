window.onload = function()
{
    $(".content_general").addClass("content_blockActive");
};


$(".btn_general").click(function()
{
    $(".content_general").addClass("content_blockActive");
    $(".content_singIn").removeClass("content_blockActive");
    $(".block_btn_header_general").addClass("active_block");
    $(".block_btn_header_singIn").removeClass("active_block");
    $(".content_registr").removeClass("content_blockActive");
});

$(".btn_singIn").click(function()
{
    $(".content_general").removeClass("content_blockActive");
    $(".content_singIn").addClass("content_blockActive");
    $(".block_btn_header_general").removeClass("active_block");
    $(".block_btn_header_singIn").addClass("active_block"); 
    $(".content_registr").removeClass("content_blockActive");   
});

$(".content_general").click(function()
{
    $(".content_general").removeClass("content_blockActive");
    $(".content_singIn").addClass("content_blockActive");
    $(".content_registr").removeClass("content_blockActive");
});


$(".btn_GoRegistr").click(function()
{
    $(".content_general").removeClass("content_blockActive"); 
    $(".content_singIn").removeClass("content_blockActive");
    $(".content_registr").addClass("content_blockActive");
});