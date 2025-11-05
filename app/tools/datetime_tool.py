from datetime import datetime, timezone

class DateTimeTool:
    name = "now"
    description = "Get current UTC time in ISO-8601"
    parameters = {"type": "object", "properties": {}, "required": []}

    async def __call__(self):
        return {"now": datetime.now(timezone.utc).isoformat()}
