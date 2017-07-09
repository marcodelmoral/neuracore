INSERT INTO statusProyecto (statusProyecto) VALUES ('en curso');
INSERT INTO statusProyecto (statusProyecto) VALUES ('en espera');
INSERT INTO statusProyecto (statusProyecto) VALUES ('cancelado');

INSERT INTO tipoCliente (tipo) VALUES ('persona moral');
INSERT INTO tipoCliente (tipo) VALUES ('persona fisica');
INSERT INTO tipoCliente (tipo) VALUES ('emprendedor');

INSERT INTO profesiones (profesion) VALUES ('disenador grafico');
INSERT INTO profesiones (profesion) VALUES ('disenador industrial');
INSERT INTO profesiones (profesion) VALUES ('desarrollador web front end');

INSERT INTO grados (grado) VALUES ('licenciado');
INSERT INTO grados (grado) VALUES ('master');
INSERT INTO grados (grado) VALUES ('doctor');

INSERT INTO servicios (serviciosNombre, serviciosDescripcion) VALUES ('branding', 'genera marcas');
INSERT INTO servicios (serviciosNombre, serviciosDescripcion) VALUES ('desarrollo web','genera webs');
INSERT INTO servicios (serviciosNombre, serviciosDescripcion) VALUES ('desarrollo de producto','genera productos');

INSERT INTO niveles (nivelNombre) VALUES ('staff');
INSERT INTO niveles (nivelNombre) VALUES ('coordinador');
INSERT INTO niveles (nivelNombre) VALUES ('master');

INSERT INTO status (statusNombre) VALUES ('en tiempo');
INSERT INTO status (statusNombre) VALUES ('retrasado');
INSERT INTO status (statusNombre) VALUES ('no terminado');

INSERT INTO calificaciones (calificacionesNombre) VALUES ('azul');
INSERT INTO calificaciones (calificacionesNombre) VALUES ('verde');
INSERT INTO calificaciones (calificacionesNombre) VALUES ('naranja');
INSERT INTO calificaciones (calificacionesNombre) VALUES ('rojo');

INSERT INTO etapas (etapasNombre, etapasDuracion) VALUES ('estudio comercial', 2);
INSERT INTO etapas (etapasNombre, etapasDuracion) VALUES ('desarrollo de marca', 2);
INSERT INTO etapas (etapasNombre, etapasDuracion) VALUES ('aplicaciones de marca', 2);
INSERT INTO etapas (etapasNombre, etapasDuracion) VALUES ('entrega final', 2);

INSERT INTO tareas (tareasNombre, tareasDuracion) VALUES ('investigacion sobre marcas registradas', 10);
INSERT INTO tareas (tareasNombre, tareasDuracion) VALUES ('naming', 8);
INSERT INTO tareas (tareasNombre, tareasDuracion) VALUES ('estudio de la competencia', 5);
INSERT INTO tareas (tareasNombre, tareasDuracion) VALUES ('propuesta de colores a logotipo', 7);

INSERT INTO rol (rolDescripcion) VALUES ('nivel 1');
INSERT INTO rol (rolDescripcion) VALUES ('nivel 2');
INSERT INTO rol (rolDescripcion) VALUES ('nivel 3');



