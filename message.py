# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from flask import Flask, request, render_template


# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate('C:/xampp/htdocs/myResume/serviceAccount.json')
# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)
# 初始化firestore
db = firestore.client()

app = Flask(__name__)
# @app.route('/')
# def home():
#     return "Hello, World!"
@app.route('/', methods=['POST'])
def receive_data():
    data = request.form
    # 處理接收到的資料
    name = data['name']
    email = data['email']
    messgae = data['message']
    print(name, email, messgae)
    try:
        doc = {
        'name': name,
        'email': email,
        'message': messgae,
        }
        # 建立文件 必須給定 集合名稱 文件id
        # 即使 集合一開始不存在 都可以直接使用

        # # 語法
        # # doc_ref = db.collection("集合名稱").document("文件id")
        # doc_ref = db.collection("myResume").document("contact_01")
        # # doc_ref提供一個set的方法，input必須是dictionary
        # doc_ref.set(doc)

        # 語法
        # collection_ref = db.collection("集合路徑")
        collection_ref = db.collection("myResume")
        # collection_ref提供一個add的方法，input必須是文件，型別是dictionary
        collection_ref.add(doc)
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error occurred while saving data", 500

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
