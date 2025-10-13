// import mongoose
const mongoose = require('mongoose');
require('dotenv').config({ path: __dirname + '/.env' });

// Desestructuración de variables de entorno para mayor limpieza
const {
    MONGO_USER,
    MONGO_PASSWORD,
    MONGO_CLUSTER,
    MONGO_DATABASE,
    MONGO_RETRY_WRITES = 'true',
    MONGO_W = 'majority'
} = process.env;

// Validación de variables requeridas
const validateEnvVars = () => {
    const requiredVars = ['MONGO_USER', 'MONGO_PASSWORD', 'MONGO_CLUSTER', 'MONGO_DATABASE'];
    const missingVars = requiredVars.filter(varName => !process.env[varName]);
    
    if (missingVars.length > 0) {
        throw new Error(`Faltan las siguientes variables de entorno: ${missingVars.join(', ')}`);
    }
};

const connection = async () => {
    try {
        // Validar variables antes de conectar
        validateEnvVars();
        
        // Construir la URI de conexión
        const mongoURI = `mongodb+srv://${MONGO_USER}:${MONGO_PASSWORD}@${MONGO_CLUSTER}/${MONGO_DATABASE}?retryWrites=${MONGO_RETRY_WRITES}&w=${MONGO_W}`;
        
        // Conectar sin las opciones deprecated
        await mongoose.connect(mongoURI);

        console.log('✅ Conexión a la base de datos establecida');

    } catch (error) {
        console.error('Error al conectar a la base de datos:', error.message);
        throw new Error("No se pudo conectar a la base de datos");
    }
};

module.exports = connection;
