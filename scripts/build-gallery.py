#!/usr/bin/env python3
"""Generate gallery metadata from files; no hand-maintained image list."""
import argparse
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

SUPPORTED = {'.jpg', '.jpeg', '.png', '.webp'}

def scan(folder):
    photos = []
    if not folder.is_dir():
        return {'photos': photos}
    for path in sorted(folder.iterdir(), key=lambda p: p.name.casefold()):
        if path.name.startswith('.') or path.is_symlink() or not path.is_file() or path.suffix.lower() not in SUPPORTED:
            continue
        try:
            digest = hashlib.sha256()
            with path.open('rb') as source:
                for chunk in iter(lambda: source.read(1024 * 1024), b''):
                    digest.update(chunk)
            photos.append({'src': 'gallery/' + quote(path.name, safe=''), 'version': digest.hexdigest()[:16]})
        except FileNotFoundError:
            continue
    return {'photos': photos}

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', type=Path, default=Path(__file__).resolve().parents[1] / 'gallery')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(scan(args.folder), ensure_ascii=False), encoding='utf-8')
