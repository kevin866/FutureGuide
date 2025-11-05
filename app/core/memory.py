from collections import defaultdict
from typing import List, Dict

class InMemoryShortTermMemory:
    def __init__(self):
        self._store: Dict[str, List[dict]] = defaultdict(list)

    def append(self, key: str, role: str, content: str):
        self._store[key].append({"role": role, "content": content})

    def get(self, key: str) -> List[dict]:
        return list(self._store.get(key, []))

    def clear(self, key: str):
        self._store.pop(key, None)
