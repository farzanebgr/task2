function addProductToOrder(productId){
    const productCount = $('#count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count='+ productCount).then(res => {
        console.log(res);
    })
}