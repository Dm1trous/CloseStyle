function showModal(productId) {
    var modal = document.getElementById("cart-modal-" + productId);
    modal.style.display = "block";
}

function closeModal(productId) {
    var modal = document.getElementById("cart-modal-" + productId);
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        var modals = document.getElementsByClassName('modal');
        for (var i = 0; i < modals.length; i++) {
            modals[i].style.display = "none";
        }
    }
};

// Новая функция для показа уведомления
function showNotification() {
    var notificationBar = document.getElementById('notification-bar');
    notificationBar.style.display = 'block';
    setTimeout(function() {
        notificationBar.style.display = 'none';
    }, 2000); // Убрать уведомление через 2 секунды
}

function addToCart(productId, sizeId, addToCartUrl) {
    fetch(addToCartUrl.replace('0', productId) + '?size_id=' + sizeId, {
        method: 'GET',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
    .then(response => {
        if (response.ok) {
            closeModal(productId);
            showNotification(); // Показываем уведомление
        } else {
            console.error('Ошибка добавления в корзину.');
        }
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
}

