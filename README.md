# AtCoder

AtCoder の Python 解答と、再利用する競技プログラミング用ライブラリを管理するリポジトリです。

## 目的から探す

| やりたいこと | 入口 |
| --- | --- |
| 問題の解答を見る | [src/](src/) — コンテスト・分類ごとの Python 解答 |
| アルゴリズムを再利用する | [ライブラリ目次](library/README.md) — 用途別のコードと使用例 |
| 実行環境を作る・解答を検証する | [スクリプトの使い方](scripts/README.md) — セットアップとランダムテスト |

## 構成

| パス | 内容 |
| --- | --- |
| [src/](src/) | `abc`・`arc` などのコンテスト別、アルゴリズムなどの分類別の解答 |
| [library/](library/README.md) | 再利用する実装、同名 Markdown の説明、カテゴリ別の索引 |
| [scripts/](scripts/README.md) | 環境構築・依存差分確認・ランダムテスト |
| [.vscode/](.vscode/) | ランダムテスト用のタスク・デバッグ設定 |
| [.agents/skills/](.agents/skills/) | このリポジトリで使用するスキル |
| [skills-lock.json](skills-lock.json) | 外部スキルの入手元と内容のハッシュ |

## セットアップ

```bash
scripts/setup_envs.sh
```

AtCoder 2025/10 公開の Python ランタイム（CPython / PyPy）用仮想環境を構築します。必要なツール、実行環境、ランダムテストの手順は [scripts/README.md](scripts/README.md) を参照してください。

requirements の公式差分を確認するには:

```bash
python3 scripts/check_requirements_drift.py
```

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
