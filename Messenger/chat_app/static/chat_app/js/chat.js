/*
    Файл для взаємодії клієнта з сервером за протоколом WS
*/

// Формуємо URL адресу для WS-з'єднання за поточним хостом
const SOCKET_URL = `ws://${window.location.host}/chat/`
// Ініціалізуємо WebSocket (Створюємо WS-з'єднання)
const CHAT_SOCKET = new WebSocket(SOCKET_URL)

// Після успішного з'єднання повідомлення виводится у консоль
CHAT_SOCKET.addEventListener("open",() => console.log("Успішне з`єднання"))

// 
const messages = document.getElementById("messages");
// 
CHAT_SOCKET.addEventListener("message", (event) => {
    // 
    let data = JSON.parse(event.data);
    // 
    messages.innerHTML += `<p>${data.message}</p>`;
})

// 
const messageForm = document.querySelector("#messageForm");
// 
const messageTextInput = document.querySelector("#id_message");
// 
messageForm.addEventListener("submit", (event) => {
    // 
    event.preventDefault();
    // 
    let message = messageTextInput.value;
    // 
    let dataToSend = {"message": message};
    // 
    let JSONString = JSON.stringify(dataToSend);
    // 
    CHAT_SOCKET.send(JSONString);
    // 
    messageForm.reset()
}
)
