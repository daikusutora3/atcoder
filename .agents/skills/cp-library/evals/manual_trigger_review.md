# cp-library trigger review

## Context

- この環境では `claude -p` ベースの trigger 評価ループを使わず、Codex による手動レビューで description を改善した。
- 評価用クエリは `evals/trigger_evals.json` に保存してある。

## Review focus

主に次を拾えるかを見た。

- 「〇〇のライブラリを作りたい」
- 「ライブラリ化したい」
- 「再利用できる形に切り出したい」
- 「`library/` に置きたい」
- 「README や md も含めて整えたい」

逆に、次では起動しすぎないようにした。

- `src/...` だけ触る 1 問解答
- ライブラリ化不要の単発バグ修正
- 説明だけの依頼

## Issues found in the previous description

- `library/` の利用や追加は書いていたが、「ライブラリを作りたい」という直接的な言い回しが弱かった。
- `ライブラリ化`、`切り出したい`、`雛形を置きたい` のような自然な依頼文が description に十分入っていなかった。
- どこまでが非対象かが弱く、`src/...` だけの単発作業にも広がりうる書き方だった。

## Changes made

- `「〇〇のライブラリを作りたい」` を description に直接追加した。
- `ライブラリ化したい`、`再利用できる形に切り出したい`、`library/ に雛形や実装を置きたい` を trigger 語として追加した。
- `1 問だけを解く src/... の編集`、`ライブラリ化不要のバグ修正`、`説明だけの依頼` は基本対象外と明記した。

## Expected outcome

- `evals/trigger_evals.json` の positive 群には以前より強く反応しやすくなる。
- negative 群のうち、単発解答・単発修正・説明依頼への誤起動は減る想定。
