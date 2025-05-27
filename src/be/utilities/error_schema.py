error_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "error": {
            "type": "object",
            "properties": {
                "code": {
                    "type": "integer"
                },
                "message": {
                    "type": "string"
                },
                "errors": {
                    "type": "array",
                    "items": [
                        {
                            "type": "object",
                            "properties": {
                                "property": {
                                    "type": "string"
                                },
                                "message": {
                                    "type": "string"
                                },
                                "details": {
                                    "type": "object"
                                },
                                "children": {
                                    "type": "array",
                                    "items": {}
                                }
                            },
                            "required": [
                                "property",
                                "message",
                                "details",
                                "children"
                            ]
                        }
                    ]
                },
                "status": {
                    "type": "string"
                }
            },
            "required": [
                "code",
                "message",
                "errors",
                "status"
            ]
        },
        "timestamp": {
            "type": "string"
        }
    },
    "required": [
        "error",
        "timestamp"
    ]
}
