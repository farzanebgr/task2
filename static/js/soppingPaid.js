function shoppingPaid(orderId,productCount) {
    const customerCount = $('#customerCount').val();
    $.get('/userpanel/shopping-paid/?orderId=' + orderId + '&productCount=' + productCount,{
        customerCount : customerCount,
    }).then(res => {
        Swal.fire({
            icon: res.icon,
            title: res.text,
            showConfirmButton: false,
            timer: 2000
        }).then((result) => {
                window.location.reload()
            })

    });
}