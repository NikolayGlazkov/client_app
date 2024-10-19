// Функция для обновления времени
function updateTime() {
    var now = new Date();
    var hours = String(now.getHours()).padStart(2, '0');
    var minutes = String(now.getMinutes()).padStart(2, '0');
    var seconds = String(now.getSeconds()).padStart(2, '0');
    var timeString = hours + ":" + minutes + ":" + seconds;
    document.getElementById('clock').innerHTML = timeString;
}

// Обновляем время каждую секунду
setInterval(updateTime, 1000);

// Обновляем время сразу после загрузки страницы
window.onload = updateTime;


document.getElementById('search-client').addEventListener('click', function(event) {
    event.preventDefault();
    document.getElementById('inn-modal').style.display = 'block';
});

document.getElementById('close-modal').addEventListener('click', function() {
    document.getElementById('inn-modal').style.display = 'none';
});

document.getElementById('inn-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const inn = document.getElementById('inn-input').value;
    
    // Переход на страницу с деталями клиента
    window.location.href = `/client/${inn}/`;  // Измените на правильный путь
});