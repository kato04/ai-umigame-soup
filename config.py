# %%writefile config.py
# ↑ Colabセルでこのファイルを作成するためのマジックコマンド

import streamlit as st
import google.generativeai as genai
import os

# --- APIキー設定 (一時ファイルから取得) ---
@st.cache_resource # 結果をキャッシュして毎回ファイル読み込みしないようにする
def load_api_key():
    """一時ファイルからAPIキーを読み込む"""
    api_key = None
    api_key_file_path = "/content/api_key.txt"
    try:
        if os.path.exists(api_key_file_path):
            with open(api_key_file_path, "r") as f:
                api_key = f.read().strip()
            # セキュリティのため、一度読み込んだら削除するオプション
            # try:
            #     os.remove(api_key_file_path)
            # except OSError as e:
            #     print(f"Warning: Could not remove API key file: {e}")
        else:
            st.error(f"APIキーファイル ({api_key_file_path}) が見つかりません。")
            st.stop()
    except Exception as e:
        st.error(f"APIキーファイル ({api_key_file_path}) の読み込み中にエラー: {e}")
        st.stop()

    if not api_key:
        st.error(f"APIキーをファイル ({api_key_file_path}) から読み込めませんでした。")
        st.stop()
    return api_key

# --- Gemini設定 ---
@st.cache_resource # モデルオブジェクトもキャッシュする
def initialize_gemini():
    """APIキーを設定し、Geminiモデルを初期化して返す"""
    api_key = load_api_key() # 上の関数でAPIキーを取得
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash') # または他のモデル
        return model
    except Exception as e:
        st.error(f"Google Generative AIの設定またはモデル読み込み中にエラー: {e}")
        st.stop()

# config.pyが直接実行された場合（通常はない）の動作（任意）
if __name__ == '__main__':
    print("設定ファイルを読み込みました。")
    # 簡単なテストなど
    # test_model = initialize_gemini()
    # print(f"Geminiモデルの初期化テスト: {test_model is not None}")