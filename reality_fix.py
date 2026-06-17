
import pathlib

# Remove unused version in cli.py line ~167
cli = pathlib.Path("typer/cli.py")
if cli.exists():
    lines = cli.read_text().splitlines()
    # Find line with "version ="
    for i, line in enumerate(lines):
        if "version" in line and "=" in line and "get_version" in line.lower():
            print(f"Found at line {i+1}: {line}")
            # Comment out instead of delete to be safe
            lines[i] = f"# REMOVED by Reality OS: {line}"
            break
    cli.write_text("\n".join(lines) + "\n")
    print("Patched cli.py")

# Remove ReadableBuffer import
testing = pathlib.Path("typer/testing.py")
if testing.exists():
    text = testing.read_text()
    new_text = text.replace("from typing import ReadableBuffer\n", "")
    new_text = new_text.replace("ReadableBuffer, ", "")
    testing.write_text(new_text)
    print("Patched testing.py")
