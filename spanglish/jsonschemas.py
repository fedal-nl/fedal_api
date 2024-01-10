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

translation_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "word": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
        "sentence": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
        "translation": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
            "uniqueItems": True,
        },
        "language": {"type": "integer"},
        "added_at": {"type": "string", "format": "date-time"},
    },
    "required": ["translation", "language"],
    "anyOf": [
        {"required": ["word"]},
        {"required": ["sentence"]},
    ],
}

verb_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "word": {"type": "integer"},
        "tense": {"type": "string"},
        "yo": {"type": "string"},
        "tu": {"type": "string"},
        "usted": {"type": "string"},
        "nosotros": {"type": "string"},
        "vosotros": {"type": "string"},
        "ustedes": {"type": "string"},
    },
}
