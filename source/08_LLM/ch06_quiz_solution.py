import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = OpenAI()

# Define file paths
text_file_path = os.path.join(os.path.dirname(__file__), "data", "ch06_quiz.txt")
mp3_file_path = os.path.join(os.path.dirname(__file__), "data", "ch06_quiz.mp3")


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that summarizes text to a maximum of 50 characters.",
            },
            {
                "role": "user",
                "content": f"Summarize the following text to a maximum of 50 characters: {text}",
            },
        ],
        max_tokens=50,
    )
    return response.choices[0].message.content


def convert_text_to_speech(text, voice="nova"):
    response = client.audio.speech.create(model="tts-1", voice=voice, input=text)
    return response


def save_audio_to_mp3(audio_response, file_path):
    # audio_response.stream_to_file(file_path)
    # 임시 버그 우회 방식
    with open(file_path, "wb") as f:
        f.write(audio_response.read())


if __name__ == "__main__":
    # Read the text file
    original_text = read_text_file(text_file_path)
    print(f"Original text read from {text_file_path}:\n{original_text}\n")

    # Summarize the text
    summarized_text = summarize_text(original_text)
    print(f"Summarized text (max 50 chars):\n{summarized_text}\n")

    # Convert summarized text to speech
    print(f"Converting summarized text to speech with 'nova' voice...")
    speech_response = convert_text_to_speech(summarized_text, voice="nova")

    # Save the audio to MP3
    save_audio_to_mp3(speech_response, mp3_file_path)
    print(f"Audio saved to {mp3_file_path}")
