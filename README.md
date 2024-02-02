# Tarea Data Engineering

Proyecto de analisis de data con una url de coingecko

## Tabla de Contenidos

- [Requisitos](#Requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Licencia](#licencia)

## Requisitos
Se necesita setear variables en airflow (Admin -> Variables)

Las variables necesarias para hacer la conexion a la base de datos: 
    db_name="Nombre de tu base de datos"
    username="Usuario"
    password="Contraseña"
    table_name = "Nombre de tu tabla"

Las variables necesario para el envio de mensajes por correo:
    senderEmail = "Correo del emisor"        
    senderPasswordEmail = "Contraseña de emisor"
    receiberEmail = "Correo del receptor"
    subjectMessaje = "Asunto del mensaje"
    bodyMessaje = "Cuerpo del mensaje"

Para obtener la contraseña del emisor:
1) Se debe activar la utenticacion de 2 pasos
2) Debes ir a la sección de aplicaciones
3) Genera una contraseña y esta sera tu "contraseña de emisor"

## Instalación

Ejecutar "docker-compose-up"

## Uso

Analisis de las mejoras criptomonedas

## Licencia

Libre
