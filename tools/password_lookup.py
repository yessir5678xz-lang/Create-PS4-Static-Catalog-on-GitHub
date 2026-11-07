#!/usr/bin/env python3
"""Local-only archive password lookup for a user's own authorized package catalog."""
from __future__ import annotations
import argparse, copy, json
from pathlib import Path
from typing import Any

def lookup_archive_passwords(package_id: str, password_file: str | Path = "passwords.local.json") -> list[str]:
    path = Path(password_file)
    if not path.exists():
        return []
    data = json.loads(path.read_text(encoding="utf-8"))
    mapping = data.get("packagePasswords", {})
    if not isinstance(mapping, dict):
        raise ValueError("packagePasswords must be a JSON object")
    values = mapping.get(package_id, [])
    if isinstance(values, str):
        values = [values]
    if not isinstance(values, list) or len(values) > 16:
        raise ValueError("Use at most 16 passwords per package ID")
    result = []
    for value in values:
        if not isinstance(value, str) or len(value) > 256 or any(ord(c) < 32 for c in value):
            raise ValueError("Invalid password entry")
        if value and value not in result:
            result.append(value)
    return result

def apply_passwords(catalog: dict[str, Any], password_file: str | Path = "passwords.local.json") -> dict[str, Any]:
    output = copy.deepcopy(catalog)
    for title in output.get("titles", []):
        for package in title.get("packages", []):
            values = lookup_archive_passwords(package.get("id", ""), password_file)
            if values:
                package["archivePasswords"] = values
    return output

def main() -> None:
    parser = argparse.ArgumentParser(description="Merge locally supplied archive passwords into catalog JSON")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--password-file", type=Path, default=Path("passwords.local.json"))
    args = parser.parse_args()
    catalog = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(catalog, dict):
        raise SystemExit("Input catalog must be a JSON object")
    merged = apply_passwords(catalog, args.password_file)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(merged, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("Wrote catalog with local passwords to", args.output)

if __name__ == "__main__":
    main()
