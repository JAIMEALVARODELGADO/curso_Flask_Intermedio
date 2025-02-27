from app import db
from app.models import Editorial

def get_all_editoriales():
    return Editorial.query.all()

def get_editorial_by_id(id_editorial):
    return Editorial.query.get_or_404(id_editorial)

def create_editorial(editorial_data):
    editorial = Editorial(
        nombre_editorial = editorial_data['nombre_editorial']
        direccion = editorial_data['direccion']
        telefono = editorial_data['telefono']
        contacto = editorial_data['contacto']
    )
    db.session.add(editorial)
    db.session.commit()

def update_editorial(id_editorial, editorial_data):
    editorial = Editorial.query.get_or_404(id_editorial)        
    editorial.nombre_editorial = editorial_data['nombre_editorial']
    editorial.direccion = editorial_data['direccion']
    editorial.telefono = editorial_data['telefono']
    editorial.contacto = editorial_data['contacto']
    db.session.commit()

def delete_editorial(id_editorial):
    editorial = Editorial.query.get_or_404(id_editorial)
    db.session.delete(editorial)
    db.session.commit()
        
#def get_all_generos():
#    return Genero.query.all()

#def get_genero_by_id(id_genero):
#    return Genero.query.get_or_404(id_genero)

#def create_genero(genero_data):
#    genero = Genero(
#        nombre_genero = genero_data['nombre_genero']
#    )
#    db.session.add(genero)
#    db.session.commit()

#def update_genero(id_genero, genero_data):
#    genero = Genero.query.get_or_404(id_genero)        
#    genero.nombre_genero = genero_data['nombre_genero']
#    db.session.commit()

#def delete_genero(id_genero):
#    genero = Genero.query.get_or_404(id_genero)
#    db.session.delete(genero)
#    db.session.commit()