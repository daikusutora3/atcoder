# scripts ディレクトリの説明

## setup_envs.sh

AtCoder 2025/10 公開の Python ランタイム（CPython 3.13.7 / PyPy 3.11-v7.3.20）をローカルで再現する自動セットアップスクリプトです。必要に応じて `pyenv` を `.pyenv/` にクローンし、各インタプリタのインストールから仮想環境構築までをまとめて実行します。macOS でも完走するよう、Linux 専用ホイールが必要なライブラリは `scripts/requirements/` から除外済みです。各環境の依存導入後には `from atcoder.segtree import SegTree` を実行し、ACL が実際に import できるところまで検証します。

### 前提
- `uv` / `git` / `curl` が利用可能であること
- `PYENV_ROOT` を指定しない場合はリポジトリ直下に `.pyenv/` が作成されます（既存の pyenv を利用する場合は事前に `PYENV_ROOT` を切り替えてください）。

### 実行例
```bash
scripts/setup_envs.sh
```

完了後は `.cp313` / `.pypy` が作成され、それぞれ `scripts/requirements/` 内のパッケージがインストール済みになります。`CPython` では `numba 0.61.2` を CUDA 無効化した状態で導入します（`atcoder-cli` は npm パッケージのため対象外）。PyPy には AtCoder 公式環境に合わせて `ac-library-python` と `acl-cpp-python` の両方を入れます。

### ドリフト検査
```bash
python3 scripts/check_requirements_drift.py
```

AtCoder 公式の 2025/10 言語一覧を `scripts/requirements/official/` に写し、ローカルの `scripts/requirements/*.txt` との差分を検査します。現在は `torch`（CPython）と、macOS で除外している `pandas` / `scikit-learn` / `scipy` / `shapely` / `z3-solver`（PyPy）のみを意図的な差分として許容します。

### 他のスクリプト
- `install_patched_numba.sh`  
  AtCoder 公式の CUDA 無効化手順を再現し、`numba==0.61.2` をソースからインストールします。`setup_envs.sh` 内で自動実行されますが、必要であれば個別に呼び出すことも可能です。

## ランテス

`scripts/rantest.py` は、提出用の解答・ランダム入力生成器・愚直解を標準入出力でつないで比較するためのスクリプトです。提出用ファイルを import しないため、`input()` / `print()` 直書きの解答にも使えます。

例として `src/abc999/c.py` を検証する場合は、同じディレクトリに次の 2 ファイルを置きます。

```text
src/abc999/c.py
src/abc999/c_gen.py
src/abc999/c_oracle.py
```

`c_gen.py` は seed を第 1 引数で受け取り、1 ケース分の入力を標準出力へ出します。`c_oracle.py` は `c.py` と同じ入力を標準入力から読み、愚直解の答えを標準出力へ出します。

コマンドで実行する場合:

```bash
python3 scripts/rantest.py src/abc999/c.py --auto --cases 1000 --seed 0 --timeout 2 --require-contest-quiet
```

VSCode では `src/abc999/c.py` を開いた状態で、Run and Debug から `Rantest current file (100 cases)` または `Rantest current file (1000 cases)` を選ぶと実行できます。Task として実行する場合は `AtCoder: rantest current file (100 cases)` を選びます。

`--require-contest-quiet` を付けると、AtCoder の開催状況を確認できない場合やコンテスト中・開始直前・終了直後の場合に停止します。AI が関わる作業ではこの確認を外さないでください。
