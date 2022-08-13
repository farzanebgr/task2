function addProductToOrder(productId){
    const numbers = $('#numbers').val();
    $.get('/order/add-to-order?product_id=' + productId + '&numbers='+ numbers).then(res =>{
        console.log(res);
    })
}