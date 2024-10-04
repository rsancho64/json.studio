# stuff

- [ ] serialización y marshaling

Son sinónimos en contexto RPC (llamadas a procedimientos remotos) pero difieren en la intención.

- **marshaling**: trasladar parámetros.
- **serialización**: traducir datos estructurados 
  - desde o hacia una forma fisica.
    - como un flujo de bytes.
    - de forma reversible.

,, la serialización da soporte al marshaling, normalmente implementando la semántica pass-by-value. 

También es posible que un objeto sea "marshaleado" por referencia, 
,, los datos "en el cable" son locators (ej URLs) 
,, pueden romperse.

puede haber metadatos adicionales como la ubicación de la base de código o incluso el código de implementación del objeto.

- [ ] python complex data to/from json (serializar)

    read [**this**](https://docs.python.org/3/library/json.html)

json: an API familiar: similar a las std lib: marshal and pickle