<?php
error_reporting(E_ALL & ~E_NOTICE);
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="robots" content="noindex">
		<meta name="googlebot" content="noindex">
		<title>BelSD - Home Server</title>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script type="text/javascript">
			var auto_refresh = setInterval(
			function ()
			{
				$('#bloc').load('lecture.php').fadeIn("slow");
			}, 1000); // refresh every 1000 milliseconds
			$(document).ready(function(){
				$("#lire_carte").click(function(){
					$.ajax({
						   url : 'read_card.php' // La ressource ciblée
						});
				});
			});
			$(document).ready(function(){
				$("#reboot").click(function(){
					$.ajax({
						   url : 'reboot_server.php' // La ressource ciblée
						});
				});
			});
			$(document).ready(function(){
				$("#halt").click(function(){
					$.ajax({
						   url : 'shutdown_server.php' // La ressource ciblée
						});
				});
			});
		</script>
		
	</head>
	<body>
		<div id="bloc">Cliquez sur le bouton pour lire la carte</div>
		<button id="lire_carte">Lire Carte</button>
        <BR>
		<form action="creer_carte.php"><button id="creer_carte" type="submit" >Créer Carte</button></form>
	    
        <button id="reboot">Reboot Server</button>
	    <BR>
        <button id="halt">Shutdown Server</button>
	</body>
</html>
