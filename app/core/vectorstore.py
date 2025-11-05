from typing import List, Dict, Any
import math

class InMemoryVectorStore:
    def __init__(self, dim: int = 1536):
        self.dim = dim
        self.rows: List[Dict[str, Any]] = []  # {key, content, embedding, meta...}

    def upsert(self, key: str, items: List[Dict[str, Any]]):
        for it in items:
            self.rows.append({"key": key, **it})

    @staticmethod
    def _cos(a: list[float], b: list[float]) -> float:
        dot = sum(x*y for x, y in zip(a, b))
        na = math.sqrt(sum(x*x for x in a))
        nb = math.sqrt(sum(y*y for y in b))
        return 0.0 if na == 0 or nb == 0 else dot / (na * nb)

    def search(self, key: str, qvec: list[float], k: int = 5):
        pool = [r for r in self.rows if r["key"] == key]
        ranked = sorted(pool, key=lambda r: -self._cos(r["embedding"], qvec))
        return ranked[:k]
