function sendProductComments(productId){
     var comment = $('#commentText').val();
    var parentId = $('#parent_id').val();
$.get('/productions/add-product-comment/', {
    product_comment: comment,
    product_id: productId,
    parent_id: parentId,
    }).then(res =>{
    $('#comments_area').html(res);
    $('#commentText').val('');
    $('#parent_id').val('');

    if (parentId !== null && parentId !== '') {
        document.getElementById('single_comment_box_' + parentId).scrollIntoView({behavior: "smooth"});
    }
        else{
            document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});
    }
});
}
function fillParentId(parentId){
    $('#parent_id').val(parentId);
    document.getElementById('comment_form').scrollIntoView({behavior: "smooth"});

}