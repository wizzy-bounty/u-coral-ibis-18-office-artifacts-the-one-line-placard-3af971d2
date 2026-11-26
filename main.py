import os
from pathlib import Path

OUTPUT_FILENAME = "entry.txt"


def entry_text() -> str:
    return "Lanyard, c. 2026. Woven cord, plastic seal. Gift of Human Resources: a neck-ring proving its bearer was allowed indoors."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_FILENAME).write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
