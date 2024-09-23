
from fastapi import APIRouter,Form,Depends
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from db.deps import get_conection
from schema.user_schema import User_schema,User_Schema_Output
from use_case.user_use_cases import User_use_cases

front_router = APIRouter(prefix="/front")



templates = Jinja2Templates(directory="templates")

#ALTEREI ESSA ROTA, A ROTA (/) AGORA VAI PARA O HOME DA PAG.
@front_router.get("/")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="home.html")

#ALTEREI ESSA ROTA, A ROTA (/nota) AGORA VAI PARA ESCREVERMOS A NOSSA NOTA.
@front_router.get("/nota")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="nota.html")

#ALTEREI ESSA ROTA, A ROTA (/toda/nota) FUTURAMENTE VAI PARA VISUALIZAR AS NOTAS
@front_router.get("/toda/nota")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="buscar_nota.html")

@front_router.get("/cadastro")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="cadastro.html")

@front_router.get("/login")
def read_front(request:Request):
    return templates.TemplateResponse(request=request,name="login.html")

@front_router.post("/result-form",response_model=User_Schema_Output)
def post_front(request:Request, fname:str=Form(...),cpf:str= Form(...),password:str= Form(...),db_session:Session = Depends(get_conection)):
    person = User_schema(name=fname,cpf=cpf,password=password)
    uc = User_use_cases(db_session=db_session)
    uc.post_user(person)
    return templates.TemplateResponse(request=request,name="nota.html")

#@front_router.post("/enviar-nota", response_model=Nota_Salva_saida)
#def enviar_nota(titulo:str=Form(...),anotacao:str=Form(...),db_session:Session = Depends(get_conection)):
#    nota = Nota_Salva(title=titulo,text=anotacao)
#    uc = User_use_cases(db_session=db_session)
#    uc.enviar_nota(nota)
#    return nota

    
