from voluptuous import Schema, PREVENT_EXTRA, Optional, Required


create_user_schema = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    required=True,
    extra=PREVENT_EXTRA,
)


login_successful_schema = Schema(
    {
        "token": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)

login_unsuccessful_schema = Schema(
    {
        "error": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)


user_data_schema = Schema(
    {
        Required("data"): {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str,
        },
        Optional("support"): {
            "url": str,
            "text": str,
        }
    },
    required=True,
    extra=PREVENT_EXTRA,
)


register_unsuccessful_user_schema = Schema(
    {
        "error": str,
    },
    required=True,
    extra=PREVENT_EXTRA,
)
