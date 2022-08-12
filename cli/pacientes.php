<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
require_once(dirname(__DIR__) . '/cli/php/libraries/rutas.php');
include_once(rutaBase . 'php' . DS . 'includes' . DS . 'template.php');
$usuario = "Admin";
?>
<?= template::verificarSesion() ?>
<?= template::head('Pacientes') ?>
<?= template::startBody($usuario) ?>

<div class="pcoded-content">
    <div class="pcoded-inner-content">
        <!-- Main-body start -->
        <div class="main-body">
            <div class="page-wrapper">
                <!-- Page-header start -->
                <div class="page-header card">
                    <div class="card-block">
                        <h5 class="m-b-10">Bootstrap Basic Tables</h5>
                        <p class="text-muted m-b-10">lorem ipsum dolor sit amet, consectetur adipisicing elit</p>


                        <!-- Button trigger modal -->
                        <button type="button" id="btnmodal_paciente" class="btn btn-primary" data-toggle="modal">
                            Agregar Nuevo Paciente
                        </button>
                        <!-- Button trigger modal END -->


                        <p class="text-muted m-b-10"></p>
                        <ul class="breadcrumb-title b-t-default p-t-10">
                            <li class="breadcrumb-item">
                                <a href="index.html"> <i class="fa fa-home"></i> </a>
                            </li>
                            <li class="breadcrumb-item"><a href="#!">Basic Componenets</a>
                            </li>
                            <li class="breadcrumb-item"><a href="#!">Bootstrap Basic Tables</a>
                            </li>
                        </ul>
                    </div>
                </div>
                <!-- Page-header end -->

                <!-- Page-body start -->
                <div class="page-body">
                    <!-- Basic table card start -->
                    <div class="card">
                        <div class="card-header">
                            <h5>Basic table</h5>
                            <span>use class <code>table</code> inside table element</span>
                            <div class="card-header-right">
                                <ul class="list-unstyled card-option">
                                    <li><i class="fa fa-chevron-left"></i></li>
                                    <li><i class="fa fa-window-maximize full-card"></i></li>
                                    <li><i class="fa fa-minus minimize-card"></i></li>
                                    <li><i class="fa fa-refresh reload-card"></i></li>
                                    <li><i class="fa fa-times close-card"></i></li>
                                </ul>
                            </div>
                        </div>
                        <div class="card-block table-border-style">
                            <div class="table-responsive">
                                <table class="table">
                                    <thead>
                                        <tr>
                                            <th>ID</th>
                                            <th>Nombre</th>
                                            <th>Apellido</th>
                                            <th>Tipo Documento</th>
                                            <th>Documento</th>
                                            <th>Fecha de Nacimiento</th>
                                            <th>Celular</th>
                                            <th>Whatsapp</th>
                                            <th>Usuario</th>
                                            <th>Estado</th>
                                            <th>Editar</th>
                                            <th>Eliminar</th>
                                        </tr>
                                    </thead>
                                    <tbody id="tabla_paciente">



                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                    <!-- Basic table card end -->



                    <!-- Modal -->
                    <div class="modal fade" id="modal_paciente" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                        <div class="modal-dialog" role="document">
                            <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                        <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">

                                    <!-- Form Modal -->
                                    <form id="formulario_paciente">
                                        <div class="form-row">
                                            <div class="form-group col-md-6">
                                                <label for="Nombre">Nombre</label>
                                                <input type="text" class="form-control" name="nombre_paciente" id="nombre_paciente" placeholder="Nombre">
                                            </div>
                                            <div class="form-group col-md-6">
                                                <label for="Apellido">Apellido</label>
                                                <input type="text" class="form-control" name="apellido_paciente" id="apellido_paciente" placeholder="Apellido">
                                            </div>
                                        </div>
                                        <div class="form-row">
                                            <div class="form-group col-md-6">
                                                <label for="Tipo de Documento">Tipo de Documento</label>
                                                <select name="tipo_documento_paciente" id="tipo_documento_paciente" class="form-control">
                                                    <option selected>Cedula</option>
                                                    <option selected>Pasaporte</option>
                                                    <option selected>Tarjeta de Identidad</option>
                                                    <option selected>...</option>
                                                </select>
                                            </div>
                                            <div class="form-group col-md-6">
                                                <label for="Numero de Documento">Numero de Documento</label>
                                                <input type="number" class="form-control" name="numero_documento_paciente" id="numero_documento_paciente" placeholder="Numero de Documento">
                                            </div>
                                        </div>
                                        <div class="form-row">
                                            <div class="form-group col-md-6">
                                                <label for="Fecha de Nacimiento">Fecha de Nacimiento</label>
                                                <input type="date" class="form-control" name="fecha_nacimiento_paciente" id="fecha_nacimiento_paciente" placeholder="Fecha de Nacimiento">
                                            </div>
                                            <div class="form-group col-md-6">
                                                <label for="Telefono">Telefono</label>
                                                <input type="number" class="form-control" name="telefono_paciente" id="telefono_paciente" placeholder="Telefono">
                                            </div>
                                        </div>
                                        <div class="form-row">
                                            <div class="form-group col-md-6">
                                                <label for="Usuario">Usuario</label>
                                                <input type="text" class="form-control" name="usuario_paciente" id="usuario_paciente" placeholder="Usuario">
                                            </div>
                                            <div class="form-group col-md-6">
                                                <label for="Estado">Estado</label>
                                                <input type="text" class="form-control" name="estado_paciente" id="estado_paciente" placeholder="Estado">
                                            </div>
                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Cancelar</button>
                                            <button type="submit" class="btn btn-primary">Save changes</button>
                                        </div>
                                    </form>
                                    <!-- Form Modal END -->

                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- Modal End -->

                </div>
                <!-- Page-body end -->
            </div>
        </div>
        <!-- Main-body end -->

        <div id="styleSelector">

        </div>
    </div>
</div>
<?= template::endBody() ?>