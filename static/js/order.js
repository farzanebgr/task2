function removeOrderDetail(detailId) {
    $.get('/userpanel/remove-order-detail/?detailId=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}