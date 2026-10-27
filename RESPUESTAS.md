

## Fase 1

1. ¿Para qué sirven user.name y user.email? ¿Dónde aparecerán más adelante?
   Sirven para que cada commit lleve mi nombre y mi correo como autor. Aparecen en el Log de PyCharm, en el Git Blame y en GitHub, junto a cada commit. El correo debe ser el de mi cuenta para que GitHub me lo asocie.

2. ¿Por qué GitHub no permite usar la contraseña de la cuenta para subir código por HTTPS?
   Porque con la contraseña se accede a toda la cuenta y es más fácil de robar. Un token o el login por navegador se puede limitar y revocar sin cambiar la contraseña.

## Fase 2

1. ¿Por qué no se debe subir la carpeta .venv al repositorio?
   Pesa mucho y se puede volver a crear en cualquier equipo. Además depende de mi ordenador y no es código mío.

2. ¿Qué significaba el color rojo antes del commit? ¿Y qué color tendría un archivo modificado después?
   El rojo significa que Git ve el archivo pero aún no lo sigue. Después del commit, un archivo modificado sale en azul.

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

## Fase 9

1. ¿Qué diferencia hay entre Pop y Apply al recuperar un stash?
   Pop aplica los cambios guardados y borra el stash de la lista. Apply los aplica pero deja el stash guardado, por si lo quiero usar otra vez.