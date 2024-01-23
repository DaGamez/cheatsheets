



#en consola
python -m unittest tests/test_album.py

#correr con mayor nivel de detalle
python -m unittest -v tests/test_album.py

#correr todas las pruebas de la carpeta tests
python -m unittest discover -s tests -v

#correr una prueba en especifico
python -m unittest discover -s tests -v -k test_method_one

#ayuda en unittest
python -m unittest -h

HU013 Caso 3: el IMC contine maximo 2 decimales (Rojo)

setUp() #metodo para preparar objetos
tearDown() # capturar las excepciones de los metodos

#metodos mas utilizados https://docs.python.org/3/library/unittest.html

assertEqual(a, b) #: Verifica que los argumentos ‘a' y ‘b' sean iguales.
assertNotEqual(a, b)#: Verifica que los argumentos ‘a' y ‘b' sean diferentes.
assertTrue(x)#: Verifica que el argumento ‘x' sea un valor verdadero. El argumento debe ser de tipo boolean.
assertFalse(x)#: Verifica que el argumento ‘x' sea un valor falso. El argumento debe ser de tipo boolean.
assertIs(a, b)#: Verifica que los argumentos ‘a' y ‘b' sean el mismo objeto.
assertIsNot(a, b)#: Verifica que los argumentos ‘a' y ‘b' no sean el mismo objeto.
assertIsNone(x)#: Verifica que el argumento ‘x' sea un valor None.
assertIsNotNone(x)#: Verifica que el argumento ‘x' no sea un valor None.
assertIn(a, b)#: Verifica que el elemento ‘a' se encuentre contenido en el contenedor o conjunto ‘b'. El elemento ‘b' debe ser un contenedor o conjunto.
assertNotIn(a, b)#: Verifica que el elemento ‘a' no se encuentre contenido en el contenedor o conjunto ‘b'. El elemento ‘b' debe ser un contenedor o conjunto.
assertIsInstance(a, b)#: Verifica que el objeto ‘a' sea una instancia de la clase ‘b'.
assertNotIsInstance(a, b)#: Verifica que el objeto ‘a' no sea una instancia de la clase ‘b'.


#coverage
coverage run -m unittest discover -s tests -v
coverage report -m
coverage html

crear_rama_release.yml

#datos falsos aleatorios---------------------------------------------------------------------------------------------
pip install faker
from faker import Faker
import random





