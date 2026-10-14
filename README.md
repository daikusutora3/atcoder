# AtCoder

AtCoder の Python 解答と、再利用する競技プログラミング用ライブラリを管理するリポジトリです。

## 構成

- `src/`: コンテスト・分類ごとの解答
- `library/`: 競プロ用ライブラリと使用方法（[目次](library/README.md)）
- `scripts/`: 環境構築・ランダムテスト用スクリプト（[使い方](scripts/README.md)）
- `.vscode/`: ランダムテスト用のタスク・デバッグ設定
- `.agents/skills/`: このリポジトリで使用するスキル
- `skills-lock.json`: 外部スキルの入手元と内容のハッシュ

## セットアップ

```bash
scripts/setup_envs.sh
```

`scripts/setup_envs.sh` を 1 回実行すると AtCoder 2025/10 公開の Python ランタイム（CPython / PyPy）用仮想環境を構築できます。requirements の公式差分確認には `python3 scripts/check_requirements_drift.py` を使います。

仮想環境・キャッシュ・個人用設定・ルートの作業用ファイルは `.gitignore` で管理対象から除外しています。

## GitHub への更新

```bash
git add .
git commit -m "Add solutions"
git push
```

AI を使った作業は、AtCoder のコンテスト開催中を避けてください。詳細は [AGENTS.md](AGENTS.md) を参照してください。

## ライセンス

[MIT License](LICENSE) のもとで、利用・改変・再配布・商用利用ができます。再配布時は著作権表示とライセンス文を残してください。ソフトウェアは無保証で提供します。

外部から導入した `.agents/skills/skill-creator/` は [anthropics/skills](https://github.com/anthropics/skills) に由来し、同ディレクトリの [Apache License 2.0](.agents/skills/skill-creator/LICENSE.txt) が適用されます。
