import sys
import cv2
import pytesseract
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, QFileDialog
from PyQt6.QtCore import Qt

class SubtitleExtractorGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.label = QLabel("字幕抽出ツール")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.select_button = QPushButton("動画を選択")
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)
        
        self.text_area = QTextEdit()
        self.text_area.setPlaceholderText("抽出された字幕がここに表示されます")
        layout.addWidget(self.text_area)
        
        self.extract_button = QPushButton("字幕を抽出")
        self.extract_button.clicked.connect(self.extract_subtitles)
        layout.addWidget(self.extract_button)
        
        self.setLayout(layout)
        self.setWindowTitle("字幕抽出ツール")
        self.setGeometry(100, 100, 500, 400)

    def select_video(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "動画を選択", "", "Video Files (*.mp4 *.avi *.mov)")
        if file_path:
            self.label.setText(f"選択された動画: {file_path}")
            self.video_path = file_path

    def extract_subtitles(self):
        if hasattr(self, 'video_path'):
            self.text_area.setText("字幕の抽出中...\n")
            subtitles = self.ocr_extract_subtitles(self.video_path)
            self.text_area.setText(subtitles if subtitles else "字幕が検出されませんでした。")
        else:
            self.text_area.setText("先に動画を選択してください。")

    def ocr_extract_subtitles(self, video_path):
        cap = cv2.VideoCapture(video_path)
        subtitles = ""
        frame_count = 0

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % 30 == 0:  # 30フレームごとに解析
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                blurred = cv2.GaussianBlur(gray, (5, 5), 0)
                _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY_INV)
                
                contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    if h > 20 and w > 50 and y > frame.shape[0] // 2:  # 下部の字幕を狙う
                        roi = gray[y:y+h, x:x+w]
                        text = pytesseract.image_to_string(roi, lang='eng')
                        if text.strip():
                            subtitles += text + "\n"

            frame_count += 1

        cap.release()
        return subtitles

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SubtitleExtractorGUI()
    window.show()
    sys.exit(app.exec())
