# %%writefile problems.py
# ↑ Colabセルでこのファイルを作成するためのマジックコマンド

# 問題データのリスト
PROBLEMS = [
    # --- 既存の問題 (context改善済み) ---
    {
        "id": "turtle_soup",
        "title": "ウミガメのスープ（難易度：★★★）", # タイトルに難易度を追加
        "question": """
        ある男が、とある海の見えるレストランで「ウミガメのスープ」を注文した。
        スープを一口飲んだ男は、それが本物の「ウミガメのスープ」であることを確認し、
        勘定を済ませて帰宅した後、自殺した。一体、なぜ？
        """,
        "context": """
        あなたは「ウミガメのスープ」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（なぜ男が自殺したか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        男はかつて数人の仲間と海で遭難し、とある島に漂着した。食料はなく、仲間たちは生き延びるために力尽きて死んだ者の肉を食べ始めたが、男はかたくなに拒否していた。見かねた仲間の一人が、「これはウミガメのスープだから」と嘘をつき、男に人肉のスープを飲ませ、救助が来るまで生き延びさせた。男はレストランで飲んだ「本物のウミガメのスープ」とかつて自分が飲んだスープの味が違うことから真相を悟り（＝仲間が作ってくれたスープが人肉であったこと）、絶望のあまり自ら命を絶った。
        """,
        "answer": """
        男はかつて数人の仲間と海で遭難し、とある島に漂着した。食料はなく、仲間たちは生き延びるために力尽きて死んだ者の肉を食べ始めたが、男はかたくなに拒否していた。見かねた仲間の一人が、「これはウミガメのスープだから」と嘘をつき、男に人肉のスープを飲ませ、救助が来るまで生き延びさせた。男はレストランで飲んだ「本物のウミガメのスープ」とかつて自分が飲んだスープの味が違うことから真相を悟り、絶望のあまり自ら命を絶った。
        """
    },
    {
        "id": "manhole",
        "title": "マンホール（難易度：★★★）", # タイトルに難易度を追加
        "question": """
        男は雨の中、マンホールの蓋が開いているのを見たが、特に気にせず通り過ぎた。
        しばらくして、男は自分が大変な失敗を犯したことに気づき、後悔した。一体、なぜ？
        """,
        "context": """
        あなたは「マンホール」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（なぜ男が後悔したか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        男は小説家で、雨の中を散歩中に開いたマンホールを見た。彼はそれを面白い光景だと思ったが、気にせず家に帰った。その後、執筆中の小説の重要なトリックとして「開いたマンホール」を使うことを思いついたが、散歩中に具体的な場所や周囲の状況を全く覚えていなかったため、小説に使えず後悔した（＝これが大変な失敗）。
        """,
        "answer": """
        男は小説家。散歩中に開いたマンホールを見て面白いと思ったが、詳細を確認せずに通り過ぎた。後で小説のトリックに使おうとしたが、場所や状況を覚えていなかったため、ネタにできず後悔した。
        """
    },
    {
        "id": "elevator",
        "title": "エレベーター（難易度：★★★）", # タイトルに難易度を追加
        "question": """
        ある男はマンションの10階に住んでいる。毎朝、エレベーターで1階に降りて会社へ行く。しかし、会社から帰ってくるときは、雨が降っている日か、他に誰かがエレベーターに乗っている日だけ10階まで行く。それ以外の日（晴れていて誰も乗っていない日）は、必ず7階でエレベーターを降り、そこから階段で10階まで歩いて登る。一体、なぜ？
        """,
        "context": """
        あなたは「エレベーター」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（なぜ男が特定の条件下で7階で降りるのか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        その男は非常に背が低い（例えば小人症など）。エレベーターのボタンに手が届かない。降りるときは「1階（またはG階）」のボタンには手が届くので問題ない。しかし、昇るときは自力では「7階」のボタンまでしか手が届かない。雨が降っている日は傘を持っているので、傘の柄を使って「10階」のボタンを押すことができる。他に誰かが乗っていれば、その人に頼んで「10階」のボタンを押してもらえる。晴れていて誰も乗っていない日は、自力で押せる「7階」までしか行けず、残りは階段を使うしかない。
        """,
        "answer": """
        男は背がとても低く、エレベーターの「10階」のボタンに手が届かない。自力で届くのは「7階」のボタンまで。雨の日は持っている傘で、他に人がいればその人に頼んで「10階」を押してもらえるが、晴れていて一人のときは7階までしか行けないため、残りを歩いて登る。
        """
    },
    # --- ↓↓↓ 新しく追加する問題 ↓↓↓ ---
    {
        "id": "bank_robber",
        "title": "銀行に来た男（難易度：★☆☆）",
        "question": """
        ある男が銀行の前に車を停め、銀行の中に走りこんだ。男は25人を動けなくし、200ドルを持って銀行を飛び出した。
        一部始終を見ていた警官が男を呼び止め、「そんなことをしてはいかん」と叱咤したが、警官はすぐに男を解放した。なぜだろう？
        """,
        "context": """
        あなたは「銀行に来た男」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（なぜ男は警官に解放されたのか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        男は銀行で現金200ドルをおろすために、銀行の前に車を一時的に停めた。銀行内での用事を済ませて車に戻ると、彼の駐車が原因で交通渋滞が発生しており、後続の車（約25台、運転手含む）が動けなくなっていた。それを見ていた警官が男を呼び止め、不適切な駐車について叱咤したが、悪質な違反ではなかったため、逮捕はせずに口頭注意で解放した。男が「25人を動けなくし、200ドルを持って銀行を飛び出した」というのは、言葉のトリックであり、事実は「（駐車によって）25人（のドライバー）を動けなくし、（ATMでおろした）200ドルを持って銀行を（普通に）出た」ということである。（＝これが解放された理由）
        """,
        "answer": """
        男は200ドルをおろすために銀行の前に駐車した。そのせいで渋滞になり、後ろの25人のドライバー達を動けなくしてしまった。警官は駐車違反について叱ったが、逮捕はせずに解放した。
        """
    },
    {
        "id": "goldfish",
        "title": "アントニーとクレオパトラ（難易度：★☆☆）",
        "question": """
        アントニーとクレオパトラが、エジプトの屋敷の床で息絶えていた。屍のそばには、割れた金魚鉢。彼らの体に傷はなく、毒を飲んだ形跡もない。死亡時、屋敷には誰も居なかった。アントニーとクレオパトラはどうやって死んだのだろうか？
        """,
        "context": """
        あなたは「アントニーとクレオパトラ」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（どうやって死んだのか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        「アントニー」と「クレオパトラ」というのは、人間の名前ではなく、その屋敷で飼われていた二匹の金魚の名前だった。何らかのアクシデント（例えば、猫が倒した、地震で落ちたなど）で金魚鉢が床に落ちて割れてしまい、水が無くなった。水から出された金魚であるアントニーとクレオパトラは、床の上で窒息死してしまった。（＝これが彼らの死因）
        """,
        "answer": """
        アントニーとクレオパトラは、その家で飼われていた金魚の名前だった。何らかの事故で金魚鉢が割れて水がなくなり、床の上で死んでしまった。
        """
    },
    {
        "id": "sandwich_shop",
        "title": "理想のタマゴサンド（難易度：★★☆）",
        "question": """
        タマゴサンドは、タクロウさんの大好物。中でも一番好きなタマゴサンドを出すパン屋へ向かったタクロウさんは、売り切れの札を見て喜んでいる。一体、なぜ？
        """,
        "context": """
        あなたは「理想のタマゴサンド」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（なぜタクロウさんは喜んでいるのか）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        タクロウさんはパン屋の客ではなく、そのパン屋の店主だった。彼が作るタマゴサンドは非常に人気があり、毎日すぐに売り切れてしまう。彼が店に向かった時、「売り切れ」の札が出ていたということは、その日も自分の作ったタマゴサンドが大好評で完売したことを意味する。自分の店の繁盛ぶりを見て喜んでいるのだ。（＝これが喜んでいる理由）
        """,
        "answer": """
        タクロウさんは、そのパン屋の店主だった。彼が作る大好物のタマゴサンドが、その日も大人気で売り切れたことを喜んでいるのだ。
        """
    },
    {
        "id": "parachute",
        "title": "野原の死体（難易度：★★☆）",
        "question": """
        ある男が、野原で死んでいた。死体の隣には、開かれていない包みがあった。この男の死因とは？
        """,
        "context": """
        あなたは「野原の死体」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（男の死因は何か）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        男はスカイダイビングをしていた。死体の隣にあった「開かれていない包み」とは、開くはずだったパラシュートのことである。飛行機から飛び降りた後、何らかの理由でパラシュートが開かず、そのまま地面に激突して死亡した。（＝これが死因）
        """,
        "answer": """
        男はスカイダイビングをしており、隣にあった「開かれていない包み」は開かなかったパラシュートだった。パラシュートが開かずに地面に落下したことが死因である。
        """
    },
    {
        "id": "basement",
        "title": "地下室の扉（難易度：★★★）",
        "question": """
        小さな女の子が両親に「決して地下室の扉を開けてはいけない、開けたら見てはいけないものを目にする」と注意されていた。しかしある日、両親が出かけている間に女の子は地下室の扉を開けてしまった。果たして、女の子が見てはいけなかったものとは何だろうか？
        """,
        "context": """
        あなたは「地下室の扉」という水平思考クイズの出題者です。以下のストーリーに基づいて、ユーザーからの質問に回答してください。回答は「はい」「いいえ」「関係ありません」のいずれかのみとし、余計な説明は絶対に含めないでください。

        重要なルール：
        - ユーザーの質問内容が、提示されたストーリーの**真相（女の子が見てはいけなかったものとは何か）を理解する上で核心的かつ直接的に重要**な場合は「はい」と答えます。
        - 質問内容がストーリーの事実と**明確に矛盾する**場合は「いいえ」と答えます。
        - 質問内容がストーリーの内容と矛盾はしないものの、**真相の核心とは直接関係がない**場合は「関係ありません」と答えます。

        ストーリー：
        女の子はずっと地下室に閉じ込められて育てられていた。彼女にとって「地下室」が世界の全てであり、地下室から外へ出る「扉」を開けることは固く禁じられていた。両親の外出中に初めてその扉を開けた女の子が目にした「見てはいけなかったもの」とは、地下室の外に広がる「外の世界（＝普通の家の中や庭、空など）」そのものだった。両親にとっては、娘に外の世界を見せること自体が禁忌だったのである。（＝これが女の子が見てはいけなかったもの）
        """,
        "answer": """
        女の子が見てはいけなかったのは「外の世界」そのもの。女の子は生まれてからずっと地下室に閉じ込められており、両親は彼女が外の世界を見ることを禁じていた。彼女が開けたのは地下室から外へ出る扉だった。
        """
    }
]