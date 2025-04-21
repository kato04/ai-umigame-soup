# config.py (Streamlit Community Cloud向けに修正)

import streamlit as st
import google.generativeai as genai
import os # os はここでは不要になるが、残しても問題ない

# --- APIキー設定 (Streamlit Secretsから取得) ---
# @st.cache_resource # Secretsを使う場合、キャッシュは不要かもしれない（要検証）
# -> Secrets自体がキャッシュされるため、関数キャッシュは不要
def load_api_key():
    """Streamlit SecretsからAPIキーを読み込む"""
    try:
        # st.secrets["キー名"] でアクセス
        api_key = st.secrets["GOOGLE_API_KEY"]
        if not api_key:
            # Secretsには存在するが値が空の場合
            st.error("Streamlit Secretsに GOOGLE_API_KEY はありますが、値が設定されていません。")
            st.stop()
        return api_key
    except KeyError:
        # Secretsに GOOGLE_API_KEY 自体が存在しない場合
        st.error("Streamlit Secretsに GOOGLE_API_KEY が設定されていません。アプリの設定を確認してください。")
        st.stop()
    except Exception as e:
        # その他の予期せぬエラー
        st.error(f"Secretsの読み込み中にエラーが発生しました: {e}")
        st.stop()

# --- Gemini設定 ---
@st.cache_resource # モデルオブジェクトはキャッシュした方が効率が良い
def initialize_gemini():
    """APIキーを設定し、Geminiモデルを初期化して返す"""
    api_key = load_api_key() # 上の関数でAPIキーを取得
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-pro-latest') # モデル指定
        # st.success("Geminiモデル初期化完了！") # デバッグ用
        return model
    except Exception as e:
        st.error(f"Google Generative AIの設定またはモデル読み込み中にエラー: {e}")
        st.stop()

# config.pyが直接実行された場合の動作（変更なし）
if __name__ == '__main__':
    print("設定ファイルを読み込みました。")
