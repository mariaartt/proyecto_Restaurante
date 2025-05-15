import cx_Oracle

password = "1234"

try:
    # Intentar con el usuario C##RAMOS
    cx_Oracle.connect("C##RAMOS", password, "localhost/XE")
    db_user = "C##RAMOS"
except cx_Oracle.DatabaseError:
    # Si falla, usar C##MARIA
    db_user = "C##MARIA"

db_password = password