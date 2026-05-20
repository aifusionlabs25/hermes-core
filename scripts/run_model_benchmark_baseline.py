from __future__ import annotations

import subprocess
import time
from pathlib import Path


REPO = Path(r"C:\AI Fusion Labs\X AGENTS\REPOS\Hermes Core")
OUT = REPO / "docs" / "model-benchmark-baseline-2026-05-19.md"

PROMPTS = [
    (
        "Daily Brief v2",
        "Give me a Daily Brief v2 using loaded context only. Do not check Gmail or Calendar. Use ASCII only. Include Sources and Needs Rob approval.",
    ),
    (
        "Gmail Triage Rules",
        "Tell me how you would safely triage rob-personal Gmail. Do not run commands. Use ASCII only.",
    ),
    (
        "Capture to Linear Judgment",
        "Triage inbox and suggest Linear issues. Do not create them yet. Do not force stale captures, tests, duplicates, handled notes, or vague ideas into issues.",
    ),
    (
        "X Agents GTM Planning",
        "Draft a Local Lead Scout plan for 10 blue-collar trade businesses within 10 miles of 85045. Public web only. Do not save files, send outreach, create Linear issues, or create X-LINK work orders. Show lead fields, scoring method, and first batch plan.",
    ),
    (
        "X-LINK Work Order Draft",
        "Using a hypothetical market signal that HVAC companies miss after-hours leads, draft a proposed X-LINK work order. Do not create it.",
    ),
]


def run_prompt(prompt: str) -> tuple[float, str]:
    started = time.perf_counter()
    proc = subprocess.run(
        [
            "wsl.exe",
            "/home/ai_fusion_labs/.local/bin/hermes",
            "-p",
            "xlink-core",
            "-z",
            prompt,
            "--accept-hooks",
        ],
        cwd=str(REPO),
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        timeout=300,
    )
    elapsed = round(time.perf_counter() - started, 2)
    output = proc.stdout.strip()
    if proc.stderr.strip():
        output += "\n\nSTDERR:\n" + proc.stderr.strip()
    if proc.returncode != 0:
        output += f"\n\nRETURN_CODE: {proc.returncode}"
    return elapsed, output


def main() -> None:
    parts = [
        "# Model Benchmark Baseline - 2026-05-19",
        "",
        "Provider:",
        "- nvidia",
        "",
        "Model:",
        "- openai/gpt-oss-120b",
        "",
        "Notes:",
        "- Baseline run before xAI/Grok OAuth is connected.",
        "- Outputs are from Hermes oneshot mode through xlink-core.",
        "- These results are for comparison, not a final model decision.",
        "",
    ]
    for name, prompt in PROMPTS:
        elapsed, output = run_prompt(prompt)
        ascii_ok = all(ord(ch) < 128 for ch in output)
        parts.extend(
            [
                f"## {name}",
                "",
                "Latency seconds:",
                f"- {elapsed}",
                "",
                "ASCII clean:",
                f"- {'yes' if ascii_ok else 'no'}",
                "",
                "Prompt:",
                "```text",
                prompt,
                "```",
                "",
                "Output:",
                "```text",
                output,
                "```",
                "",
            ]
        )
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
