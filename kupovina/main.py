from fastapi import FastAPI, Depends, status, Response
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/kupovina', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Kupovina, db : Session = Depends(get_db)):
    nova_kupovina = models.Kupovina(kupac=request.kupac, grad=request.grad, proizvod=request.proizvod, cijena=request.cijena)
    db.add(nova_kupovina)
    db.commit()
    db.refresh(nova_kupovina)
    return nova_kupovina


@app.delete('/kupovina/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session = Depends(get_db)):
    db.query(models.Kupovina).filter(models.Kupovina.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'



@app.get('/kupovina')
def all(db: Session = Depends(get_db)):
    kupovine = db.query(models.Kupovina).all()
    return kupovine


@app.get('/kupovina/{id}', status_code=200)
def show(id, response: Response, db: Session = Depends(get_db)):
    kupovina = db.query(models.Kupovina).filter(models.Kupovina.id == id).first()
    if not kupovina:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail':f"Kupovina {id} ne postoji"}
    return kupovina
