/*

*/

// 
const SOCKET_URL = `ws://${window.location.host}/chat/`
// 
const CHAT_SOCKET = new WebSocket(SOCKET_URL)

// 
CHAT_SOCKET.addEventListener("open",() => console.log("Успішне з`єднання"))
