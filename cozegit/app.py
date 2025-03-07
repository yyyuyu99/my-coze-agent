from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import uuid
from cozepy import (
    Coze, 
    TokenAuth, 
    Message,
    ChatEventType,
    COZE_CN_BASE_URL
)

app = Flask(__name__)
CORS(app)

# 配置信息
COZE_API_TOKEN = "pat_HGfUtiK2S4a4pPEhGFyqr4SzG4bTrGAl90iVOJ5bInJVg8xGzckp2vI67UjLchYp"
BOT_ID = "7472641110310322230"

# 初始化Coze客户端
coze = Coze(
    auth=TokenAuth(token=COZE_API_TOKEN),
    base_url=COZE_CN_BASE_URL
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    question = data.get('question', '')
    
    if not question:
        return jsonify({'error': '问题不能为空'}), 400
    
    try:
        response_text = ""
        token_count = 0
        
        # 生成随机用户ID
        user_id = str(uuid.uuid4())
        
        # 开始对话
        for event in coze.chat.stream(
            bot_id=BOT_ID,
            user_id=user_id,
            additional_messages=[
                Message.build_user_question_text(question),
            ],
        ):
            if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                response_text += event.message.content
                
            if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
                token_count = event.chat.usage.token_count
        
        return jsonify({
            'response': response_text,
            'token_count': token_count
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# ... 其他代码保持不变 ...

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))