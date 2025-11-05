from pathlib import Path

class FileLoaderTool:
    name = "load_text_file"
    description = "Load local .txt or .md file content (dev only, restricted)"
    parameters = {"type":"object","properties":{"path":{"type":"string"}},"required":["path"]}

    async def __call__(self, path: str):
        p = Path(path)
        if not p.suffix.lower() in {".txt", ".md"}:
            return {"error": "only .txt/.md allowed"}
        if not p.exists() or not p.is_file():
            return {"error": "file not found"}
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")
            return {"path": str(p), "size": len(text), "preview": text[:1000]}
        except Exception as e:
            return {"error": str(e)}
