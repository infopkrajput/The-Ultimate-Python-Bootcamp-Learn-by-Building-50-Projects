from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must be at least 4 characters long')
        if not v.isalnum():
            raise ValueError('Username must contain only alphanumeric characters')
        return v

class SignupData(BaseModel):
    email: str
    password: str

    @field_validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            raise ValueError('Invalid email address')
        return v

    @model_validator(mode='after')
    def validate_password(cls, v):
        if len(v.password) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v