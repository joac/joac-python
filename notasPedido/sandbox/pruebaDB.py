from elixir import *
metadata.bind = "sqlite:///sandbox.db"
metadata.bind.echo = True

class Empresa(Entity):
    using_options(tablename = 'Empresas')
    nombre = Field(Unicode(30))
    razon_social = Field(Unicode(30), primary_key = True)
    direccion= OneToMany('Direccion')
   # datos_proveedor = OneToOne('Proveedor')
    datos_cliente = OneToOne('Cliente')
    def __repr__(self):
        return '<%s(%s)>' %(self.nombre, self.razon_social)

class Direccion(Entity):
    using_options(tablename ='Direccion')
    calle = Field(Unicode(30))
    ciudad = Field(Unicode(30))
    provincia = Field(Unicode(30))
    empresa = ManyToOne('Empresa')
    def __repr__(self):

        return '<%s | %s, %s, %s>'%(str(self.empresa),\
                                    self.calle,\
                                    self.ciudad,\
                                    self.provincia)
class Proveedor(Entity):
    using_options(tablename = 'Proveedores')
   # empresa = OneToOne('Empresa')
    #vendedores = OneToMany('Vendedores')

class Cliente(Entity):
    using_options(tablename = "Clientes")
    empresa = OneToOne('Empresa')
    compradores = Field(Unicode(30))

def populate():

    casa = Direccion(calle = u'Corrientes 6477',\
                    ciudad = u'Capital Federal',\
                    provincia = u'Buenos Aires')
    dir1 = Direccion(calle = u'Mariano Acha 4046',\
                    ciudad = u'Capital Federal',\
                    provincia = u'Buenos Aires')
    dir2 = Direccion(calle = u'Florencio Varela 534',\
                    ciudad = u'Villa Martelli',\
                    provincia = u'Buenos Aires')
    mama = Direccion(calle = u'De la Garua 1492',\
                    ciudad = u'Bariloche',\
                    provincia = 'Rio Negro')
    laCasita = Empresa(nombre = u'La Casita de Mama',\
             razon_social = u'Cecilia Pepe',\
             direccion = [mama])
    flowtec = Empresa(nombre = u'Flowtec',\
            razon_social = u'Flowtec SRL',\
            direccion = [dir1, dir2])
    yo = Empresa(nombre = u'Joac',\
             razon_social = u'Joaquin Sorianello',\
             direccion = [casa])
    Proveedor(empresa = yo)
    Cliente(empresa = flowtec)
    Proveedor(empresa = laCasita)
    Cliente(empresa = laCasita)
    session.commit()
    
