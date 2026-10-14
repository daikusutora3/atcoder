#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timedelta, timezone
from html.parser import HTMLParser
from urllib.error import URLError
from urllib.request import Request, urlopen


CONTESTS_URL = "https://atcoder.jp/contests/"
JST = timezone(timedelta(hours=9))


class TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if text:
            self.parts.append(text)


def parse_duration(text: str) -> timedelta:
    hours, minutes = map(int, text.split(":"))
    return timedelta(hours=hours, minutes=minutes)


def load_contests_page(timeout: float) -> str:
    request = Request(CONTESTS_URL, headers={"User-Agent": "atcoder-local-rantest/1.0"})
    with urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", errors="replace")


def extract_contests(html: str) -> list[tuple[datetime, timedelta, str]]:
    parser = TextExtractor()
    parser.feed(html)
    tokens = parser.parts

    contests: list[tuple[datetime, timedelta, str]] = []
    time_re = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[+-]\d{4}$")
    duration_re = re.compile(r"^\d{2,3}:\d{2}$")

    for i, token in enumerate(tokens):
        if not time_re.match(token):
            continue
        try:
            start = datetime.strptime(token, "%Y-%m-%d %H:%M:%S%z")
        except ValueError:
            continue

        name = "(unknown contest)"
        duration: timedelta | None = None
        for candidate in tokens[i + 1 : i + 16]:
            if duration_re.match(candidate):
                duration = parse_duration(candidate)
                break
            if candidate not in {"Ⓐ◉", "Ⓗ◉", "-", "All"} and name == "(unknown contest)":
                name = candidate

        if duration is not None:
            contests.append((start, duration, name))

    return contests


def active_contests(
    contests: list[tuple[datetime, timedelta, str]],
    now: datetime,
    pre_buffer: timedelta,
    post_buffer: timedelta,
) -> list[tuple[datetime, datetime, str]]:
    active: list[tuple[datetime, datetime, str]] = []
    for start, duration, name in contests:
        guarded_start = start - pre_buffer
        guarded_end = start + duration + post_buffer
        if guarded_start <= now < guarded_end:
            active.append((start, start + duration, name))
    return active


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fail if an AtCoder contest appears to be active now."
    )
    parser.add_argument("--timeout", type=float, default=8.0)
    parser.add_argument("--pre-buffer-minutes", type=int, default=15)
    parser.add_argument("--post-buffer-minutes", type=int, default=10)
    args = parser.parse_args()

    now = datetime.now(JST)
    try:
        html = load_contests_page(args.timeout)
        contests = extract_contests(html)
    except (OSError, URLError) as exc:
        print(
            "Could not confirm AtCoder contest status. Stopping safely.",
            file=sys.stderr,
        )
        print(f"reason: {exc}", file=sys.stderr)
        return 1

    running = active_contests(
        contests,
        now,
        timedelta(minutes=args.pre_buffer_minutes),
        timedelta(minutes=args.post_buffer_minutes),
    )
    if running:
        print("AtCoder contest guard is active. Do not use AI work here now.", file=sys.stderr)
        print(f"now: {now:%Y-%m-%d %H:%M:%S %Z}", file=sys.stderr)
        for start, end, name in running:
            print(
                f"- {name}: {start:%Y-%m-%d %H:%M} - {end:%Y-%m-%d %H:%M}",
                file=sys.stderr,
            )
        return 2

    print(f"No active AtCoder contest detected at {now:%Y-%m-%d %H:%M:%S %Z}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
