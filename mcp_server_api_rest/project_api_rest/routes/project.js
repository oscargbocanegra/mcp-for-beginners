//definir las rutas
const express = require('express');
const router = express.Router();
//cargar el controlador
const ProjectController = require('../controllers/project');

//definir las rutas
router.post('/save', ProjectController.save);
router.get('/list', ProjectController.list);
router.get('/item/:id', ProjectController.item);
router.delete('/delete/:id', ProjectController.deleteProject);
router.put('/update', ProjectController.update);

//exportar la configuración
module.exports = router;