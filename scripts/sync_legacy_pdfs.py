"""Keep previously shared /Personal_Webpage/files/ PDF links working."""

from pathlib import Path
import shutil


def main():
    root = Path(__file__).resolve().parents[1]
    destination = root / "Personal_Webpage" / "files"
    destination.mkdir(parents=True, exist_ok=True)
    for name in ("ShiqiLI_CV.pdf", "ShiqiLI_JMP.pdf"):
        shutil.copy2(root / "files" / name, destination / name)
        print(f"Updated Personal_Webpage/files/{name}")


if __name__ == "__main__":
    main()
