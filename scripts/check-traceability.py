"""Check defined UC/FR coverage and local links; report unassigned releases honestly."""
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
matrix = ROOT / "docs/traceability.md"
text = matrix.read_text(encoding="utf-8")
requirements = ROOT / "docs/requirements"
defined = set(re.findall(r"^### (UC-[\w-]+):", (requirements / "use-cases.md").read_text(encoding="utf-8"), re.M))
defined.update(re.findall(r"^- \*\*`(FR-[\w-]+)`", (requirements / "software-requirements-specification.md").read_text(encoding="utf-8"), re.M))
rows = re.findall(r"^\| `(UC-[\w-]+|FR-[\w-]+)`\s*\|(.+)$", text, re.M)
found = [identifier for identifier, _ in rows]
errors = []
for identifier in sorted(defined - set(found)):
    errors.append(f"Missing row: {identifier}")
for identifier in sorted(set(found)):
    if found.count(identifier) != 1:
        errors.append(f"Duplicate row: {identifier}")
    if identifier not in defined:
        errors.append(f"Row without a definition: {identifier}")

def anchors(content):
    counts = {}
    result = set()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", content, re.M):
        heading = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", heading).lower()
        slug = "".join(c for c in heading if c in "-_ " or unicodedata.category(c)[0] in "LN").replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug if number == 0 else f"{slug}-{number}")
    return result

local_count = 0
for document in [matrix, *sorted((ROOT / "docs/checkpoints").glob("*.md"))]:
    for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", document.read_text(encoding="utf-8")):
        if re.match(r"[a-z]+://", link):
            continue
        local_count += 1
        target, _, fragment = unquote(link).partition("#")
        path = document.parent / target if target else document
        if not path.is_file():
            errors.append(f"Missing link target in {document.name}: {link}")
        elif fragment and fragment not in anchors(path.read_text(encoding="utf-8")):
            errors.append(f"Missing anchor in {document.name}: {link}")
unassigned = []
for identifier, row in rows:
    cells = [cell.strip() for cell in row.split("|")]
    release = cells[2].strip("`")
    if release not in {"v0.1.0", "v0.2.0", "v1.0.0", "Spring", "Out"}:
        unassigned.append(identifier)
print(f"Coverage: {len(defined)} defined UC/FRs; {len(rows)} rows. Local links checked: {local_count}.")
for error in errors:
    print(f"ERROR: {error}")
print(f"Release decisions pending: {len(unassigned)}")
for identifier in unassigned:
    print(f"PENDING: {identifier}")
print("External URLs and passing flow coverage require separate evidence review.")
sys.exit(1 if errors or unassigned else 0)
