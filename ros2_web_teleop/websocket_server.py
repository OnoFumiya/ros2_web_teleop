import asyncio
import json

from websockets.asyncio.server import serve
from websockets.server import ServerConnection


class WebSocketServer:
    """
    スマートフォンのGUIとWebSocket通信を行うサーバー。
    """

    def __init__(self, host="0.0.0.0", port=8080):
        self.host = host
        self.port = port

        # 現在接続しているGUI
        self.client = None

        # サーバー本体
        self.server = None

    async def start(self):
        """
        WebSocketサーバーを起動する。
        """

        self.server = await serve(
            self.handle_client,
            self.host,
            self.port
        )

        print(f"WebSocket server started: ws://{self.host}:{self.port}")

        # サーバーを起動したまま待機
        await self.server.serve_forever()

    async def handle_client(self, websocket: ServerConnection):
        """
        GUIが接続したときに呼ばれる。
        """

        self.client = websocket

        print("GUI connected")

        try:
            async for message in websocket:
                await self.handle_message(message)

        except Exception as e:
            print(f"WebSocket error: {e}")

        finally:
            print("GUI disconnected")

            # 現在の接続が切れた場合だけNoneにする
            if self.client == websocket:
                self.client = None

    async def handle_message(self, message):
        """
        GUIから受信したデータを処理する。
        """

        print(f"Received: {message}")

        try:
            data = json.loads(message)

        except json.JSONDecodeError:
            print("Invalid JSON")
            return

        # TODO:
        # ここでGUIから送られてきたデータを処理する
        #
        # 例:
        #
        # if data["type"] == "joystick":
        #     ...
        #
        # elif data["type"] == "emergency":
        #     ...

    async def send_message(self, data):
        """
        GUIへデータを送信する。
        """

        if self.client is None:
            return

        message = json.dumps(data)

        await self.client.send(message)


async def main():

    server = WebSocketServer(
        host="0.0.0.0",
        port=8080
    )

    await server.start()


if __name__ == "__main__":
    asyncio.run(main())