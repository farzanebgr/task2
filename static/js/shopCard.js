function addProductToOrder(productId){
    const productCount = $('#count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count='+ productCount).then(res => {
        Swal.fire({
            title: 'ثبت محصول',
            text: res.text,
            icon: res.icon,
            showCancelButton: false,
            confirmButtonColor: '#3085d6',
            confirmButtonText: res.confirm_button_text
        }).then((result) => {
            if (result.isConfirmed && res.status === 'not_auth') {
                window.location.href = '/login/';
            }
        })
    });
}