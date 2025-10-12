const Project = require('../models/Project');

const save = (req, res) => {

    // recibir los datos por post a guardar
    let body = req.body;

    // validar los datos
    if (!body.name || !body.description || !body.category || !body.year || !body.state) {
        return res.status(400).send({
            status: 'error',
            message: 'Faltan datos por enviar'
        });
    }

    // crear un objeto de tipo project
    let projectToSave = new Project(body);

    // guardar el project en la base de datos
    projectToSave.save().then(Project => {

        if (!Project) {
            return res.status(400).send({
                status: 'error',
                message: 'El proyecto no se ha guardado'
            });
        }

        // devolver una respuesta
        return res.status(200).send({
            status: 'success',
            project: Project,
            message: 'Proyecto guardado con exito'
        });


    }).catch(error => {
        return res.status(500).send({
            status: 'error',
            message: 'Error al guardar el documento'
        });
    });

}


const list = (req, res) => {

    Project.find()
        .then(projects => {

            if (!projects) {
                return res.status(404).send({
                    status: 'error',
                    message: 'No hay proyectos para mostrar'
                });
            }

            return res.status(200).send({
                status: 'success',
                projects
            });


        }).catch(error => {
            return res.status(500).send({
                status: 'error',
                message: 'Error al devolver los datos'
            });
        });
}






module.exports = { save, list };