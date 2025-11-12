from sqlalchemy.orm import Session
from . import models, schemas

# Criar novo usuário
def criar_usuario(db: Session, usuario: schemas.UserCreate):
    novo_usuario = models.User(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

# Listar todos os usuários
def listar_usuarios(db: Session):
    return db.query(models.User).all()

# Buscar usuário por ID
def buscar_usuario(db: Session, usuario_id: int):
    return db.query(models.User).filter(models.User.id == usuario_id).first()

# Atualizar usuário existente
def atualizar_usuario(db: Session, usuario_id: int, usuario: schemas.UserCreate):
    usuario_existente = buscar_usuario(db, usuario_id)
    if usuario_existente:
        for key, value in usuario.model_dump().items():
            setattr(usuario_existente, key, value)
        db.commit()
        db.refresh(usuario_existente)
        return usuario_existente
    return None

# Deletar usuário
def deletar_usuario(db: Session, usuario_id: int):
    usuario_existente = buscar_usuario(db, usuario_id)
    if usuario_existente:
        db.delete(usuario_existente)
        db.commit()
        return True
    return False
