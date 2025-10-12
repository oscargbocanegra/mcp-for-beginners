// importar dependencias.
const connection = require('./database/connection');
const express = require('express');
const cors = require('cors');

//conexion a la base de datos
connection();

// crear el servidor 
const app = express();
const port = 3977;

// configurar el cors
app.use(cors());

// configurar body parser
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// convertir los datos del body a objetos

// cargar rutas
const project_routes = require('./routes/project');
app.use('/api/project', project_routes);

// crear endpoints de pruebas

app.get('/', (req, res) => {

    console.log('Se ha recibido una petición de pruebas');

    return res.status(200).send([
        {
            message: 'Hola mundo desde el servidor de NodeJS',
            url: 'hhtp://localhost:3977/api/test'
        },
        {
            message: 'Hola mundo desde el servidor de NodeJS',
            url: 'hhtp://localhost:3977/api/test'
        }
    ]);
});

app.get('/api/test', (req, res) => {

    console.log('Se ha recibido una petición de pruebas');

    return res.status(200).send(`
        <section>
            <h1>Hola mundo desde el servidor de NodeJS</h1>
            <p>Esta es una página de pruebas</p>
        </section>
    `);
});

// poner el servidor a escuchar en un puerto
app.listen(port, () => {
    console.log(`Servidor corriendo en http://localhost:${port}`);
});