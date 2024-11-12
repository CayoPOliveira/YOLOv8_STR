import cv2
from flask import Flask, Response

app = Flask(__name__)

def generate_frames():
    # Defina o endereço de IP e porta de acesso da câmera do celular
    # Exemplo para câmera IP: 'http://192.168.0.100:8080/video'
    # Substitua pela URL fornecida pelo app de câmera do seu celular
    camera_url = 'http://192.168.100.120:4747/video'
    cap = cv2.VideoCapture(camera_url)

    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Codifique o frame como JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Use o frame para stream
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Inicia o servidor Flask no IP e porta desejados
    app.run(host='0.0.0.0', port='5000')