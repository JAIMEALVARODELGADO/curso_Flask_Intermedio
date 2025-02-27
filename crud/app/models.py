from app import db

class Editorial(db.Model):
    __tablename__ = 'editorial'
    id_editorial = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_editorial = db.Column(db.String(40), nullable=True)
    direccion = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(20), nullable=True)
    contacto = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return f'<Editorial{self.nombre_editorial}>'
    
class Genero(db.Model):
    __tablename__ = 'genero'
    id_genero = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_genero = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        return f'<Genero{self.nombre_genero}>'
    
class Libro(db.Model):
    __tablename__ = 'libro'
    id_libro = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_libro = db.Column(db.String(80), nullable=True)    
    id_editorial = db.Column(db.Integer, db.ForeignKey('editorial.id_editorial'))
    id_genero = db.Column(db.Integer, db.ForeignKey('genero.id_genero'))
    autor = db.Column(db.String(80), nullable=True)
    estado = db.Column(db.String(50), nullable=True)
    codigo = db.Column(db.String(10), nullable=True)

    editorial = db.relationship('Editorial', backref=db.backref('libros', lazy=True))
    genero = db.relationship('Genero', backref=db.backref('libros', lazy=True))

    def __repr__(self):
        return f'<Libro{self.nombre_libro}>'
    
class Usuario(db.Model):
    __tablename__ = 'usuario'
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo_identificacion = db.Column(db.String(2), nullable=True)
    numero_identificacion = db.Column(db.String(10), nullable=True)
    nombres = db.Column(db.String(40), nullable=True)
    apellidos = db.Column(db.String(40), nullable=True)
    direccion = db.Column(db.String(100), nullable=True)
    telefono = db.Column(db.String(10), nullable=True)
    correo = db.Column(db.String(100), nullable=True)
    genero = db.Column(db.String(1), nullable=True)
    fecha_nacimiento = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f'<Usuario{self.nombres}>'
    
class Prestamo(db.Model):
    __tablename__ = 'prestamo'
    id_prestamo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'))
    id_libro = db.Column(db.Integer, db.ForeignKey('libro.id_libro'))
    fecha_prestamo = db.Column(db.Date, nullable=True)
    fecha_devolucion = db.Column(db.Date, nullable=True)
    observacion = db.Column(db.String(100), nullable=True)

    usuario = db.relationship('Usuario', backref=db.backref('prestamos', lazy=True))
    libro = db.relationship('Libro', backref=db.backref('prestamos', lazy=True))    

    def __repr__(self):
        return f'<Prestamo{self.id_prestamo}>'