const joystickBase =
    document.getElementById("joystick-base");

const joystickStick =
    document.getElementById("joystick-stick");

const joystickValue =
    document.getElementById("joystick-value");


// 現在のジョイスティック値
let joystickX = 0.0;
let joystickY = 0.0;


// 現在操作しているか
let isDragging = false;


// ================================
// ジョイスティックの最大移動量
// ================================

const baseRadius =
    joystickBase.clientWidth / 2;

const stickRadius =
    joystickStick.clientWidth / 2;

const maxDistance =
    baseRadius - stickRadius;


// ================================
// 指がジョイスティックに触れた
// ================================

joystickBase.addEventListener(
    "pointerdown",
    (event) => {

        isDragging = true;

        joystickBase.setPointerCapture(
            event.pointerId
        );

        updateJoystick(event);
    }
);


// ================================
// 指を動かした
// ================================

joystickBase.addEventListener(
    "pointermove",
    (event) => {

        if (!isDragging) {
            return;
        }

        updateJoystick(event);
    }
);


// ================================
// 指を離した
// ================================

joystickBase.addEventListener(
    "pointerup",
    (event) => {

        isDragging = false;

        resetJoystick();
    }
);


// ================================
// ジョイスティックを更新
// ================================

function updateJoystick(event) {

    const rect =
        joystickBase.getBoundingClientRect();


    // ジョイスティック中心からの座標
    let x =
        event.clientX -
        (rect.left + rect.width / 2);

    let y =
        event.clientY -
        (rect.top + rect.height / 2);


    // 距離
    const distance =
        Math.sqrt(x * x + y * y);


    // 最大距離を超えないようにする
    if (distance > maxDistance) {

        x =
            x / distance * maxDistance;

        y =
            y / distance * maxDistance;
    }


    // スティック画像を移動
    joystickStick.style.transform =
        `translate(${x}px, ${y}px)`;


    // -1.0 ～ +1.0 に正規化
    joystickX =
        x / maxDistance;

    joystickY =
        -y / maxDistance;


    // 画面表示
    // joystickValue.innerHTML =
        // `X: ${joystickX.toFixed(2)}<br>
        //  Y: ${joystickY.toFixed(2)}`;


    // WebSocketで送信
    sendJoystickValue(
        joystickX,
        joystickY
    );
}


// ================================
// ジョイスティックを中央に戻す
// ================================

function resetJoystick() {

    joystickX = 0.0;
    joystickY = 0.0;


    joystickStick.style.transform =
        "translate(0px, 0px)";


    // joystickValue.innerHTML =
        // `X: 0.00<br>
        //  Y: 0.00`;


    sendJoystickValue(
        0.0,
        0.0
    );
}