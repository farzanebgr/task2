function removeOrderDetail(detailId) {
    $.get('/userpanel/remove-order-detail/?detailId=' + detailId).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

function changeOrderDetailCount(detailId, state) {
    $.get('/userpanel/change-order-detail/?detailId=' + detailId + '&state=' + state).then(res => {
        if (res.status === 'success') {
            $('#order-detail-content').html(res.body);
        }
    });
}

