const GUI_WIDTH =   585;
const GUI_HEIGHT = 1239;

const gui = document.getElementById("gui");
const canvas = document.getElementById("canvas");


function updateGUI() {

    const windowWidth = window.innerWidth;
    const windowHeight = window.innerHeight;

    // 横方向・縦方向それぞれの倍率
    const scaleX = windowWidth / GUI_WIDTH;
    const scaleY = windowHeight / GUI_HEIGHT;

    // 小さい方を採用して、全体が画面内に収まるようにする
    let min_scale = Math.min(scaleX, scaleY);

    // 小さい方を採用して、全体が画面内に収まるようにする
    let sel_scale;
    if (windowWidth < windowHeight) {
        // 縦のほうが長い場合
        sel_scale = scaleX;
    } else {
        // 横のほうが長い場合
        sel_scale = scaleY;
    }

    // if (min_scale != sel_scale) {
    //     sel_scale = sel_scale/2 + min_scale/2;
    // }

    // 実際に表示されるキャンバスサイズ
    const width = GUI_WIDTH * sel_scale;
    const height = GUI_HEIGHT * sel_scale;

    // 画面中央に配置
    const left = (windowWidth - width) / 2;
    const top = (windowHeight - height) / 2;

    // 仮想キャンバスのサイズ
    canvas.style.width = `${GUI_WIDTH}px`;
    canvas.style.height = `${GUI_HEIGHT}px`;

    // 拡大縮小して中央配置
    canvas.style.transform =
        `translate(${left}px, ${top}px) scale(${sel_scale})`;
}


// ウィンドウサイズが変わったら再計算
window.addEventListener("resize", updateGUI);


// 最初にも実行
updateGUI();