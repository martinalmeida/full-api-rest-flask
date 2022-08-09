<?php
error_reporting(E_ALL);
ini_set('display_errors', '1');
require_once(dirname(__DIR__) . '/cli/php/libraries/rutas.php');
include_once(rutaBase . 'php' . DS . 'includes' . DS . 'template.php');
$usuario = "Admin";
?>
<?= template::verificarSesion() ?>
<?= template::head('Dashboard') ?>
<?= template::startBody($usuario) ?>

<div class="pcoded-content">
    <div class="pcoded-inner-content">
        <div class="main-body">
            <div class="page-wrapper">

                <div class="page-body">
                    <div class="row">




                        <!-- users visite and profile start -->
                        <div class="col-md-4">
                            <div class="card user-card">
                                <div class="card-header">
                                    <h5>Perfil</h5>
                                </div>
                                <div class="card-block">
                                    <div class="usre-image">
                                        <img src="assets/images/avatar-4.jpg" class="img-radius" alt="User-Profile-Image">
                                    </div>
                                    <h6 class="f-w-600 m-t-25 m-b-10">Alessa Robert</h6>
                                    <p class="text-muted">Active | Male | Born 23.05.1992</p>
                                    <hr />

                                    <p class="m-t-15 text-muted">Lorem Ipsum is simply dummy text of the printing and typesetting industry.</p>
                                    <hr />
                                </div>
                            </div>
                        </div>
                        <div class="col-md-8">

                            <div class="col-md-12">
                                <div class="card bg-c-blue order-card">
                                    <div class="card-block">
                                        <h6 class="m-b-20">Orders Received</h6>
                                        <h2 class="text-right"><i class="ti-shopping-cart f-left"></i><span>486</span></h2>
                                        <p class="m-b-0">Completed Orders<span class="f-right">351</span></p>
                                    </div>
                                </div>
                            </div>

                            <div class="col-md-12">
                                <div class="card bg-c-green order-card">
                                    <div class="card-block">
                                        <h6 class="m-b-20">Total Sales</h6>
                                        <h2 class="text-right"><i class="ti-tag f-left"></i><span>1641</span></h2>
                                        <p class="m-b-0">This Month<span class="f-right">213</span></p>
                                    </div>
                                </div>
                            </div>

                        </div>
                        <!-- users visite and profile end -->

                    </div>
                </div>

                <div id="styleSelector">

                </div>
            </div>
        </div>
    </div>
</div>

<?= template::endBody() ?>