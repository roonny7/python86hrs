from empleado import Empleado

class Empresa:
    def __init__(self, nombre_empresa):
        self.nombre_empresa = nombre_empresa
        self.empleados = []

    def contratar_empleados(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self.empleados.append(empleado)

    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:
                contador_empleados_por_departamento += 1

        return contador_empleados_por_departamento

    def obtener_total_empleados(self):
        print(f'\nEl total de empleados para la empresa {self.nombre_empresa}')
        for empleado in self.empleados:
            print(f'''Empleado : {empleado.id}
            Nombre : {empleado.nombre}
            Departamento : {empleado.departamento}                
            ''')