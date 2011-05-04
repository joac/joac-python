from elixir import *
import datetime
metadata.bind = "sqlite:///flowtec.db"
metadata.bind.echo = True

class Nota_Pedido(Entity):
    """Define la entidad nota de pedido, con los campos indicados"""
    using_options(tablename = "Notas_Pedido")
    proveedor = ManyToOne("Proveedor")
    items = ManyToMany("Producto")
    fichaTecnica = Field(Integer)
    responsable = Field(Unicode(30), required=True)
    vendedor = ManyToOne("Vendedor")
    fechaEntrega = Field(DateTime, default=datetime.date.today())
    fechaElab = Field(Date, default=datetime.date.today())
    tipoEntrega = ManyToOne("Tipo_Entrega")
    total = Field(Numeric)

class Producto(Entity):
    """Define un producto"""
    using_options(tablename = "Producto")
    descripcion = Field(Unicode(30), required=True)
    codigoFabricante = Field(Unicode(20))
    numeroAlmacen = Field(Unicode(20))
    proveedor = ManyToOne("Proveedor")
    tipoIva = ManyToOne("Iva")
    precio = Field(Numeric)

class Proveedor(Entity):
    using_options(tablename = "Proveedores")
    nombre = Field(Unicode(30), required = True)
    direccion = Field(Unicode(50))
    postalCode = Field(Unicode(10))
    telefono1 = Field(Unicode(20))
    telefono2 = Field(Unicode(20))
    fax = Field(Unicode(20))
    email = Field(UnicodeText) 
    vendedores = OneToMany("Vendedor")
    formasPago = ManyToMany("Forma_Pago")
class Iva(Entity):
    valor = Field(Numeric)
    productos = OneToMany("Producto")

class Tipo_Entrega(Entity):
    nombre = Field(Unicode(30))
    notasPedido = OneToMany("Nota_Pedido")

class Vendedor(Entity):
    using_options(tablename="vendedores")
    nombre = Field(Unicode (30))
    empresa = ManyToOne("Proveedor")

class Comprador(Entity):
    pass

class Forma_Pago(Entity):
    nombre = Field(Unicode(50))
    notasPedido = ManyToMany("Proveedor")

def initDB():
    pass
