# Subtitle Translator GUI

このプロジェクトは、動画に埋め込まれた英語字幕を自動で抽出し、日本語に翻訳するツールです。
PyQtを用いたGUIベースのアプリケーションで、DeepL APIを利用して翻訳を行います。

## 🔧 インストール方法

### 1. 必要なライブラリをインストール
まず、Python仮想環境を作成し、必要なライブラリをインストールします。

```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

pip install -r requirements.txt
```

### 2. `config.json` に DeepL API キーを設定
DeepL の API キーを取得し、`config.json` を作成して以下のように記述してください。

```json
{
  "DEEPL_API_KEY": "your_deepl_api_key_here"
}
```

### 3. アプリを実行
```bash
python main.py
```

## 📌 機能一覧
✅ 動画の字幕を OCR で抽出  
✅ DeepL API で字幕を翻訳  
✅ GUI で簡単に操作可能  

## ⚡ 使用技術
- Python
- OpenCV
- PyQt
- pytesseract
- DeepL API

## 📝 ライセンス
このプロジェクトは MIT ライセンスのもとで提供されます。

