const statusElement =
    document.getElementById("connection-status");


const websocket = new WebSocket(
    "ws://192.168.1.29:8080"
);


// ================================
// 接続成功
// ================================

websocket.addEventListener("open", () => {

    console.log("WebSocket connected");

    statusElement.textContent =
        "WebSocket: CONNECTED";
});


// ================================
// Pythonから受信
// ================================

websocket.addEventListener("message", (event) => {

    console.log(
        "Received from Python:",
        event.data
    );
});


// ================================
// エラー
// ================================

websocket.addEventListener("error", (error) => {

    console.error(
        "WebSocket error:",
        error
    );

    statusElement.textContent =
        "WebSocket: ERROR";
});


// ================================
// 切断
// ================================

websocket.addEventListener("close", () => {

    console.log(
        "WebSocket disconnected"
    );

    statusElement.textContent =
        "WebSocket: DISCONNECTED";
});


// ================================
// ジョイスティック送信
// ================================

function sendJoystickValue(x, y) {

    const data = {

        type: "joystick",

        x: x,
        y: y
    };


    websocket.send(
        JSON.stringify(data)
    );


    console.log(
        "Joystick:",
        data
    );
}