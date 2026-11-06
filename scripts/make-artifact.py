#!/usr/bin/env python3
"""index.html から claude.ai Artifact 用の断片を切り出す。

Artifact は公開時に <!doctype>/<html>/<head>/<body> の骨組みを自動で付けるため、
index.html のマーカー（ARTIFACT-HEAD-* / ARTIFACT-BODY-*）で囲んだ部分だけを
1 ファイルにまとめて出力する。index.html 自体はそのままブラウザで開ける完全な文書。

使い方: python3 scripts/make-artifact.py [index.html] [dist/kart-rush.html]
"""
import pathlib
import re
import sys

src_path = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "index.html")
out_path = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else "dist/kart-rush.html")
src = src_path.read_text(encoding="utf-8")


def part(name: str) -> str:
    m = re.search(rf"<!--ARTIFACT-{name}-START-->(.*?)<!--ARTIFACT-{name}-END-->", src, re.S)
    if not m:
        sys.exit(f"marker ARTIFACT-{name}-START/END not found in {src_path}")
    return m.group(1).strip()


out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(part("HEAD") + "\n" + part("BODY") + "\n", encoding="utf-8")
print(f"wrote {out_path} ({out_path.stat().st_size // 1024} KB)")
