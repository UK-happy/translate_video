# 字幕翻訳ツール

## 概要
このツールは、PyQtを使用して開発されたGUIアプリケーションで、動画から埋め込まれた字幕を抽出し、自動翻訳する機能を提供します。

## 主な機能
- **動画の選択**: ユーザーが動画ファイルを選択
- **字幕の抽出**: OCR（光学文字認識）を用いて動画の字幕を検出
- **翻訳機能**: DeepL API を使用して英語の字幕を日本語に翻訳
- **プレビュー機能**: 抽出・翻訳された字幕をGUI上で確認可能

## 動作環境
- Python 3.x
- PyQt6
- OpenCV
- pytesseract
- requests
- dotenv（APIキー管理用）

## インストール
1. 必要なライブラリをインストール
   ```sh
   pip install PyQt6 opencv-python pytesseract requests python-dotenv

2. .env ファイルを作成し、DeepL APIキーを設定
   ```plaintext
   DEEPL_API_KEY=your_deepl_api_key_here

## 使い方
1. アプリを起動
   ```sh
   python main.py

2. 「動画を選択」ボタンで動画ファイルを選ぶ
3. 「字幕を抽出」ボタンを押して字幕を取得
4. 「翻訳」ボタンを押して日本語に翻訳

## 注意事項
- DeepLの無料APIキーには使用回数制限があります。
- OCR精度は動画の品質や字幕のフォントによって変動します。

## ライセンス 
このプロジェクトはMITライセンスのもとで提供されます。



