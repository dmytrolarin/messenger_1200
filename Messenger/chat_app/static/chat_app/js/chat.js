/*
    Файл для взаємодії клієнта з сервером за протоколом WS
*/

// Формуємо URL адресу для WS-з'єднання за поточним хостом
const SOCKET_URL = `ws://${window.location.host}/chat/`
// Ініціалізуємо WebSocket (Створюємо WS-з'єднання)
const CHAT_SOCKET = new WebSocket(SOCKET_URL)

// Після успішного з'єднання повідомлення виводится у консоль
CHAT_SOCKET.addEventListener("open",() => console.log("Успішне з`єднання"))

// Отримуємо DOM-елемент, в який будуть додаватися нові повідомлення
const messages = document.getElementById("messages");
// Слухаємо події надходження повідомлень від WebSocket-з'єднання
CHAT_SOCKET.addEventListener("message", (event) => {
    // Розбираємо отриманий JSON-рядок у вигляді об'єкта
    let data = JSON.parse(event.data);
    // Додаємо нове повідомлення до вмісту блоку з повідомленнями
    messages.innerHTML += `<p>${data.message}</p>`;
})

// Створюємо константу messageForm з об'єктом форми
const messageForm = document.querySelector("#messageForm");
// Створюємо константу messageTextInput об'єктом поля з повідомленням
const messageTextInput = document.querySelector("#id_message");
// Прослуховування подію відправки форми
messageForm.addEventListener("submit", (event) => {
    // Зупиняємо дію за замовучванням (відправку форми)
    event.preventDefault();
    // Створюємо змінну message й задаємо значення з константи messageTextInput
    let message = messageTextInput.value;
    // Створюємо об'єкт для відправки на клієнт
    let dataToSend = {"message": message};
    // Створюємо JSONString та перетворюємо його в string
    let JSONString = JSON.stringify(dataToSend);
    // Відправляємо JSONString на сервер
    CHAT_SOCKET.send(JSONString);
    // Очищуємо messageForm без оновлення сторінки
    messageForm.reset()
}
)
