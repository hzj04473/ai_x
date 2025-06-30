# 자동완성이 안 될 경우 (가상환경 설정 안 된있는 경우) + cmd + shift + p : 가상환경 선택
import os
import time
from dotenv import load_dotenv
from decouple import config
from openai import OpenAI, OpenAIError

# 경고 메세지 무시
import warnings

warnings.filterwarnings("ignore")


# 1. client 생성
load_dotenv(".env")

# dotenv
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# decouple
client = OpenAI(api_key=str(config("OPENAI_API_KEY")))

# 2. assistant 생성 (assistant.id 필요)
assistant_cs = client.beta.assistants.create(
    name="CustomerSupportBot",
    instructions="당신은 고객 지원 챗봇입니다. 사용자 문의에 대해 30자 이내로 친철한 답변을 하세요",
    model="gpt-4o-mini",
)

# 3. thread 생성 : 기억담당
thread_cs = client.beta.threads.create()
print("챗봇이 시작됩니다. 종료를 원하시면, (종로 : '종료'나 'exit') 모든 대화이력은 저장됩니다.")

while True:
    user_input = input("user : ")

    if user_input.strip().lower() in ["종료", "exit"]:
        print("챗봇이 종료됩니다. 이용해 주셔서 감사합니다.")
        break

    if user_input == "":
        continue
    else:
        # 4 ~ 6 : user_input을 thread_cs에 추가하고 실행한 후 최종 답변 출력

        # 4. thread에 user_input 메세지 추가
        client.beta.threads.messages.create(thread_id=thread_cs.id, role="user", content=user_input)

        # 5. run 수행 (assistant.id, thread.id 필요)
        client.beta.threads.runs.create_and_poll(
            thread_id=thread_cs.id, assistant_id=assistant_cs.id
        )

        # 6. 최종 답변 출력
        messages = client.beta.threads.messages.list(thread_id=thread_cs.id)
        assistant_reply = messages.data[0]

        reply_text = ""
        if assistant_reply.content and assistant_reply.content[0].type == "text":
            reply_text = assistant_reply.content[0].text.value

        # print(f"user : {user_input}")  # 사용자 질문
        print(f"assistant : {reply_text}")  # 최신답변

# 7. 대화 이력 뽑아, 파일 출력
messages = client.beta.threads.messages.list(thread_id=thread_cs.id)

if messages.data:
    sorted_messages = sorted(messages.data, key=lambda data: data.created_at)

    with open("./data/ch7_chat_history.txt", "w", encoding="utf-8", errors="replace") as f:
        for message in sorted_messages:
            # 생성 시각 (message.created_at)을 datetime 형식으로 변환
            datetime_info = time.localtime(message.created_at)
            # 보기 좋은 문자열 형식으로 변환
            output_str = time.strftime("%Y-%m-%d %H:%M:%S", datetime_info)

            content_text = ""
            if message.content and message.content[0].type == "text":
                content_text = message.content[0].text.value

            f.write("{:9} ({}) : {}\n".format(message.role, output_str, content_text))
