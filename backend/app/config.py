from pydantic import BaseModel, ValidationError

class Settings(BaseModel):
    database_url: str
    secret_key: str
    mercadopago_api_key: str

def validate_and_create_settings(data):
    try:
        # Validate and create the Settings object
        settings = Settings(**data)
        return settings
    except ValidationError as e:
        # Handle validation errors gracefully
        print(f"Invalid data: {e}")
        return None

# Example usage with user input (replace with your actual input source)
user_input = {
    "database_url": "your_database_url",
    "secret_key": "your_secret_key",
    "mercadopago_api_key": "your_mercadopago_api_key"
}

settings = validate_and_create_settings(user_input)
if settings:
    # Use the validated settings object
    print(settings.database_url)