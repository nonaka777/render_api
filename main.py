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
                <th>担当教員</th>
                <th>教室</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>月曜日</td>
                <td>09:00 - 10:30</td>
                <td>情報セキュリティ基礎</td>
                <td>田中 一郎</td>
                <td>101教室</td>
            </tr>
            <tr>
                <td>火曜日</td>
                <td>11:00 - 12:30</td>
                <td>ネットワーク工学</td>
                <td>佐藤 花子</td>
                <td>202教室</td>
            </tr>
            <tr>
                <td>水曜日</td>
                <td>13:00 - 14:30</td>
                <td>プログラミング演習</td>
                <td>鈴木 太郎</td>
                <td>PCルームA</td>
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
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}  # f文字列というPythonの機能を使っている
