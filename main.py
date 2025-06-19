from typing import Optional

from fastapi import FastAPI
from fastapi.responses import HTMLResponse #インポート
import random  # randomライブラリを追加

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]




### コードいろいろ... ###

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Hello! HTML!</h1>
            <table>
        <caption>講義スケジュール</caption>
        <thead>
            <tr>
                <th>曜日</th>
                <th>時間</th>
                <th>講義名</th>
                <th>教室</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>月曜日</td>
                <td>11:10 - 12:50</td>
                <td>基礎ゼミ</td>
                <td>なし</td>
                <td>2403教室</td>
            </tr>
            <tr>
                <td>火曜日</td>
                <td>13:40 - 15:20</td>
                <td>CGモデリング</td>
                <td>電大　太郎</td>
                <td>FI科教室</td>
            </tr>
            <tr>
                <td>水曜日</td>
                <td>9:20 - 11:10</td>
                <td>プログラミング演習</td>
                <td>電大　太郎</td>
                <td>丹羽ホール</td>
            </tr>
            <!-- 必要に応じて行を追加 -->
        </tbody>
    </table>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present):
    return {"response": f"サーバです。21歳のお誕生日おめでとう！ {present}ありがとう。お返しはディスクトップPCとS評価の単位です。"}  # f文字列というPythonの機能を使っている
