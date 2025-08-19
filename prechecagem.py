import cv2
import sounddevice as sd
import numpy as np
import urllib.request
import time

def checar_camera():
    cap = cv2.VideoCapture(0)  # 0 = câmera padrão
    if not cap.isOpened():
        return False, "❌ Câmera não encontrada ou não está funcionando."
    
    ret, frame = cap.read()
    cap.release()
    if not ret or frame is None:
        return False, "❌ Não foi possível capturar imagem da câmera."
    
    return True, "✅ Câmera funcionando corretamente."

def checar_microfone():
    try:
        duration = 3  # segundos
        fs = 44100   # taxa de amostragem
        print("\n🎙️ Fale algo durante os próximos 3 segundos...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        if np.max(np.abs(recording)) < 0.01:
            return False, "⚠️ Microfone detectado, mas não captou som."
        return True, "✅ Microfone funcionando corretamente."
    except Exception as e:
        return False, f"❌ Erro no microfone: {str(e)}"

def checar_internet():
    url = "http://www.google.com"
    try:
        start_time = time.time()
        urllib.request.urlopen(url, timeout=5)
        latency = time.time() - start_time
        if latency > 2:
            return False, f"⚠️ Internet lenta (resposta: {latency:.2f}s)"
        return True, f"✅ Internet OK (resposta: {latency:.2f}s)"
    except:
        return False, "❌ Sem conexão com a internet."

def pre_checagem():
    print("\n🔍 Iniciando pré-checagem da consulta online...\n")

    cam_ok, cam_msg = checar_camera()
    print("📷", cam_msg)

    mic_ok, mic_msg = checar_microfone()
    print("🎤", mic_msg)

    net_ok, net_msg = checar_internet()
    print("🌐", net_msg)

    if cam_ok and mic_ok and net_ok:
        print("\n✅ Tudo pronto! Você pode realizar a consulta online sem problemas.")
    else:
        print("\n⚠️ Alguns problemas foram detectados. Entre em contato com o suporte.")

if __name__ == "__main__":
    pre_checagem()


