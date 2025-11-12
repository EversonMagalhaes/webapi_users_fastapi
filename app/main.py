from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, database, crud
from app.routers import users
from app import models
from app.database import engine

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="WebAPI Users - CRUD Completo")

app.include_router(users.router)

# Dependência para conexão com o banco
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota inicial
@app.get("/")
def root():
    return {"message": "API WebAPI Users v2 funcionando!"}

# Criar usuário
@app.post("/usuarios/", response_model=schemas.UserResponse)
def criar_usuario(usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    db_usuario = db.query(models.User).filter(models.User.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    return crud.criar_usuario(db, usuario)

# Listar usuários
@app.get("/usuarios/", response_model=list[schemas.UserResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    return crud.listar_usuarios(db)

# Buscar usuário por ID
@app.get("/usuarios/{usuario_id}", response_model=schemas.UserResponse)
def buscar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = crud.buscar_usuario(db, usuario_id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario

# Atualizar usuário
@app.put("/usuarios/{usuario_id}", response_model=schemas.UserResponse)
def atualizar_usuario(usuario_id: int, usuario: schemas.UserCreate, db: Session = Depends(get_db)):
    usuario_atualizado = crud.atualizar_usuario(db, usuario_id, usuario)
    if usuario_atualizado is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return usuario_atualizado

# Deletar usuário
@app.delete("/usuarios/{usuario_id}")
def deletar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    sucesso = crud.deletar_usuario(db, usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"mensagem": "Usuário deletado com sucesso!"}
