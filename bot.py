from flask import Flask,request
import requests
token = "6633917435:AAE6qq-FBcnAH08A_quwG3V3BlJZXANqdo4"
app = Flask(__name__)
@app.route("/bot/", methods=['POST', 'GET'])
def bot():
    if request.method=="POST":
        data=request.get_json()
        chat_id=data["message"]["chat"]["id"]
        url=f"https://api.telegram.org/bot{token}/sendMessage"
        payload={
            "chat_id":chat_id,
            "text":"salom"
        }
        r=requests.get(url,params=payload)
        print(r.status_code, r.text)
        return {"message":"ok"}
if __name__ == "__main__":
    app.run(debug=True)fgvbfdzxbv