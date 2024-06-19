# receive_request.py
# server_b
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/receive")
async def receive(request: Request):
    data = await request.json()
    target_var = data.get("TARGET_VAR", "default_value")

    # 受信した変数に基づいて挙動を変更
    if target_var == "special_value":
        response = {"message": "Special behavior activated!"}
    else:
        response = {"message": f"Received {target_var}"}

    print(response)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
