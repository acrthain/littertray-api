from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from engine import Engine
from datetime import datetime
from tray_visit import TrayVisit
from fastapi import HTTPException

app = FastAPI()


class CatOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    age: int


class CatIn(BaseModel):
    name: str
    age: int


class TrayVisitOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    time: datetime
    visit_type: str
    cat_weight: float
    cat: CatOut


class TrayVisitIn(BaseModel):
    visit_type: str
    cat_weight: float
    cat_id: int


@app.get("/allcats", response_model=list[CatOut])
async def all_cats():
    engine = Engine()
    return engine.print_cats()


@app.post("/cats", response_model=CatOut)
async def create_cat(cat: CatIn):
    engine = Engine()
    return engine.add_cat(cat.name, cat.age)


@app.delete("/cats/{cat_id}")
async def delete_cat(cat_id: int):
    engine = Engine()
    if not engine.delete_cat(cat_id):
        raise HTTPException(status_code=404, detail=f"Cat {cat_id} not found")
    return {"message": f"Cat {cat_id} deleted"}


@app.get("/alltrayvisits", response_model=list[TrayVisitOut])
async def all_tray_visits():
    engine = Engine()
    return engine.print_tray_visits()


@app.post("/tray-visits", response_model=TrayVisitOut)
async def create_tray_visit(visit: TrayVisitIn):
    engine = Engine()
    return engine.add_tray_visit(visit.visit_type, visit.cat_weight, visit.cat_id)


@app.delete("/tray-visits/{tray_visit_id}")
async def delete_tray_visit(tray_visit_id: int):
    engine = Engine()
    if not engine.delete_tray_visit(tray_visit_id):
        raise HTTPException(status_code=404, detail=f"Tray visit {tray_visit_id} not found")
    return {"message": f"Tray visit {tray_visit_id} deleted"}
