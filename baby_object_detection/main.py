import streamlit as st
from ultralytics import YOLO
from PIL import Image
import os
import cv2
import subprocess
import time

# Konfigurasi halaman
st.set_page_config(page_title="Baby Object Detection CCTV-Style", layout="centered")
st.title("👶 Baby Object Detection CCTV-Style")

# Upload file
uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4", "avi", "mov"])

# Load model
model = YOLO("baby_model.pt")

def check_for_tepi_kasur(result):
    detected_labels = []
    try:
        boxes = result.boxes
        if boxes is not None:
            classes = boxes.cls.cpu().numpy().astype(int)
            names = result.names
            detected_labels = [names[i] for i in classes]
    except Exception as e:
        print(f"Error checking labels: {e}")
    return "tepi_kasur" in detected_labels

if uploaded_file:
    file_type = uploaded_file.type

    if "image" in file_type:
        image = Image.open(uploaded_file)
        st.image(image, caption="📷 Uploaded Image", use_container_width=True)
        tmp_path = "temp_uploaded_image.png"
        image.save(tmp_path)
        st.write("🔍 Running detection on image...")

        results = model.predict(source=tmp_path, conf=0.2, iou=0.3, agnostic_nms=True, deterministic=True)

        if check_for_tepi_kasur(results[0]):
            st.warning("⚠️ Peringatan: 'tepi_kasur' terdeteksi pada gambar ini!")
            st.toast("⚠️ 'tepi_kasur' terdeteksi!", icon="⚠️")

        result_array = results[0].plot()
        result_array = cv2.cvtColor(result_array, cv2.COLOR_BGR2RGB)
        result_image = Image.fromarray(result_array)
        st.image(result_image, caption="✅ Detection Result", use_container_width=True)
        os.remove(tmp_path)

    elif "video" in file_type:
        video_path = "temp_uploaded_video.mp4"
        with open(video_path, "wb") as f:
            f.write(uploaded_file.read())

        st.video(video_path)
        st.write("🔍 Running detection on video (CCTV style)...")

        tepi_kasur_detected_once = False
        last_notify_time = 0

        for frame_idx, result in enumerate(model.predict(
            source=video_path,
            conf=0.2,
            iou=0.3,
            stream=True
        )):
            current_time = time.time()
            if check_for_tepi_kasur(result):
                tepi_kasur_detected_once = True
                # hanya munculkan notif jika sudah lewat 5 detik dari notif terakhir
                if current_time - last_notify_time >= 5:
                    st.toast(f"⚠️ 'tepi_kasur' terdeteksi pada frame {frame_idx}!", icon="⚠️")
                    last_notify_time = current_time

        if tepi_kasur_detected_once:
            st.warning("⚠️ 'tepi_kasur' terdeteksi di beberapa frame video ini!")
        else:
            st.success("✅ Tidak ada 'tepi_kasur' terdeteksi pada video ini.")

        # Generate hasil video dengan anotasi
        st.write("🎥 Generating annotated video...")
        results = model.predict(
            source=video_path,
            conf=0.2,
            iou=0.3,
            save=True,
            vid_stride=1,
            project="runs/detect",
            name="baby_video",
            exist_ok=True
        )

        save_dir = results[0].save_dir
        st.write(f"📂 Output folder: `{save_dir}`")

        output_video_path = None
        for file in sorted(os.listdir(save_dir), reverse=True):
            if file.endswith(".avi"):
                output_video_path = os.path.join(save_dir, file)
                break

        if output_video_path and output_video_path.endswith(".avi"):
            mp4_path = output_video_path.replace(".avi", ".mp4")
            ffmpeg_cmd = [
                "ffmpeg", "-y", "-i", output_video_path,
                "-vcodec", "libx264", "-pix_fmt", "yuv420p",
                "-movflags", "+faststart", mp4_path
            ]
            result = subprocess.run(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            if result.returncode != 0:
                st.error("❌ FFmpeg failed to convert video.")
                st.text(result.stderr.decode())
                st.stop()
            output_video_path = mp4_path

        if output_video_path and os.path.exists(output_video_path):
            st.success("✅ Detection complete!")
            st.video(output_video_path)
            with open(output_video_path, "rb") as f:
                st.download_button("📥 Download Result Video", f, file_name="detected_video.mp4")
        else:
            st.error("❌ Processed video not found.")
            st.write("📁 Files in folder:")
            st.write(os.listdir(save_dir))

        os.remove(video_path)
