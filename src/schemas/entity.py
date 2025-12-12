ENTITY_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"}
    },
    "required": ["id", "name", "description"]
}

ENTITIES_SCHEMA = {
    "type": "object",
    "properties": {
        "entities": {
            "type": "array",
            "items": ENTITY_SCHEMA
            }
    },
    "required": ["entities"]
}