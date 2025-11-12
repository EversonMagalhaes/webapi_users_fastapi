from pydantic import BaseModel, EmailStr

# Schema usado para exibir usuários (dados de saída)
class UserBase(BaseModel):
    nome: str
    email: EmailStr
    idade: int


# Schema usado na criação de um novo usuário (entrada)
class UserCreate(UserBase):
    pass


# Schema usado quando o usuário já existe no banco (tem ID)
class UserResponse(UserBase):
    id: int

class Config:
    from_attributes = True
