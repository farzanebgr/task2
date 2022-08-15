function addProductToOrder(productId,productCount ) {
    const count = $('#count').val();
    $.get('/order/add-to-order?product_id=' + productId + '&count=' + count  + '&productCount=' + productCount).then(res => {
            Swal.fire({
                title: 'محصول',
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