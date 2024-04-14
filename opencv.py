import cv2

running = True
def vtuber():
    global running
    cap = cv2.VideoCapture("./aigpt.mp4")
    if not cap.isOpened():
        print("ビデオファイルを開くことができませんでした。")
        return

    try:
        while running:
            ret, frame = cap.read()
            if not ret:
                print("ビデオの末尾に到着しました最初から再生します。")
                cap.set(cv2.CAP_PROP_POS_FRAMES,0)
                continue

            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord("q"):
                break



    finally:
        cap.release()
        cv2.destroyAllWindows()


def stop_vtuber():
    global running
    running = False