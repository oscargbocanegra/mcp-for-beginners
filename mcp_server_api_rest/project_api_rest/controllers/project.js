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


const item = (req, res) => {

    let id = req.params.id;

    Project.findById(id)
        .then(project => {

            if (!project) {
                return res.status(404).send({
                    status: 'error',
                    message: 'No existe el proyecto'
                });
            }

            return res.status(200).send({
                status: 'success',
                project
            })
        }).catch(error => {
            return res.status(500).send({
                status: 'error',
                message: 'Error al devolver los datos'
            });
        })
}


const deleteProject = (req, res) => {

    let id = req.params.id;

    Project.findByIdAndDelete(id)
        .then(project => {

            if (!project) {
                return res.status(404).send({
                    status: 'error',
                    message: 'No se haborrado el proyecto'
                });
            }

            return res.status(200).send({
                status: 'success',
                project
            })
        }).catch(error => {
            return res.status(500).send({
                status: 'error',
                message: 'Error al eliminar los datos'
            });
        })
}


const update = (req, res) => {

    let body = req.body;

    if (!body || !body.id) {
        return res.status(404).send({
            status: 'error',
            message: 'Faltan datos por enviar'
        });
    }

    Project.findByIdAndUpdate(body.id, body, { new: true })
        .then(projectUpdated => {

            if (!projectUpdated) {
                return res.status(404).send({
                    status: 'error',
                    message: 'No existe el proyecto'
                });
            }

            return res.status(200).send({
                status: 'success',
                project: projectUpdated
            });


        }).catch(error => {
            return res.status(500).send({
                status: 'error',
                message: 'Error al actualizar el proyecto'
            });
        })
}

module.exports = {
    save,
    list,
    item,
    deleteProject,
    update
};