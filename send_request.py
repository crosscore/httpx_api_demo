# send_request.py
# server_a
import httpx
import os
import json

def main():
    # 送信するメッセージを指定
    message = {"message": "Hello from Server A!"}

    # JSONに変換
    message_json = json.dumps(message)

    # サーバーBのURL
    url = "http://server_b:8000/receive"

    # HTTP/2リクエストを送信
    with httpx.Client(http2=True) as client:
        response = client.post(url, data=message_json, headers={"Content-Type": "application/json"})
        print(response.status_code)
        print(response.json())

if __name__ == "__main__":
    main()
