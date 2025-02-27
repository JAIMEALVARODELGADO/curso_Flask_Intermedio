from flask import Flask, render_template, request, redirect, url_for
from app import app, db
from app.models import Editorial
from app.models import Genero
from app.models import Libro
from app.models import Usuario
from app.models import Prestamo

import json

@app.route('/')
def index():
    #editoriales = Editorial.query.all()
    return render_template('index.html')


@app.route('/listaeditoriales')
def listaeditoriales():
    editoriales = Editorial.query.all()
    return render_template('editorial/index.html', editoriales = editoriales)
    

@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':        
        nombre_editorial = request.form['nombre_editorial']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        contacto = request.form['contacto']
        new_editorial = Editorial(nombre_editorial=nombre_editorial, direccion=direccion, telefono=telefono, contacto=contacto)
        db.session.add(new_editorial)
        db.session.commit()
        return redirect(url_for('listaeditoriales'))
    
    return render_template('editorial/create.html')

@app.route('/update/<int:id_editorial>', methods=['GET','POST'])
def update(id_editorial):
    editorial = Editorial.query.get_or_404(id_editorial)
    if request.method == 'POST':        
        editorial.nombre_editorial = request.form['nombre_editorial']
        editorial.direccion = request.form['direccion']
        editorial.telefono = request.form['telefono']
        editorial.contacto = request.form['contacto']
        db.session.commit()
        return redirect(url_for('listaeditoriales'))
    
    return render_template('editorial/update.html',editorial = editorial)

@app.route('/delete/<int:id_editorial>')
def delete(id_editorial):
    editorial = Editorial.query.get_or_404(id_editorial)
    db.session.delete(editorial)
    db.session.commit()
    return redirect(url_for('listaeditoriales'))

@app.route('/listageneros')
def listageneros():
    generos = Genero.query.all()
    return render_template('genero/index.html', generos = generos)  

@app.route('/creategenero', methods=['GET','POST'])
def creategenero():    
    if request.method == 'POST':        
        nombre_genero = request.form['nombre_genero']
        new_genero = Genero(nombre_genero=nombre_genero)
        db.session.add(new_genero)
        db.session.commit()
        return redirect(url_for('listageneros'))
    
    return render_template('genero/create.html')

@app.route('/updategenero/<int:id_genero>' , methods=['GET','POST'])
def updategenero(id_genero):
    genero = Genero.query.get_or_404(id_genero)
    if request.method == 'POST':        
        genero.nombre_genero = request.form['nombre_genero']
        db.session.commit()
        return redirect(url_for('listageneros'))
    
    return render_template('genero/update.html',genero = genero)

@app.route('/deletegenero/<int:id_genero>')
def deletegenero(id_genero):
    genero = Genero.query.get_or_404(id_genero)
    db.session.delete(genero)
    db.session.commit()
    return redirect(url_for('listageneros'))

@app.route('/listalibros')
def listalibros():    
    libros = db.session.query(Libro).join(Editorial, Libro.id_editorial == Editorial.id_editorial).join(Genero, Libro.id_genero == Genero.id_genero).add_columns(
        Libro.id_libro, Libro.nombre_libro, Libro.id_editorial, Libro.id_genero, Libro.autor, Libro.estado, Libro.codigo,
        Editorial.nombre_editorial, Genero.nombre_genero
    ).all()
    return render_template('libro/index.html', libros=libros)

@app.route('/createlibro', methods=['GET','POST'])
def createlibro():
    editoriales = Editorial.query.all()
    generos = Genero.query.all()
    if request.method == 'POST':        
        nombre_libro = request.form['nombre_libro']
        id_editorial = request.form['id_editorial']
        id_genero = request.form['id_genero']
        autor = request.form['autor']
        estado = request.form['estado']
        codigo = request.form['codigo']

        new_libro = Libro(nombre_libro=nombre_libro, 
                          id_editorial=id_editorial, 
                          id_genero=id_genero, autor=autor,
                          estado=estado, 
                          codigo=codigo)
        db.session.add(new_libro)
        db.session.commit()
        return redirect(url_for('listalibros'))
    
    return render_template('libro/create.html', editoriales = editoriales, generos = generos)

@app.route('/updatelibro/<int:id_libro>', methods=['GET','POST'])
def updatelibro(id_libro):
    libro = Libro.query.get_or_404(id_libro)
    editoriales = Editorial.query.all()
    generos = Genero.query.all()
    if request.method == 'POST':        
        libro.nombre_libro = request.form['nombre_libro']
        libro.id_editorial = request.form['id_editorial']
        libro.id_genero = request.form['id_genero']
        libro.autor = request.form['autor']
        libro.estado = request.form['estado']
        libro.codigo = request.form['codigo']
        db.session.commit()
        return redirect(url_for('listalibros'))
    
    return render_template('libro/update.html',libro = libro, editoriales = editoriales, generos = generos)

@app.route('/deletelibro/<int:id_libro>')
def deletelibro(id_libro):
    libro = Libro.query.get_or_404(id_libro)
    db.session.delete(libro)
    db.session.commit()
    return redirect(url_for('listalibros'))

@app.route('/listausuarios')
def listausuarios():
    usuarios = Usuario.query.all()    
    return render_template('usuario/index.html', usuarios=usuarios)
    

@app.route('/createusuario', methods=['GET','POST'])
def createusuario():
    if request.method == 'POST':                
        tipo_identificacion = request.form['tipo_identificacion']
        numero_identificacion = request.form['numero_identificacion']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        correo = request.form['correo']
        genero = request.form['genero']
        fecha_nacimiento = request.form['fecha_nacimiento']         
         
        new_usuario = Usuario(tipo_identificacion=tipo_identificacion,
                        numero_identificacion=numero_identificacion,
                        nombres=nombres,
                        apellidos=apellidos,
                        direccion=direccion,
                        telefono=telefono,
                        correo=correo,
                        genero=genero,
                        fecha_nacimiento=fecha_nacimiento)
        db.session.add(new_usuario)
        db.session.commit()
        return redirect(url_for('listausuarios'))
    
    return render_template('usuario/create.html')

@app.route('/updateusuario/<int:id_usuario>', methods=['GET','POST'])
def updateusuario(id_usuario):
     usuario = Usuario.query.get_or_404(id_usuario)
     if request.method == 'POST':        
         usuario.tipo_identificacion = request.form['tipo_identificacion']
         usuario.numero_identificacion = request.form['numero_identificacion']
         usuario.nombres = request.form['nombres']
         usuario.apellidos = request.form['apellidos']
         usuario.direccion = request.form['direccion']
         usuario.telefono = request.form['telefono']
         usuario.correo = request.form['correo']
         usuario.genero = request.form['genero']
         usuario.fecha_nacimiento = request.form['fecha_nacimiento']
         
         db.session.commit()
         return redirect(url_for('listausuarios'))
    
     return render_template('usuario/update.html',usuario = usuario)

# @app.route('/deletelibro/<int:id_libro>')
# def deletelibro(id_libro):
#     libro = Libro.query.get_or_404(id_libro)
#     db.session.delete(libro)
#     db.session.commit()
#     return redirect(url_for('listalibros'))

@app.route('/listaprestamos')
def listaprestamos():
        
    prestamos = db.session.query(Prestamo).join(Usuario, Prestamo.id_usuario == Usuario.id_usuario).join(Libro, Prestamo.id_libro == Libro.id_libro).add_columns(
        Prestamo.id_prestamo, Prestamo.id_usuario, Prestamo.id_libro, Prestamo.fecha_prestamo, Prestamo.fecha_devolucion,Prestamo.observacion,
        Usuario.nombres,Usuario.apellidos, Libro.nombre_libro
    ).filter(Prestamo.fecha_devolucion == None).all()

    usuarios = Usuario.query.order_by(Usuario.nombres).all()

    libros = Libro.query.order_by(Libro.nombre_libro).all()       

    return render_template('prestamo/index.html', prestamos=prestamos, usuarios = usuarios, libros = libros)

@app.route('/createprestamo', methods=['GET','POST'])
def createprestamo():
    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        id_libro = request.form['id_libro']
        fecha_prestamo = request.form['fecha_prestamo']        
        observacion = request.form['observacion']        
         
        new_prestamo = Prestamo(
            id_usuario=id_usuario,
            id_libro=id_libro,
            fecha_prestamo=fecha_prestamo,            
            observacion=observacion)
        db.session.add(new_prestamo)
        db.session.commit()
    return redirect(url_for('listaprestamos'))            
    
@app.route('/devolucion', methods=['GET','POST'])
def devolucion():
    if request.method == 'POST':
        id_prestamo = request.form['id_prestamoE']
        prestamo = Prestamo.query.get_or_404(id_prestamo)
        prestamo.fecha_devolucion = request.form['fecha_devolucionE']
        prestamo.observacion = request.form['observacionE']
        db.session.commit()
        return redirect(url_for('listaprestamos'))


    return redirect(url_for('listaprestamos'))   