function shoppingPaid(orderId, state, ) {
    $.get('/userpanel/shopping-paid/?orderId=' + orderId + '&state=' + state).then(res => {
        Swal.fire({
            icon: 'success',
            title: res.text,
            showConfirmButton: false,
            timer: 2000
        }).then((result) => {
                window.location.reload()
            })

    });
}