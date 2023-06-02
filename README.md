# Dani Shop

Este proyecto utiliza las siguientes tecnologías:
* Python
* Django
* Django Rest Framework
* Celery
* Redis
* Swagger
* OAuth2

Este proyecto está dockerizado, por lo que una vez clonado y estándo posicionado en la raiz del proyecto puede crear los contenedores con el siguiente comando:
> docker-compose up

Esto nos creará las imágenes y levantará los contenedores correspondientes, si queremos al contenedor principal podemos ejecutar el siguiente comando:
> docker exec -ti dani_shop_web bash

El proyecto hace uso de los bots de Landbot, y para hacer posible la comunicación se con el bot se debe de exponer el proyecto mediante Ngrok utilizando:
> ./ngrok http 8000

Con esto conseguiremos una url que utilizaremos para configurar las peticiones realizadas desde Landbot a nuestros endpoints (url de ejemplo -> https://1d42-88-17-117-240.ngrok.io)

# Configuración del proyecto

Además de la configuración de Landbot deberá cubrir los siguientes datos incluidos en settings.py:

* EMAIL_HOST_USER -> Dirección de correo utilizada para enviar los emails 
* EMAIL_HOST_PASSWORD -> Contraseña de la dirección de correo
* EMAIL_TO_ASSISTANCE -> Email que recibirá los correos de asistencia
* TELEGRAM_TOKEN -> Token del bot de Telegram
* TELEGRAM_CHAT_ID -> ID del chat al que se envían los mensajes de Telegram

Para que pueda utilizar el email debe de habilitar las opciones en su proveedor, por ejemplo en gmail serían las de "Acceso de aplicaciones poco seguras"
Y para crear un bot de Telegram puede seguir el siguiente enlace: https://core.telegram.org/bots#6-botfather

# Ejecutar tests

Una vez dentro del contenedor podemos lanzar los tests unitarios con el siguiente comando:
> python3 /opt/dani_shop/dani_shop/manage.py test register_bot

Esto ejecuta el test ubicado en el directorio '/opt/dani_shop/dani_shop/register_bot/tests/'.

# Principales características del proyecto

Dentro del proyecto se han creado dos apps con diferentes finalidades: register_bot y assistance_bot.

La app de register_bot nos permite recibir información desde una bot de Landbot que recabará los datos necesarios y llamará al endpoint utilizando un token de OAuth2. Una vez creado el usuario se ejecutará de manera asíncrona el envío al email de un correo de bienvenida justo 1 minuto después.

Por otro lado la app de assistance_bot nos permitirá recibir preguntas sobre diferentes temáticas. Estas preguntas son registradas con un bot de Landbot que sigue el mismo proceso que el comentado previamente, y que al recibirse se enviarán a los canales configurados para los diferentes temas (Email y/o Telegram)

Los endpoints se pueden ver en detalle en la url: http://localhost:8000/swagger/

# Otros detalles

Al crear los contenedores se cargarán automáticamente una serie de fixtures con los datos mínimos de usuarios, applicación de OAuth2, Token de OAuth2, Topics y Channels. Esta es una información mínima para poder probar el proyecto lo antes posible.

Si deseas añadir más canales a la app de assistance_bot, o crear nuevos topics, podrás utilizar el apartado de admin. Ten en cuenta que deberás de indicar el nombre de la función que corresponda para el canal y que los Topics se deben de añadir también en el bot de Landbot.

Datos de usuarios del fixture:
* admin / 123456
* api_user / EJH2y8dBMCvfVq2W

