<?php
	require_once("modelo.php");
	
	$pattern=strtolower($_GET['pattern']);
	$conexion=connect();
	$query="INSERT INTO productos (nombre) VALUES (?)";
	if (!($statement=$conexion->prepare($query))){
			disconnect($conexion);
            die("Preparation failed");
	}
	$nombre = $conexion->real_escape_string($pattern);
	if(!($statement->bind_param("s", $nombre))){
			disconnect($conexion);
			die("Parameter vinculation failed");
	}
	if (!$statement->execute()){
		disconnect($conexion);
		return false;
	}
	disconnect($conexion);
	return true;
?>
