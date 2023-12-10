Sistema de control de cuentas bancarias

Un Banco desea automatizar el control de cuentas bancarias. De las cuentas en general se
conoce el número de cuenta, los datos del cliente, los datos del comercial que realizó la
apertura de la cuenta, el saldo, el tipo de moneda (que puede ser CUP, CUC, USD o EUR),
la fecha en que se abrió y la fecha en que se retiró la última vez. Además, se conoce que
existen cuentas de formación de fondos de las cuales se conoce que tienen una cuota de
incremento mensual que va a la cuenta directamente del salario de la persona; y que existen
cuentas de plazo fijo que tienen un plazo dado en años que cuyo interés es superior al resto
de las cuentas siempre que no se hagan extracciones en el plazo fijado. Por otro lado, del
cliente se registra el nombre, el sexo, el carné de identidad, el centro de trabajo, la ocupación
y el salario mensual. De los comerciales se registra el nombre, el sexo, el carné de identidad
y los años de experiencia de trabajo en el banco. El sistema cuenta con una lista de cuentas,
una lista de clientes y una lista de comerciales.
El sistema debe permitir realizar las siguientes funcionalidades:
a) Implemente la funcionalidad necesaria para abrir (crear) y cerrar (eliminar) cuentas
bancarias; además debe permitir listar los datos de las cuentas de cada tipo de manera
independiente, así como gestionar (insertar, actualizar, eliminar y listar) los datos de los
clientes y los comerciales.
b) Implemente la funcionalidad necesaria para calcular el interés de una cuenta dado su
número, teniendo en cuenta que este se calcula de la siguiente forma:
* Para las cuentas simples el interés es de 4% por cada peso por año sin extraer.
* Para las cuentas de formación de fondo es de 6% por cada peso por año sin extraer.
* Para las cuentas de plazo fijo es de 8% por cada peso el primer año y aumenta 2%
por cada peso por año de plazo fijo hasta los 5 años, que sería 16%.
c) Implemente la funcionalidad necesaria para hacer un depósito en una cuenta dado el
número de la cuenta y el valor a depositar actualizando el saldo de la cuenta, tenga en cuenta
que antes de cada depósito se calcula el interés a la cuenta y se le suma si no es a plazo fijo.
d) Implemente la funcionalidad necesaria para determinar a cuánto asciende el interés de
todas las cuentas de plazo fijo que hay creadas en una fecha dada dentro de los próximos 5
años.
e) Implemente la funcionalidad necesaria para determinar los datos del propietario de la
cuenta de mayor saldo estimado en este momento teniendo en cuenta que para estimar el
saldo hay que tener en cuenta el interés acumulado.
f) Implemente la funcionalidad necesaria para determinar el listado los datos de las cuentas
de plazo fijo de más de 10000 CUP que sean de un plazo dado y que se muestre el interés
acumulado, ordenado ascendentemente por el número de la cuenta.
g) Pruebe que las operaciones implementadas en el modelo funcionan correctamente según
los datos de prueba que usted le entró al programa.
