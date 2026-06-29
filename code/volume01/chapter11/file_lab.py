from pathlib import Path


def write_report(output_dir: Path, title: str, lines: list[str]) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "report.txt"
    content = title + "\n" + "=" * len(title) + "\n" + "\n".join(lines) + "\n"
    report_path.write_text(content, encoding="utf-8")
    return report_path


def read_report(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8")


if __name__ == "__main__":
    path = write_report(Path("outputs"), "File Lab", ["Created by Python.", "Stored on disk."])
    print(read_report(path))
