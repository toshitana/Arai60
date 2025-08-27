# How to work on each step
Step 1: 答えを見ずに 5 分以内に解く。わからなかったら答えを見て、開始から答えを見ないで 5 分以内に正解になるところまで行う。 
Step 2: 本協会メンバーや LeetCode の過去解答を参考にしつつ、コードを見やすくする形で整える。 
Step 3: 全部消して、10 分以内にエラーを一度も出さずに正解するのを 3 回続けて行う。 
Step 4: いただいたレビューをもとに、コードを整える。

# Comments
## Step 1
方針として、新しいListNode、unique_sorted_linked_listを作成して、head.val==head.next.valと同じだったらパス、head.val != head.next.valだったらunique_sorted_linked_list.nextに追加する

## Step 2
そういえば、==の仕様で、nodeとnode.nextを比較しても当然同じになるなと気がつき、node.valを比較する部分を実装した。
あと、ListNodeで提出しなければいけないオブジェクトは、新しく作ったListNodeオブジェクトの一番最初だと気がついた。

## Step 3
nodeの定義をheadにしてしまった。nodeはunique_headの次のnodeを探すためのものなので、初期定義はunique_headである。
これは、思うにnodeという名前よくないために起こったのではないか。unique_nodeに名前を変えてもう一度やる

## Step 3-1
そういえば、unique_sorted_linked_listもunique_headに変更した。最初のノードという意味のheadでもあり、受け取ったheadという変数をuniqueにしているという意味でも過不足ない内容ではないかと考えての変更。

あと、勝手にStep4を自分のミスの修正に利用していたので、そういった修正点は3-1などの番号を振って対応する。