language_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {"name": {"type": "string", "minLength": 2, "pattern": "^[A-Za-z]+$"}},
    "required": ["name"],
}

category_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {"name": {"type": "string", "minLength": 2, "pattern": "^[A-Za-z]+$"}},
    "required": ["name"],
}

word_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "text": {"type": "string", "minLength": 2, "pattern": "^[A-Za-z]+$"},
        "category": {"type": "integer"},
        "language": {"type": "integer"},
    },
    "required": ["text", "category", "language"],
}

sentence_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "text": {
            "type": "string",
            "minLength": 4,
        },
        "category": {"type": "integer"},
        "language": {"type": "integer"},
    },
    "required": ["text", "category", "language"],
}
