def ensure_memory(context):
    if not hasattr(context, "memory"):
        context.memory = {}
    return context.memory

def remember(context, key: str, value):
    mem = ensure_memory(context)
    mem[key] = value


def recall(context, key: str):
    mem = ensure_memory(context)
    return mem[key]