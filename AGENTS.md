# kart-race プロジェクト指示

共通方針は `../../AGENTS.md`（workspace/AGENTS.md）に従う。このリポジトリは独立した Git リポジトリなので、作業開始時にその共通方針とこのファイル、README.md を読む。

## このプロジェクトの前提

- 成果物は `index.html` 1 ファイル。ビルド工程も npm もない。外部依存は cdnjs の Three.js（バージョン固定の UMD ビルド）だけ。
- 配布先は claude.ai の Artifact。`scripts/make-artifact.py` でマーカー内を切り出した `dist/kart-rush.html` を公開する（dist/ はコミットしない）。
- 検証はブラウザで行う。コンソールの `KR.dbg.auto = true` で AI がプレイヤーを運転し、3 周→結果画面まで自動で通せる。
- 傾き操作（DeviceOrientation）は実機の iPhone でしか確認できない。変更したら README の「確認済み環境」を更新する。
- 設計の判断理由は README の「設計メモ」に置く。計画・教訓は workspace の tasks/ に記録する。
