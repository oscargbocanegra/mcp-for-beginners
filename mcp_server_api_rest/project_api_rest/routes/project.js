//definir las rutas
const express = require('express');
const router = express.Router();
//cargar el controlador
const ProjectController = require('../controllers/project');

//definir las rutas
router.post('/save', ProjectController.save);
router.get('/list', ProjectController.list);

//exportar la configuración
module.exports = router;