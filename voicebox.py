import json
import requests
import simpleaudio
import speech_recognition as sr

def text2voice(introduction):
    # VOICEVOX APIのEndpoint
    localhost = "http://localhost"
    port = 50021
    #base_url = "http://localhost:50021"
    base_url = f"{localhost}:{port}"

    # 音声化するテキスト
#    text = "こんにちは、VOICEBOXの世界へようこそ。"
    text = introduction
    params = (
        ('text', text),
        ('speaker', 1),
    )
    # テキストを音声に変換するためのリクエストを送信
    query_response = requests.post(
        f"{base_url}/audio_query",
        params=params
    )
    # レスポンスから音声合成のクエリパラメータを取得
    audio_query = query_response.json()
    headers = {'Content-Type': 'application/json', }

    # 音声データを生成するリクエストを送信
    synthesis_response = requests.post(
        url=f"{base_url}/synthesis",
        headers=headers,
        params=params,
        data=json.dumps(query_response.json())
    )

    if synthesis_response.status_code == 200:
        # 音声データをファイルに保存
        with open('output.wav', 'wb') as f:
            f.write(synthesis_response.content)
            print("音声ファイルが保存されました。")
    else:
        print("エラーが発生しました。", synthesis_response.status_code)

    wav_obj = simpleaudio.WaveObject.from_wave_file("output.wav")
    play_obj = wav_obj.play()
    play_obj.wait_done()

    if play_obj.is_playing():
        print("Still playing.")

