import os
import uuid
from cozepy import (
    Coze, 
    TokenAuth, 
    Message, 
    ChatStatus, 
    MessageContentType, 
    ChatEventType,
    COZE_CN_BASE_URL
)

def chat_with_coze(question):
    # 直接使用配置信息
    coze_api_token = "pat_HGfUtiK2S4a4pPEhGFyqr4SzG4bTrGAl90iVOJ5bInJVg8xGzckp2vI67UjLchYp"
    bot_id = "7472641110310322230"
    
    # 初始化Coze客户端
    coze = Coze(
        auth=TokenAuth(token=coze_api_token),
        base_url=COZE_CN_BASE_URL
    )
    
    # 生成随机用户ID
    user_id = str(uuid.uuid4())
    
    # 开始对话
    try:
        for event in coze.chat.stream(
            bot_id=bot_id,
            user_id=user_id,
            additional_messages=[
                Message.build_user_question_text(question),
            ],
        ):
            if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
                print(event.message.content, end="", flush=True)

            if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
                print("\n")
                print("Token使用量:", event.chat.usage.token_count)
    except Exception as e:
        print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    while True:
        user_input = input("\n请输入您的问题 (输入'quit'退出): ")
        if user_input.lower() == 'quit':
            break
        chat_with_coze(user_input) 