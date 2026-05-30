import nbformat
import uuid
from pathlib import Path

for path in Path(".").rglob("*.ipynb"):
    nb = nbformat.read(path, as_version=4)
    nb.nbformat_minor = 5
    for cell in nb.cells:
        if "id" not in cell:
            cell["id"] = cell.get("metadata", {}).pop("id", str(uuid.uuid4())[:8])
    nbformat.write(nb, path)
    print(f"Corrigé : {path}")
