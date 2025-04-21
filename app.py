# %%writefile app.py
# ↑ Colabセルでこのファイルを作成するためのマジックコマンド

import streamlit as st
# --- ↓↓↓ st.set_page_config を最初に持ってくる ↓↓↓ ---
st.set_page_config(page_title="AIウミガメのスープ", layout="centered")
# --- ↑↑↑ st.set_page_config を最初に持ってくる ↑↑↑ ---

# --- その他のインポート ---
from problems import PROBLEMS
from config import initialize_gemini
import os # os は app.py では直接使わなくなったが、念のため残しても良い

# --- Geminiモデルの初期化 ---
# initialize_gemini はこの後で呼び出す。
# もし initialize_gemini 内で st.error が発生しても、
# set_page_config は既に呼ばれているのでエラーにならない。
model = initialize_gemini()
# --- Geminiモデル設定ここまで ---


# --- Streamlit アプリ UI設定 ---
# st.set_page_config(...) は既に上で呼び出したので、ここでは不要

st.title("🐢 AIウミガメのスープ 🍲")
st.write("AI相手に質問して、下の謎を解き明かそう！")

# --- 問題選択機能 (st.selectbox を使用) ---
# session_state に選択中の問題IDがなければ初期化
if 'current_problem_id' not in st.session_state:
    st.session_state.current_problem_id = PROBLEMS[0]['id']

# 問題選択が変更されたときの処理（コールバック関数）
def handle_problem_change():
    selected_title = st.session_state.problem_selector # selectbox の値を取得
    new_problem_id = next((p['id'] for p in PROBLEMS if p['title'] == selected_title), None)
    if new_problem_id and st.session_state.current_problem_id != new_problem_id:
        st.session_state.current_problem_id = new_problem_id
        # 問題が変わったら会話履歴をリセット
        if 'chat_history' in st.session_state:
            st.session_state.chat_history = []
        # フォーム入力もリセットしたい場合（通常 st.form の clear_on_submit で十分）
        # if "user_input_in_form" in st.session_state:
        #    st.session_state.user_input_in_form = ""

# 現在選択中の問題データを取得
current_problem = next((p for p in PROBLEMS if p['id'] == st.session_state.current_problem_id), PROBLEMS[0])

# 問題選択用の Selectbox (プルダウン) を表示
problem_titles = [p['title'] for p in PROBLEMS]
try:
    # 現在選択中の問題がリストにあればそのインデックスを使う
    current_index = problem_titles.index(current_problem['title'])
except ValueError:
    # もし何らかの理由で現在のタイトルがリストにない場合（通常は起こらないはず）、先頭を選ぶ
    current_index = 0
    st.session_state.current_problem_id = PROBLEMS[0]['id']
    current_problem = PROBLEMS[0]


# ★★★ ここで st.selectbox を使用 ★★★
st.selectbox(
    label="問題を選択してください:",
    options=problem_titles,
    index=current_index,
    key="problem_selector",      # Selectboxの状態を管理するキー
    on_change=handle_problem_change # 値が変わったらコールバック実行
)
st.markdown("---")
# --- 問題選択機能ここまで ---


# --- 現在の問題を表示 ---
st.subheader("問題")
st.markdown(current_problem['question'])
st.markdown("---")
# --- 問題表示ここまで ---

# --- 会話履歴の表示 (シンプル表示) ---
st.subheader("会話履歴")
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

if not st.session_state.chat_history:
    st.write("まだ質問がありません。")
else:
    for chat in st.session_state.chat_history:
        role = chat.get("role", "unknown")
        content = chat.get("content", "")
        with st.chat_message(role, avatar="🤔" if role == "user" else "🤖" if role == "ai" else "⚙️"):
             st.markdown(content)
# --- 会話履歴表示ここまで ---


# --- 入力フォーム (st.form を使用) ---
st.markdown("---")
with st.form(key="chat_input_form", clear_on_submit=True):
    user_question = st.text_input("質問を入力してください:", key="user_input_in_form", value="")
    submitted = st.form_submit_button("質問する")

    if submitted and user_question:
        try:
            prompt = f"{current_problem['context']}\n\nユーザーの質問: {user_question}"
            # config.py で初期化済みの model を使う
            response = model.generate_content(prompt)
            ai_answer = response.text.strip()

            valid_answers = ["はい", "いいえ", "関係ありません"]
            if ai_answer not in valid_answers:
                print(f"予期しないAI応答: {ai_answer}")
                ai_answer = "関係ありません"

            st.session_state.chat_history.append({"role": "user", "content": user_question})
            st.session_state.chat_history.append({"role": "ai", "content": ai_answer})
            st.rerun()

        except Exception as e:
            st.error(f"AIへの質問中にエラーが発生しました: {e}")
            st.session_state.chat_history.append({"role": "user", "content": user_question})
            st.session_state.chat_history.append({"role": "system", "content": f"エラー発生: {e}"})
            st.rerun()

    elif submitted and not user_question:
        st.warning("質問を入力してください。")
# --- 入力フォームここまで ---


# --- 答えを見る ---
st.markdown("---")
with st.expander("答えを見る"):
    st.markdown(current_problem['answer'])
    st.success("これが物語の真相です！")
# --- 答えを見る ここまで ---

# --- サイドバー説明 ---
st.sidebar.title("遊び方")
st.sidebar.info("""
1.  ドロップダウンリストから問題を選択します。
2.  下のテキストボックスにAIへの質問を入力します（例：「男は一人でしたか？」）。
3.  「質問する」ボタンを押します。
4.  AIが「はい」「いいえ」「関係ありません」で答えます。
5.  会話履歴をヒントに、問題の真相を推理してください。
6.  分かったと思ったら、またはギブアップの場合は「答えを見る」をクリックしてください。
""")
# --- サイドバー説明 ここまで ---