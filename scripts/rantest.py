#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def resolve_auto_files(target: Path) -> tuple[Path, Path]:
    gen = target.with_name(f"{target.stem}_gen.py")
    oracle_candidates = [
        target.with_name(f"{target.stem}_oracle.py"),
        target.with_name(f"{target.stem}_naive.py"),
    ]

    if not gen.exists():
        raise FileNotFoundError(f"generator not found: {gen}")

    for oracle in oracle_candidates:
        if oracle.exists():
            return gen, oracle

    names = ", ".join(str(path) for path in oracle_candidates)
    raise FileNotFoundError(f"oracle not found. expected one of: {names}")


def run_command(
    command: list[str],
    input_text: str | None,
    timeout: float,
) -> tuple[int, str, str, float]:
    started = time.perf_counter()
    try:
        completed = subprocess.run(
            command,
            input=input_text,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
        )
        elapsed = time.perf_counter() - started
        return completed.returncode, completed.stdout, completed.stderr, elapsed
    except subprocess.TimeoutExpired as exc:
        elapsed = time.perf_counter() - started
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        return 124, stdout, stderr + f"\nTIMEOUT after {timeout}s", elapsed


def normalize(text: str, mode: str) -> str | list[str]:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    if mode == "token":
        return text.split()
    return text.rstrip()


def print_block(title: str, body: str) -> None:
    print(f"--- {title} ---")
    if body:
        print(body, end="" if body.endswith("\n") else "\n")
    else:
        print("(empty)")


def save_failure(
    save_dir: Path,
    seed: int,
    case_input: str,
    expected: str,
    actual: str,
    meta: dict[str, object],
) -> Path:
    failure_dir = save_dir / f"seed-{seed:06d}"
    failure_dir.mkdir(parents=True, exist_ok=True)
    (failure_dir / "input.txt").write_text(case_input)
    (failure_dir / "expected.out").write_text(expected)
    (failure_dir / "actual.out").write_text(actual)
    (failure_dir / "meta.json").write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    return failure_dir


def run_contest_guard() -> int:
    guard = ROOT / "scripts" / "check_atcoder_quiet.py"
    return subprocess.call([sys.executable, str(guard)])


def main() -> int:
    parser = argparse.ArgumentParser(description="Run random tests for an AtCoder solution.")
    parser.add_argument("target", help="solution file, for example src/abc999/c.py")
    parser.add_argument("--auto", action="store_true", help="use *_gen.py and *_oracle.py next to target")
    parser.add_argument("--gen", help="generator file. It receives seed as argv[1].")
    parser.add_argument("--oracle", help="oracle/bruteforce file. It receives generated input on stdin.")
    parser.add_argument("--cases", type=int, default=100)
    parser.add_argument("--seed", type=int, default=0, help="first seed")
    parser.add_argument("--timeout", type=float, default=2.0)
    parser.add_argument("--python", default=sys.executable, help="Python executable for target/gen/oracle")
    parser.add_argument("--compare", choices=["strip", "token"], default="strip")
    parser.add_argument("--save-failure-dir", help="directory to save failing cases")
    parser.add_argument("--require-contest-quiet", action="store_true")
    args = parser.parse_args()

    if args.require_contest_quiet:
        guard_code = run_contest_guard()
        if guard_code != 0:
            return guard_code

    target = Path(args.target).resolve()
    if args.auto:
        gen, oracle = resolve_auto_files(target)
    else:
        if not args.gen or not args.oracle:
            parser.error("either use --auto or pass both --gen and --oracle")
        gen = Path(args.gen).resolve()
        oracle = Path(args.oracle).resolve()

    for path in [target, gen, oracle]:
        if not path.exists():
            print(f"file not found: {path}", file=sys.stderr)
            return 1

    print(f"target : {target}")
    print(f"gen    : {gen}")
    print(f"oracle : {oracle}")
    print(f"cases  : {args.cases} seeds {args.seed}..{args.seed + args.cases - 1}")

    for offset in range(args.cases):
        seed = args.seed + offset

        gen_rc, case_input, gen_err, gen_time = run_command(
            [args.python, str(gen), str(seed)],
            None,
            args.timeout,
        )
        if gen_rc != 0:
            print(f"\nGenerator failed at seed {seed} (rc={gen_rc}, {gen_time:.3f}s)")
            print_block("stderr", gen_err)
            return 1

        oracle_rc, expected, oracle_err, oracle_time = run_command(
            [args.python, str(oracle)],
            case_input,
            args.timeout,
        )
        target_rc, actual, target_err, target_time = run_command(
            [args.python, str(target)],
            case_input,
            args.timeout,
        )

        expected_norm = normalize(expected, args.compare)
        actual_norm = normalize(actual, args.compare)
        ok = oracle_rc == 0 and target_rc == 0 and expected_norm == actual_norm

        if not ok:
            print(f"\nMismatch at seed {seed}")
            print(f"oracle rc={oracle_rc} time={oracle_time:.3f}s")
            print(f"target rc={target_rc} time={target_time:.3f}s")
            print_block("input", case_input)
            print_block("expected", expected)
            print_block("actual", actual)
            if oracle_err:
                print_block("oracle stderr", oracle_err)
            if target_err:
                print_block("target stderr", target_err)

            if args.save_failure_dir:
                saved = save_failure(
                    Path(args.save_failure_dir),
                    seed,
                    case_input,
                    expected,
                    actual,
                    {
                        "seed": seed,
                        "target": str(target),
                        "gen": str(gen),
                        "oracle": str(oracle),
                        "oracle_rc": oracle_rc,
                        "target_rc": target_rc,
                    },
                )
                print(f"saved failure: {saved}")
            return 1

        if offset == 0 or (offset + 1) % 100 == 0 or offset + 1 == args.cases:
            print(f"ok {offset + 1}/{args.cases} seed={seed}")

    print("all cases passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
