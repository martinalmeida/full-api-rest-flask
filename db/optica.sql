-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1:3308
-- Tiempo de generación: 18-06-2022 a las 00:16:16
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `optica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agudeza_visual_cc`
--

CREATE TABLE `agudeza_visual_cc` (
  `id` int(11) NOT NULL,
  `ojo_derecho_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_historia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `agudeza_visual_sc`
--

CREATE TABLE `agudeza_visual_sc` (
  `id` int(11) NOT NULL,
  `ojo_derecho_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_vl` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_vp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `ambos_ph` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_historia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cerca`
--

CREATE TABLE `cerca` (
  `id` int(11) NOT NULL,
  `derecho_esfera` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_cilindro` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_eje` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_av` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_esfera` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_cilindro` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_eje` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_av` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_formula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `coti`
--

CREATE TABLE `coti` (
  `id` int(11) NOT NULL,
  `fecha` date NOT NULL,
  `id_lente` int(11) NOT NULL,
  `id_montura` int(11) NOT NULL,
  `valor` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_paciente` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estado`
--

CREATE TABLE `estado` (
  `id_estado` int(11) NOT NULL,
  `estado` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `estado`
--

INSERT INTO `estado` (`id_estado`, `estado`) VALUES
(1, 'activo'),
(2, 'inactivo'),
(3, 'eliminado'),
(4, 'pendiente');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `facturas`
--

CREATE TABLE `facturas` (
  `id` int(11) NOT NULL,
  `fecha_creacion` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `array_productos` longtext COLLATE utf8_spanish_ci NOT NULL CHECK (json_valid(`array_productos`)),
  `id_paciente` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `filtro`
--

CREATE TABLE `filtro` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `formulas`
--

CREATE TABLE `formulas` (
  `id` int(11) NOT NULL,
  `proximo_control` date NOT NULL,
  `vigencia` date NOT NULL,
  `distancia_pupilar` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `id_lente` int(11) NOT NULL,
  `id_filtro` int(11) NOT NULL,
  `observacion` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id_paciente` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `historia_clinica`
--

CREATE TABLE `historia_clinica` (
  `id_historial` int(11) NOT NULL,
  `id_sintomas` int(11) NOT NULL,
  `ojo_derecho_ee` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_ee` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `observacion_reflejos` text COLLATE utf8_spanish_ci NOT NULL,
  `vision_lejana_ct` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `vision_proxima_ct` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `observacion_motilidad` text COLLATE utf8_spanish_ci NOT NULL,
  `observacion_punto` text COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_of` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_of` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_qu` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_qu` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_vc` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vc` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `observacion_este` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `id_paciente` int(11) NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lejos`
--

CREATE TABLE `lejos` (
  `id` int(11) NOT NULL,
  `derecho_esfera` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_cilindro` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_eje` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `derecho_av` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_esfera` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_cilindro` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_eje` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `izquierdo_av` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_formula` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `lente`
--

CREATE TABLE `lente` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `montura`
--

CREATE TABLE `montura` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `paciente`
--

CREATE TABLE `paciente` (
  `id` int(11) NOT NULL,
  `nombres` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `apellidos` varchar(100) COLLATE utf8_spanish_ci NOT NULL,
  `id_documento` int(11) NOT NULL,
  `documento` varchar(20) COLLATE utf8_spanish_ci NOT NULL,
  `fecha_nacimiento` date NOT NULL,
  `celular` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `whatsapp` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `id_usuario` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `refraccion`
--

CREATE TABLE `refraccion` (
  `id` int(11) NOT NULL,
  `ojo_derecho` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_av` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_av` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `id_historia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_rol` int(11) NOT NULL,
  `rol` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_rol`, `rol`) VALUES
(1, 'administrador'),
(2, 'visitante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rx_final`
--

CREATE TABLE `rx_final` (
  `id_rx` int(11) NOT NULL,
  `ojo_derecho_vl` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vl` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_vp` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_vp` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_derecho_add` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `ojo_izquierdo_add` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `id_historia` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sintomas`
--

CREATE TABLE `sintomas` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `descripcion` text COLLATE utf8_spanish_ci NOT NULL,
  `fecha_mod` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tipo_documento`
--

CREATE TABLE `tipo_documento` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `nombre` varchar(50) COLLATE utf8_spanish_ci NOT NULL,
  `paswd` text COLLATE utf8_spanish_ci NOT NULL,
  `rol` int(11) NOT NULL,
  `id_estado` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `nombre`, `paswd`, `rol`, `id_estado`) VALUES
(1, 'Andres El Veneco', '1232344545', 1, 1),
(2, 'Eddier El Pito Chico', '12334433r54', 1, 2);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `agudeza_visual_cc`
--
ALTER TABLE `agudeza_visual_cc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_historia` (`id_historia`);

--
-- Indices de la tabla `agudeza_visual_sc`
--
ALTER TABLE `agudeza_visual_sc`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_historia` (`id_historia`);

--
-- Indices de la tabla `cerca`
--
ALTER TABLE `cerca`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_formula` (`id_formula`);

--
-- Indices de la tabla `coti`
--
ALTER TABLE `coti`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_lente` (`id_lente`),
  ADD KEY `id_montura` (`id_montura`);

--
-- Indices de la tabla `estado`
--
ALTER TABLE `estado`
  ADD PRIMARY KEY (`id_estado`);

--
-- Indices de la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `id_paciente` (`id_paciente`);

--
-- Indices de la tabla `filtro`
--
ALTER TABLE `filtro`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `formulas`
--
ALTER TABLE `formulas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `id_lente` (`id_lente`),
  ADD KEY `id_filtro` (`id_filtro`);

--
-- Indices de la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD PRIMARY KEY (`id_historial`),
  ADD KEY `id_sintomas` (`id_sintomas`),
  ADD KEY `id_paciente` (`id_paciente`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_estado` (`id_estado`);

--
-- Indices de la tabla `lejos`
--
ALTER TABLE `lejos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_formula` (`id_formula`);

--
-- Indices de la tabla `lente`
--
ALTER TABLE `lente`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `montura`
--
ALTER TABLE `montura`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_usuario` (`id_usuario`),
  ADD KEY `id_estado` (`id_estado`),
  ADD KEY `id_documento` (`id_documento`);

--
-- Indices de la tabla `refraccion`
--
ALTER TABLE `refraccion`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_historia` (`id_historia`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_rol`);

--
-- Indices de la tabla `rx_final`
--
ALTER TABLE `rx_final`
  ADD PRIMARY KEY (`id_rx`),
  ADD KEY `id_historia` (`id_historia`);

--
-- Indices de la tabla `sintomas`
--
ALTER TABLE `sintomas`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`),
  ADD KEY `rol` (`rol`),
  ADD KEY `id_estado` (`id_estado`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `agudeza_visual_cc`
--
ALTER TABLE `agudeza_visual_cc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `agudeza_visual_sc`
--
ALTER TABLE `agudeza_visual_sc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cerca`
--
ALTER TABLE `cerca`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `coti`
--
ALTER TABLE `coti`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `estado`
--
ALTER TABLE `estado`
  MODIFY `id_estado` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `facturas`
--
ALTER TABLE `facturas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `filtro`
--
ALTER TABLE `filtro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `formulas`
--
ALTER TABLE `formulas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  MODIFY `id_historial` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lejos`
--
ALTER TABLE `lejos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `lente`
--
ALTER TABLE `lente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `montura`
--
ALTER TABLE `montura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `paciente`
--
ALTER TABLE `paciente`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `refraccion`
--
ALTER TABLE `refraccion`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rx_final`
--
ALTER TABLE `rx_final`
  MODIFY `id_rx` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `sintomas`
--
ALTER TABLE `sintomas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tipo_documento`
--
ALTER TABLE `tipo_documento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `agudeza_visual_cc`
--
ALTER TABLE `agudeza_visual_cc`
  ADD CONSTRAINT `agudeza_visual_cc_ibfk_1` FOREIGN KEY (`id_historia`) REFERENCES `historia_clinica` (`id_historial`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `agudeza_visual_sc`
--
ALTER TABLE `agudeza_visual_sc`
  ADD CONSTRAINT `agudeza_visual_sc_ibfk_1` FOREIGN KEY (`id_historia`) REFERENCES `historia_clinica` (`id_historial`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `cerca`
--
ALTER TABLE `cerca`
  ADD CONSTRAINT `cerca_ibfk_1` FOREIGN KEY (`id_formula`) REFERENCES `formulas` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `coti`
--
ALTER TABLE `coti`
  ADD CONSTRAINT `coti_ibfk_2` FOREIGN KEY (`id_montura`) REFERENCES `montura` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `coti_ibfk_3` FOREIGN KEY (`id_lente`) REFERENCES `lente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `coti_ibfk_4` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `coti_ibfk_5` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `facturas`
--
ALTER TABLE `facturas`
  ADD CONSTRAINT `facturas_ibfk_1` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `facturas_ibfk_3` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `facturas_ibfk_4` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `formulas`
--
ALTER TABLE `formulas`
  ADD CONSTRAINT `formulas_ibfk_1` FOREIGN KEY (`id_lente`) REFERENCES `lente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `formulas_ibfk_2` FOREIGN KEY (`id_filtro`) REFERENCES `filtro` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `formulas_ibfk_4` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `formulas_ibfk_5` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `formulas_ibfk_6` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `historia_clinica`
--
ALTER TABLE `historia_clinica`
  ADD CONSTRAINT `historia_clinica_ibfk_2` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `historia_clinica_ibfk_3` FOREIGN KEY (`id_sintomas`) REFERENCES `sintomas` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `historia_clinica_ibfk_4` FOREIGN KEY (`id_paciente`) REFERENCES `paciente` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `historia_clinica_ibfk_5` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `lejos`
--
ALTER TABLE `lejos`
  ADD CONSTRAINT `lejos_ibfk_1` FOREIGN KEY (`id_formula`) REFERENCES `formulas` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `paciente`
--
ALTER TABLE `paciente`
  ADD CONSTRAINT `paciente_ibfk_2` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `paciente_ibfk_3` FOREIGN KEY (`id_documento`) REFERENCES `tipo_documento` (`id`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `paciente_ibfk_4` FOREIGN KEY (`id_usuario`) REFERENCES `usuarios` (`id_usuario`) ON DELETE NO ACTION ON UPDATE CASCADE;

--
-- Filtros para la tabla `refraccion`
--
ALTER TABLE `refraccion`
  ADD CONSTRAINT `refraccion_ibfk_1` FOREIGN KEY (`id_historia`) REFERENCES `historia_clinica` (`id_historial`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `rx_final`
--
ALTER TABLE `rx_final`
  ADD CONSTRAINT `rx_final_ibfk_1` FOREIGN KEY (`id_historia`) REFERENCES `historia_clinica` (`id_historial`) ON DELETE CASCADE ON UPDATE NO ACTION;

--
-- Filtros para la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD CONSTRAINT `usuarios_ibfk_1` FOREIGN KEY (`id_estado`) REFERENCES `estado` (`id_estado`) ON DELETE CASCADE ON UPDATE NO ACTION,
  ADD CONSTRAINT `usuarios_ibfk_2` FOREIGN KEY (`rol`) REFERENCES `roles` (`id_rol`) ON DELETE CASCADE ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
