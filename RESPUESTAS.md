## Fase 3

1. ¿Qué es `origin`?
   `origin` es el nombre por defecto del repositorio remoto de GitHub al que está conectado mi proyecto local. Es un atajo para no escribir la URL entera al subir o bajar cambios.

2. Explica con tus palabras la diferencia entre commit y push.
   Un commit guarda los cambios en el historial de mi ordenador, solo en local. Un push envía esos commits a GitHub. Puedo hacer varios commits y subirlos juntos con un solo push.
## Fase 5

1. ¿Qué ventaja tiene trabajar en una rama en lugar de directamente en main?
   Puedo probar una funcionalidad sin tocar el código estable de main. Si sale mal, borro la rama y no pasa nada. Si sale bien, la fusiono.

2. ¿Qué es una fusión fast-forward y por qué se ha producido aquí?
   Es cuando Git fusiona solo moviendo main hacia delante, sin crear un commit de merge. Se produjo porque en main no hubo cambios mientras trabajaba en la rama, así que el historial quedó en línea recta.

## Fase 6

1. ¿Por qué Git no pudo fusionar automáticamente esta vez y sí en la fase 5?
   Porque las dos ramas cambiaron la misma línea de forma distinta y Git no sabe cuál versión es la correcta. En la fase 5 solo cambió una rama, así que no había nada que comparar.

2. ¿Qué habría pasado si hubieras pulsado Accept Theirs?
   Se habría quedado la versión de feature/formato (Nota media con un decimal) y se habría perdido mi cambio de main (Media del grupo). El conflicto desaparecería, pero no estaría la línea combinada que pide la práctica.

## Fase 7

1. En un equipo, ¿por qué conviene hacer Update Project antes de empezar a trabajar cada día?
   Porque otras personas pueden haber subido cambios a GitHub mientras yo no estaba. Si trabajo sobre una copia vieja, luego tendré conflictos al subir mis cambios. Actualizar primero me deja partir del código más reciente.