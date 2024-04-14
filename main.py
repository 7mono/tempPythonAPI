import threading
import cv2


import chatgptapi
import voicebox
import voice2text
import chatgptapi
import opencv

def communication_thread():
    while True:
        print("何か質問はありますか？")
        question = voice2text.voice2text()
        if question == "ストップ":
            break
        answer = chatgptapi.chatGPTAPI(question)
        voicebox.text2voice(answer)


if __name__ == '__main__':
    intoro = "こんにちは、AI　Vtuberのケニーです。"
    voicebox.text2voice(intoro)

    v_thread = threading.Thread(target=communication_thread)
    v_thread.start()
    opencv.vtuber()
