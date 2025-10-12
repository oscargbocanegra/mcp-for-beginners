//importar libreria de mongoose
const {Schema, model } = require('mongoose');
const { trim } = require('validator');
require('dotenv').config({ path: __dirname + '/.env' });

// crear schema (estructura del cada documento de tipo de projecto  en la base de datos)
const ProjectSchema = Schema({
    name: {
        type: String,
        required: true
    },
    description: {
        type: String,
        required: true,
        trim: true
    },
    category: {
        type: String,
        required: true
    },
    state: {
        type: String,
        required: true
    },
    year: {
        type: Number,
        required: true
    },
    image: {
        type: String,
        default: "default.png"
    },
    created_at: {
        type: Date,
        default: Date.now
    }
});


// crear el modelo, indicarle la coleccion donde se van a guardar los documentos
// exportar el modelo
module.exports = model('Project', ProjectSchema, "myprojects");

