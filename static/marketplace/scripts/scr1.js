document.addEventListener('DOMContentLoaded', function () {
    // Обработчик события для кнопок "Обновить заказ"
    document.querySelectorAll('.btnСhangeOrd').forEach(function (btn) {
        btn.addEventListener('click', function () {
            var orderId = this.getAttribute('order-id');
            window.location.href = `/marketplace/orders/${orderId}/`;
        });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    var showGoodsBtn = document.getElementById('showGoodsBtn');
    var goodsList = document.getElementById('goodsList');
    var ordStr = document.getElementById('formOrdStr')

    showGoodsBtn.addEventListener('click', function () {
        goodsList.style.display = goodsList.style.display === 'none' ? 'grid' : 'none';
        ordStr.style.display = ordStr.style.display === 'none' ? 'grid' : 'none';
    });
});