from typing import Any, List
from uuid import uuid4

def random_string(len: int):
    return "".join(uuid4().hex for _ in range(len // 32 + 1))[:len]

async def lazy_async(lazy: bool, condition: bool, action: Any):
    if lazy:
        if condition:
            await action()
    else:
        await action()

def page_category(page_id: str):
    if ":" in page_id:
        return page_id.split(":")[0]
    else:
        return "_default"
    
def normalize_tag(tag: str) -> str:
        if tag.lower().startswith('_default:'):
            return tag[9:]
        return tag
    
def include_tags(tags: List[str]):
    return list(map(lambda t: f"+{t.replace("+", "").replace("-", "")}", tags))

def exclude_tags(tags: List[str]):
    return list(map(lambda t: f"-{t.replace("+", "").replace("-", "")}", tags))