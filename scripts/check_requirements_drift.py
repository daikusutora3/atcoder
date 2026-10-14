#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REQUIREMENTS_DIR = PROJECT_ROOT / "scripts" / "requirements"
OFFICIAL_DIR = REQUIREMENTS_DIR / "official"

TARGETS = ("cp313", "pypy")
ALLOWED_MISSING = {
    "cp313": {"torch"},
    "pypy": {"pandas", "scikit-learn", "scipy", "shapely", "z3-solver"},
}

REQ_PATTERN = re.compile(r"^\s*([A-Za-z0-9_.-]+)\s*(==|@)\s*(.+?)\s*$")


def parse_requirements(path: Path) -> dict[str, str]:
    packages: dict[str, str] = {}
    for raw_line in path.read_text().splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        match = REQ_PATTERN.match(line)
        if not match:
            raise ValueError(f"unsupported requirement format in {path}: {raw_line}")
        name, operator, spec = match.groups()
        packages[name] = f"{operator}{spec}"
    return packages


def report_group(header: str, packages: list[str], official: dict[str, str]) -> None:
    if not packages:
        return
    print(f"  {header}")
    for name in packages:
        print(f"    - {name}{official.get(name, '')}")


def main() -> int:
    failed = False
    for target in TARGETS:
        official = parse_requirements(OFFICIAL_DIR / f"{target}.txt")
        local = parse_requirements(REQUIREMENTS_DIR / f"{target}.txt")

        missing = sorted(name for name in official if name not in local)
        extra = sorted(name for name in local if name not in official)
        mismatched = sorted(
            name
            for name in official
            if name in local and official[name] != local[name]
        )

        allowed_missing = ALLOWED_MISSING.get(target, set())
        unexpected_missing = [name for name in missing if name not in allowed_missing]
        tolerated_missing = [name for name in missing if name in allowed_missing]

        print(f"[{target}]")
        if not unexpected_missing and not extra and not mismatched:
            if tolerated_missing:
                print("  OK with intentional omissions")
                for name in tolerated_missing:
                    print(f"    - {name}{official[name]}")
            else:
                print("  OK")
            continue

        if tolerated_missing:
            print("  Intentional omissions")
            for name in tolerated_missing:
                print(f"    - {name}{official[name]}")

        report_group("Unexpected missing", unexpected_missing, official)
        if extra:
            print("  Unexpected extra")
            for name in extra:
                print(f"    - {name}{local[name]}")
        if mismatched:
            print("  Version drift")
            for name in mismatched:
                print(f"    - {name}: local {local[name]} / official {official[name]}")
        failed = True

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
