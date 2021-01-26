<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <link rel="stylesheet" href="monProjet.css" />
        <title>TP Température Villes</title>
    </head>
<body>

<?php
try
{
	$bdd = new PDO('mysql:host=localhost;dbname=bdd_temperaturevilles;charset=utf8', 'root', '', array(PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION));
}
catch(Exception $e)
{
        die('Erreur : '.$e->getMessage());
}

$req = $bdd->prepare('SELECT temperature, pression, HOUR(last_update) AS heure, MINUTE(last_update) AS minute FROM temperaturevilles WHERE ville = ?');
$req->execute(array($_POST['ville']));

$data = $req->fetch();

// ucfirst : 1ere lettre en majuscule; htmlspecialchars : protection faille XSS
echo 'A '. $data['heure'] . 'h' . $data['minute'] .' il faisait '. $data['temperature'] . '° avec une pression atmosphérique de '. $data['pression'] .'hpa à '. ucfirst(htmlspecialchars($_POST['ville']));

$req->closeCursor();

?>

</body>
