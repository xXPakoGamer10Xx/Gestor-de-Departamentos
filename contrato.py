def obtener_texto_contrato(cliente, fecha_inicio, fecha_fin, costo_letras):
    margen_izquierdo = " " * 4  # 4 espacios de margen izquierdo
    ancho_texto = 72  # Ancho del texto para centrarlo
    ancho_total = ancho_texto + len(margen_izquierdo)
    espacio_firma = "_" * 25
    
    def centrar(texto):
        return texto.center(ancho_texto)
    
    def linea(texto):
        return margen_izquierdo + texto
    
    contrato = "\n" * 3  # 3 líneas en blanco al principio

    contrato += f"""
{linea(centrar("Contrato de Arrendatario"))}

{linea(f"{fecha_inicio:>70}")}

{linea("Que de conformidad con lo dispuesto por el Artículo 2260 del código")}
{linea("Civil vigente en el Estado de México, formalizan, por su propio derecho")}
{linea("como Arrendador ALBA EUNICE ARMIJO OGAZON y como Arrendatario")}
{linea(f"{cliente[1]} {cliente[2]}, sujetándose a las siguientes, CLAUSULAS:")}

{linea("La Sra. ALBA EUNICE ARMIJO OGAZON da en arrendamiento. Y la Sr(a).")}
{linea(f"{cliente[1]} {cliente[2]} lo recibe como arrendatario, el Departamento")}
{linea(f"NO.{cliente[0]}")}

{linea(("Ubicado en: callejón Zaragoza s/n, San Juan Chiautla, C.P. 56030."))}

{linea("El arrendatario pagará a la arrendadora a quien sus derechos")}
{linea(f"representan, la suma de $ {cliente[3]}.00 los días {fecha_inicio},")}
{linea("en moneda nacional de curso legal por mensualidad adelantada y dentro")}
{linea("de los cinco días que corresponda acuerdo con el contrato establecido,")}
{linea("precisar en el domicilio del arrendador.")}

{linea((f"El presente contrato da inicio el {fecha_inicio} y vence el {fecha_fin}."))}

{linea("1.- Conviene expresamente el arrendatario, en que todo mes será pagado")}
{linea("integro aun cuando no se use, más que por un día.")}

{linea(f"2.- El arrendamiento será de ${cliente[3]} mensual ({costo_letras} pesos)")}

{linea("3.- Al terminar el tiempo por el que ha sido contratado el")}
{linea("arrendamiento, el arrendatario se obliga a desocupar el departamento y")}
{linea("si por circunstancias determinadas no pudiera hacerlo, se obliga a pagar")}
{linea(f"la cantidad ${cliente[3]}.00, equivalente a un mes hasta que lo")}
{linea("desocupen o firmen nuevo contrato.")}

{linea("4.- Les es absolutamente prohibido al arrendatario, subarrendar,")}
{linea("traspasar o ceder sus derechos de inquilino a cualquier persona.")}

{linea("5.- El Arrendatario no podrá usar el departamento, más que para")}
{linea("*Vivienda, descanso, aseo personal. Y bajo ninguna circunstancia para")}
{linea("uso comercial como: Vender alimentos, bebidas, sustancias por mencionar")}
{linea("algunos es exclusivo para uso personal.*")}

{linea("6.- El arrendatario hace expreso reconocimiento, de que el local motivo")}
{linea("de este contrato lo recibe a su entera satisfacción en perfecto estado")}
{linea("de conservación y aseo, con sus instalaciones sanitarias y de")}
{linea("electricidad domestica completas y en condiciones normales de servicio,")}
{linea("comprometiéndose a conservarlas en igual estado, haciendo por su cuenta")}
{linea("las reparaciones que se originen en los servicios a que se refiere esta")}
{linea("cláusula , hasta devolver el local con solo natural deterioro de uso")}
{linea("correcto.")}

{linea("7.- Toda clase de mejoras, ya sean útiles o necesarias, serán por cuenta")}
{linea("del arrendatario, sin que pueda retirarlas al desocuparlo, ni exigir")}
{linea("pago o indemnización por ellas.")}

{linea("8.- Las mensualidades de renta serán pagadas integras, hasta que el")}
{linea("arrendatario entregue el departamento de conformidad con lo dispuesto en")}
{linea("el artículo 2283 del código Civil citado, no pudiendo retener por ningún")}
{linea("motivo que el mandato de la autoridad judicial.")}

{linea("9.- Para garantía del cumplimiento de este contrato, lo firma")}
{linea(f"mancomunadamente {cliente[7]} {cliente[8]} como fiador, haciendo solidario de las")}
{linea(f"obligaciones{cliente[1]} {cliente[2]}.")}

{linea("Hasta la fecha en que el departamento haya sido recibido de conformidad")}
{linea("por el arrendador, a cuyo fin el fiador renuncia las disposiciones")}
{linea("contenidas en el capítulo II del Título décimo tercero del repetido")}
{linea("Código Civil.")}

{linea("10.- Es importante que al dejar el departamento se avise con un mínimo")}
{linea("de 15 días, de no haber cumplido con el tiempo estipulado en este")}
{linea("contrato que se acordó, el depósito no funge como renta, esta garantía")}
{linea("se pierde por incumplimiento del contrato, de cumplir el año y no desea")}
{linea("continuar con el arrendamiento y al avisar con 15 días de anticipación")}
{linea("se recupera el depósito en especie, como renta actuando como el mes 13,")}
{linea("no hacemos devolución en efectivo.")}

{linea("11.- Se anexa Normas de Convivencia")}

{linea("-   Mantener limpio el espacio del Depto.")}
{linea("-   Evitar reuniones de más de 2 personas, en horarios de descanso.")}
{linea("-   No mascotas")}
{linea("-   Anunciar con tiempo alguna falla en los servicios.")}
{linea("-   Formar parte de una comunidad con respeto")}
{linea("-   Evitar visitas desagradables (estado de ebriedad)")}
{linea("-   Informar en caso de estar fuera del departamento durante varios")}
{linea("    días.")}
{linea("-   No prestar llaves a terceras personas (es responsabilidad del")}
{linea("    arrendador el uso de las llaves)")}
{linea("-   Cuidar nuestras salidas y entradas de cerrar bien las puertas")}
{linea("-   Lo anterior es con la finalidad y propósito de la seguridad de")}
{linea("    todos.")}
{linea("-   El uso de la lavadora es para toda la comunidad úsala con")}
{linea("    responsabilidad y respeto sugerimos de 2 a 3 cargas de ropa máximo y")}
{linea("    retirar su ropa el mismo día de lavado ya que los demás pueden usar")}
{linea("    la lavadora y estar ocupado, horario máximo hasta las 6pm.")}

{linea(centrar("INVENTARIO"))}

{linea("-   Llaves")}
{linea("-   Puertas")}
{linea("-   Muebles de baño")}
{linea("-   Instalaciones de electricidad")}
{linea("-   Focos")}
{linea("-   Refrigerador.")}
{linea("-   Escritorio")}
{linea("-   1 silla")}
{linea("-   Parrilla de inducción exterior")}

{linea(f"{espacio_firma}{espacio_firma:>46}")}
{linea(f"{cliente[1]} {cliente[2]:<36}ALBA EUNICE ARMIJO OGAZON")}
{linea(f"Arrendatario{'Arrendador':>53}")}

{linea(("__________________________"))}
{linea((f"{cliente[7]} {cliente[8]} {cliente[9]:>20}"))}
{linea(f"FIADOR {fecha_inicio:>59}")}

"""

    contrato += "\n" * 3  # 3 líneas en blanco al final

    return contrato
