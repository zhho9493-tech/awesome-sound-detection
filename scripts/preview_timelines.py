#!/usr/bin/env python3
"""Serve the repository's interactive paper timelines and open a local viewer."""
from __future__ import annotations

import argparse
import html
import json
import socket
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "resources/category-timeline-manifest.json"


def landing_page() -> bytes:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    cards = []
    for item in manifest["categories"].values():
        cards.append(
            f'''<a class="card" href="/{html.escape(item['path'])}">
                <span class="count">{item['paper_count']} 篇论文</span>
                <strong>{html.escape(item['title'])}</strong>
                <small>打开交互时间线 →</small>
            </a>'''
        )
    body = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>论文时间线本地预览</title>
<style>
:root{{--bg:#f5f7fb;--panel:#fff;--text:#172033;--muted:#68758b;--line:#dce2ed;--accent:#1769dc}}
@media(prefers-color-scheme:dark){{:root{{--bg:#10141d;--panel:#181e29;--text:#edf2ff;--muted:#aeb8ca;--line:#313b4d;--accent:#70aaff}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--text);font:15px/1.6 system-ui,-apple-system,"Segoe UI",sans-serif}}main{{max-width:1100px;margin:auto;padding:56px 24px}}h1{{margin:0;font-size:clamp(30px,5vw,54px);line-height:1.1}}p{{color:var(--muted);max-width:700px}}.grid{{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;margin-top:30px}}.card{{position:relative;display:grid;gap:10px;min-height:150px;padding:22px;background:var(--panel);border:1px solid var(--line);border-radius:18px;color:var(--text);text-decoration:none;transition:.18s transform,.18s border-color}}.card:hover{{transform:translateY(-3px);border-color:var(--accent)}}.card strong{{font-size:20px}}.card small,.count{{color:var(--muted)}}.count{{font-size:12px}}footer{{margin-top:28px;color:var(--muted);font-size:13px}}@media(max-width:760px){{.grid{{grid-template-columns:1fr}}main{{padding:32px 14px}}}}
</style></head><body><main><h1>论文时间线本地预览</h1><p>选择一个研究方向即可直接查看技术演进、支撑论文、中文简述和交互筛选。页面数据完全来自当前本地仓库。</p><section class="grid">{''.join(cards)}</section><footer>关闭启动本预览的终端窗口即可停止本地服务。</footer></main></body></html>'''
    return body.encode("utf-8")


class PreviewHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def do_GET(self):
        path = urlparse(self.path).path
        if path in {"/", "/index.html", "/preview"}:
            content = landing_page()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(content)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(content)
            return
        super().do_GET()

    def log_message(self, fmt, *args):
        print(f"[preview] {self.address_string()} {fmt % args}")


def available_port(host: str, preferred: int) -> int:
    for port in range(preferred, preferred + 20):
        with socket.socket() as probe:
            try:
                probe.bind((host, port))
            except OSError:
                continue
            return port
    raise RuntimeError(f"No free port found in {preferred}-{preferred + 19}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Preview all interactive paper timelines locally")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    if not MANIFEST.exists():
        raise SystemExit("Timeline manifest is missing; run scripts/generate_category_timelines.py first.")
    port = available_port(args.host, args.port)
    server = ThreadingHTTPServer((args.host, port), PreviewHandler)
    url = f"http://{args.host}:{port}/"
    print(f"\n论文时间线本地预览：{url}")
    print("按 Control+C 停止服务。\n")
    if not args.no_browser:
        threading.Timer(0.45, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n本地预览已停止。")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
