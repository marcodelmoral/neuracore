CREATE TABLE statusProyecto(
    statusProyectoID SERIAL,
    statusProyecto varchar(30),
    PRIMARY KEY (statusProyectoID)
);

CREATE TABLE rol(
    rolID SERIAL,
    rolDescripcion varchar(150),
    PRIMARY KEY (rolID)
);

CREATE TABLE experiencia(
    experienciaID SERIAL,
    experienciaRango varchar(30),
    PRIMARY KEY (experienciaID)
);

CREATE TABLE direccionEspecialistas(
    direccionEspecialistasID SERIAL,
    calles varchar(60),
    numeroInterior varchar(10),
    numeroExterior varchar(10),
    zip varchar(10),
    colonia varchar(30),
    ciudad varchar(30),
    estado varchar(30),
    pais varchar(20),
    PRIMARY KEY (direccionEspecialistasID)
);

CREATE TABLE direccionClientes(
    direccionClientesID SERIAL,
    calles varchar(60),
    numeroInterior varchar(10),
    numeroExterior varchar(10),
    zip varchar(10),
    colonia varchar(30),
    ciudad varchar(30),
    estado varchar(30),
    pais varchar(20),
    PRIMARY KEY (direccionClientesID)
);

CREATE TABLE tipoCliente(
    tipoClienteID SERIAL,
    tipo varchar(50),
    PRIMARY KEY (tipoClienteID)
);

CREATE TABLE profesiones(
    profesionesID SERIAL,
    profesion varchar(40),
    PRIMARY KEY (profesionesID)
);

CREATE TABLE grados(
    gradosID SERIAL,
    grado varchar(40),
    PRIMARY KEY (gradosID)
);

CREATE TABLE servicios(
    serviciosID SERIAL,
    serviciosNombre varchar(50),
    serviciosDescripcion varchar(150),
    PRIMARY KEY (serviciosID)
);

CREATE TABLE niveles(
    nivelesID SERIAL,
    nivelNombre varchar(30),
    PRIMARY KEY (nivelesID)
);

CREATE TABLE status(
    statusID SERIAL,
    statusNombre varchar(30),
    PRIMARY KEY (statusID)
);

CREATE TABLE calificaciones(
    calificacionesID SERIAL,
    calificacionesNombre varchar(30),
    PRIMARY KEY (calificacionesID)
);

CREATE TABLE especialistas(
    especialistasID SERIAL,
    especialistasLogin varchar(50),
    especialistasPass varchar(50), 
    especialistasNombre varchar(50),
    especialistasNacimiento date,
    especialistasProfesion int,
    especialistasExperiencia int,
    especialistasNivel int,
    especialistasDireccion int,
    especialistasGrado int,
    especialistasTelefono varchar(30),
    especialistasRol int,
    PRIMARY KEY (especialistasID),
    FOREIGN KEY (especialistasProfesion) REFERENCES profesiones(profesionesID),
    FOREIGN KEY (especialistasNivel) REFERENCES niveles(nivelesID),
    FOREIGN KEY (especialistasDireccion) REFERENCES direccionEspecialistas(direccionEspecialistasID),
    FOREIGN KEY (especialistasGrado) REFERENCES grados(gradosID),
    FOREIGN KEY (especialistasExperiencia) REFERENCES experiencia(experienciaID),
    FOREIGN KEY (especialistasRol) REFERENCES rol(rolID)
);

CREATE TABLE etapas(
    etapasID SERIAL,
    etapasNombre varchar(40),
    etapasDuracion int,
    PRIMARY KEY (etapasID)
);

CREATE TABLE tareas(
    tareasID SERIAL,
    tareasNombre varchar(40),
    tareasDuracion int, 
    PRIMARY KEY (tareasID)
);

CREATE TABLE clientes(
    clientesID SERIAL,
    clientesLogin varchar(50),
    clientesPass varchar(50),
    clientesNombre varchar(50),
    clienteDireccion int,
    clientesCorreo varchar(30),
    clientesTelefono varchar(30),
    clientesTipo int,
    clientesRFC varchar(13),
    clientesNacimiento date,
    PRIMARY KEY (clientesID),
    FOREIGN KEY (clienteDireccion) REFERENCES direccionClientes(direccionClientesID),
    FOREIGN KEY (clientesTipo) REFERENCES tipoCliente(tipoClienteID)
);

CREATE TABLE proyectos(
    proyectoID SERIAL,
    proyectoNombre varchar(40),
    proyectoDescripcion varchar(150),
    proyectoServicio int,
    proyectoDuracion int,
    proyectoEspecialista int,
    proyectoCliente int,
    proyectoStatus int,
    proyectoCalificacion int,
    proyectoInicio date,
    proyectoFinal date,    
    PRIMARY KEY (proyectoID),
    FOREIGN KEY (proyectoServicio) REFERENCES servicios(serviciosID),
    FOREIGN KEY (proyectoEspecialista) REFERENCES especialistas(especialistasID),
    FOREIGN KEY (proyectoCliente) REFERENCES clientes(clientesID),
    FOREIGN KEY (proyectoStatus) REFERENCES statusProyecto(statusProyectoID), 
    FOREIGN KEY (proyectoCalificacion) REFERENCES calificaciones(calificacionesID) 
);

CREATE TABLE proyectoDescripcion(
    proyectoID int REFERENCES proyectos(proyectoID),
    etapaProyecto int REFERENCES etapas(etapasID),
    etapaEspecialista int REFERENCES especialistas(especialistasID),
    etapaStatus int REFERENCES status(statusID),
    etapaCalificacion int REFERENCES calificaciones(calificacionesID),
    PRIMARY KEY (proyectoID)
); 

CREATE TABLE etapasTareas(
    etapasTareasID int REFERENCES etapas(etapasID),
    tareasEtapasID int REFERENCES tareas(tareasID),
    tareasEspecialista int REFERENCES especialistas(especialistasID),
    tareasStatus int REFERENCES status(statusID),
    tareasCalificacion int REFERENCES calificaciones(calificacionesID),
    PRIMARY KEY (etapasTareasID, tareasEtapasID)
);