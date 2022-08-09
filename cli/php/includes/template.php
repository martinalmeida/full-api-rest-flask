<?php

class template
{

    static public function verificarSesion()
    {
        // $usuario = sesion::getparametro('usuario');
        // if ($usuario == '') {
        //     header('Location: login.php', true);
        //     exit;
        // }
    }

    static public function head($title)
    {
        ob_start();
?>
        <!DOCTYPE html>
        <html lang="en">

        <head>
            <title><?= $title ?></title>
            <!-- Meta -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0, minimal-ui">
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="description" content="Gradient Able Bootstrap admin template made using Bootstrap 4. The starter version of Gradient Able is completely free for personal project." />
            <meta name="keywords" content="free dashboard template, free admin, free bootstrap template, bootstrap admin template, admin theme, admin dashboard, dashboard template, admin template, responsive" />
            <meta name="author" content="codedthemes">
            <!-- Favicon icon -->
            <link rel="icon" href="assets/images/favicon.ico" type="image/x-icon">
            <!-- Google font-->
            <link href="https://fonts.googleapis.com/css?family=Open+Sans:400,600" rel="stylesheet">
            <!-- Required Fremwork -->
            <link rel="stylesheet" type="text/css" href="assets/css/bootstrap/css/bootstrap.min.css">
            <!-- themify-icons line icon -->
            <link rel="stylesheet" type="text/css" href="assets/icon/themify-icons/themify-icons.css">
            <link rel="stylesheet" type="text/css" href="assets/icon/font-awesome/css/font-awesome.min.css">
            <!-- ico font -->
            <link rel="stylesheet" type="text/css" href="assets/icon/icofont/css/icofont.css">
            <!-- Style.css -->
            <link rel="stylesheet" type="text/css" href="assets/css/style.css">
            <link rel="stylesheet" type="text/css" href="assets/css/jquery.mCustomScrollbar.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
        </head>

        <body>
        <?php
        return ob_get_clean();
    }

    static public function startBody($usuario)
    {
        ob_start();
        ?>

            <!-- Pre-loader start -->
            <div class="theme-loader">
                <div class="loader-track">
                    <div class="loader-bar"></div>
                </div>
            </div>
            <!-- Pre-loader end -->
            <div id="pcoded" class="pcoded">
                <div class="pcoded-overlay-box"></div>
                <div class="pcoded-container navbar-wrapper">

                    <nav class="navbar header-navbar pcoded-header">
                        <div class="navbar-wrapper">
                            <div class="navbar-logo">
                                <a class="mobile-menu" id="mobile-collapse" href="#!">
                                    <i class="ti-menu"></i>
                                </a>
                                <div class="mobile-search">
                                    <div class="header-search">
                                        <div class="main-search morphsearch-search">
                                            <div class="input-group">
                                                <span class="input-group-addon search-close"><i class="ti-close"></i></span>
                                                <input type="text" class="form-control" placeholder="Enter Keyword">
                                                <span class="input-group-addon search-btn"><i class="ti-search"></i></span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <a href="./inicio">
                                    OPTICA SAN ANGEL <i class="fa-solid fa-glasses"></i>
                                </a>
                                <a class="mobile-options">
                                    <i class="ti-more"></i>
                                </a>
                            </div>

                            <div class="navbar-container container-fluid">
                                <ul class="nav-left">
                                    <li>
                                        <div class="sidebar_toggle"><a href="javascript:void(0)"><i class="ti-menu"></i></a></div>
                                    </li>
                                    <li class="header-search">
                                        <div class="main-search morphsearch-search">
                                            <div class="input-group">
                                                <span class="input-group-addon search-close"><i class="ti-close"></i></span>
                                                <input type="text" class="form-control">
                                                <span class="input-group-addon search-btn"><i class="ti-search"></i></span>
                                            </div>
                                        </div>
                                    </li>
                                    <li>
                                        <a href="#!" onclick="javascript:toggleFullScreen()">
                                            <i class="ti-fullscreen"></i>
                                        </a>
                                    </li>
                                </ul>
                                <ul class="nav-right">

                                    <li class="user-profile header-notification">
                                        <a href="#!">
                                            <i class="fa-solid fa-user fa-2x"></i>
                                            <span><?= $usuario ?></span>
                                            <i class="ti-angle-down"></i>
                                        </a>
                                        <ul class="show-notification profile-notification">
                                            <li>
                                                <a href="auth-normal-sign-in.html">
                                                    <i class="ti-layout-sidebar-left"></i> Salir
                                                </a>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </nav>
                    <div class="pcoded-main-container">
                        <div class="pcoded-wrapper">
                            <nav class="pcoded-navbar">
                                <div class="sidebar_toggle"><a href="#"><i class="icon-close icons"></i></a></div>
                                <div class="pcoded-inner-navbar main-menu">

                                    <div class="pcoded-navigatio-lavel" data-i18n="nav.category.navigation">Principal</div>
                                    <ul class="pcoded-item pcoded-left-item">
                                        <li class="active">
                                            <a href="./inicio">
                                                <span class="pcoded-micon"><i class="ti-home"></i>I</span>
                                                <span class="pcoded-mtext" data-i18n="nav.dash.main">Inicio</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>

                                        <li>
                                            <a href="./pacientes">
                                                <span class="pcoded-micon"><i class="ti-layers"></i><b>P</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.form-components.main">Pacientes</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>

                                        <li>
                                            <a href="./historias">
                                                <span class="pcoded-micon"><i class="ti-layers"></i><b>HC</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.form-components.main">Historia Clinica</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>

                                        <li>
                                            <a href="./formulas">
                                                <span class="pcoded-micon"><i class="ti-layers"></i><b>F</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.form-components.main">Formulas</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>

                                    </ul>

                                    <div class="pcoded-navigatio-lavel" data-i18n="nav.category.forms">Contabilidad</div>
                                    <ul class="pcoded-item pcoded-left-item">
                                        <li>
                                            <a href="./cotizacion">
                                                <span class="pcoded-micon"><i class="ti-layers"></i><b>C</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.form-components.main">Cotización</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>
                                        <li>
                                            <a href="./facturas">
                                                <span class="pcoded-micon"><i class="ti-layers"></i><b>F</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.form-components.main">Facturas</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                        </li>

                                    </ul>

                                    <div class="pcoded-navigatio-lavel" data-i18n="nav.category.other">Parametrizacion</div>
                                    <ul class="pcoded-item pcoded-left-item">
                                        <li class="pcoded-hasmenu ">
                                            <a href="javascript:void(0)">
                                                <span class="pcoded-micon"><i class="ti-layout-grid2-alt"></i><b>M</b></span>
                                                <span class="pcoded-mtext" data-i18n="nav.menu-levels.main">Más</span>
                                                <span class="pcoded-mcaret"></span>
                                            </a>
                                            <ul class="pcoded-submenu">
                                                <li class="">
                                                    <a href="javascript:void(0)">
                                                        <span class="pcoded-micon"><i class="ti-angle-right"></i></span>
                                                        <span class="pcoded-mtext" data-i18n="nav.menu-levels.menu-level-21">Menu Level 2.1</span>
                                                        <span class="pcoded-mcaret"></span>
                                                    </a>
                                                </li>
                                                <li class="pcoded-hasmenu ">
                                                    <a href="javascript:void(0)">
                                                        <span class="pcoded-micon"><i class="ti-direction-alt"></i></span>
                                                        <span class="pcoded-mtext" data-i18n="nav.menu-levels.menu-level-22.main">Menu Level 2.2</span>
                                                        <span class="pcoded-mcaret"></span>
                                                    </a>
                                                    <ul class="pcoded-submenu">
                                                        <li class="">
                                                            <a href="javascript:void(0)">
                                                                <span class="pcoded-micon"><i class="ti-angle-right"></i></span>
                                                                <span class="pcoded-mtext" data-i18n="nav.menu-levels.menu-level-22.menu-level-31">Menu Level 3.1</span>
                                                                <span class="pcoded-mcaret"></span>
                                                            </a>
                                                        </li>
                                                    </ul>
                                                </li>
                                                <li class="">
                                                    <a href="javascript:void(0)">
                                                        <span class="pcoded-micon"><i class="ti-angle-right"></i></span>
                                                        <span class="pcoded-mtext" data-i18n="nav.menu-levels.menu-level-23">Menu Level 2.3</span>
                                                        <span class="pcoded-mcaret"></span>
                                                    </a>
                                                </li>

                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </nav>

                        <?php
                        return ob_get_clean();
                    }

                    static public function endBody()
                    {
                        ob_start();
                        ?>
                        </div>
                    </div>
                </div>
                <!-- Warning Section Ends -->
                <!-- Required Jquery -->
                <script type="text/javascript" src="assets/js/jquery/jquery.min.js"></script>
                <script type="text/javascript" src="assets/js/jquery-ui/jquery-ui.min.js"></script>
                <script type="text/javascript" src="assets/js/popper.js/popper.min.js"></script>
                <script type="text/javascript" src="assets/js/bootstrap/js/bootstrap.min.js"></script>
                <!-- jquery slimscroll js -->
                <script type="text/javascript" src="assets/js/jquery-slimscroll/jquery.slimscroll.js"></script>
                <!-- modernizr js -->
                <script type="text/javascript" src="assets/js/modernizr/modernizr.js"></script>
                <!-- am chart -->
                <script src="assets/pages/widget/amchart/amcharts.min.js"></script>
                <script src="assets/pages/widget/amchart/serial.min.js"></script>
                <!-- Chart js -->
                <script type="text/javascript" src="assets/js/chart.js/Chart.js"></script>
                <!-- Todo js -->
                <script type="text/javascript " src="assets/pages/todo/todo.js "></script>
                <!-- Custom js -->
                <script type="text/javascript" src="assets/pages/dashboard/custom-dashboard.min.js"></script>
                <script type="text/javascript" src="assets/js/script.js"></script>
                <script type="text/javascript " src="assets/js/SmoothScroll.js"></script>
                <script src="assets/js/pcoded.min.js"></script>
                <script src="assets/js/vartical-demo.js"></script>
                <script src="assets/js/jquery.mCustomScrollbar.concat.min.js"></script>
        </body>

        </html>

<?php
                        return ob_get_clean();
                    }
                }
