function removeOrderDetail(detailId) {
    $.get('/userpanel/remove-order-detail/?detailId=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

function changeOrderDetailCount(detailId, state) {

    $.get('/userpanel/change-order-detail/?detailId=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'there_is_no_product') {
             Swal.fire({
                 title: 'محصول',
                 text: res.text,
                 icon: res.icon,
                 showCancelButton: false,
                 confirmButtonColor: '#3085d6',
                 confirmButtonText: res.confirm_button_text
             });
        }
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

