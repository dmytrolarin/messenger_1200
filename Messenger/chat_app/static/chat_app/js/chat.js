/*
    Файл для взаємодії клієнта з сервером за протоколом WS
*/

// 
const groupId = document.getElementById('groupId').value
// Формуємо URL адресу для WS-з'єднання за поточним хостом
const SOCKET_URL = `ws://${window.location.host}/chat/${groupId}`
// Ініціалізуємо WebSocket (Створюємо WS-з'єднання)
const CHAT_SOCKET = new WebSocket(SOCKET_URL)

// Після успішного з'єднання повідомлення виводится у консоль
CHAT_SOCKET.addEventListener("open",() => console.log("Успішне з`єднання"))

// 
function processMessageTime(text){
    // 
    let date = new Date(text)
    // 
    let dateText = date.toLocaleString();
    // 
    return dateText
}

// 
const messageTimes = document.querySelectorAll(".message-time")
// 
for (let messageTime of messageTimes){
    // 
    let text = messageTime.textContent
    // 
    messageTime.textContent = processMessageTime(text)
}

// Отримуємо DOM-елемент, в який будуть додаватися нові повідомлення
const messages = document.getElementById("messages");
// Слухаємо події надходження повідомлень від WebSocket-з'єднання
CHAT_SOCKET.addEventListener("message", (event) => {
    // Розбираємо отриманий JSON-рядок у вигляді об'єкта
    let data = JSON.parse(event.data);
    // 
    let localTime = processMessageTime(data.datetime)
    // Додаємо нове повідомлення до вмісту блоку з повідомленнями
    messages.innerHTML += `<p>${data.message} (${localTime})</p>`;
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
