<?php
error_reporting(E_ALL & ~E_NOTICE);
//shell_exec("sudo python Lecture.py".$buzzer);
$servername = "localhost";
$username = "USER_NAME";
$password = "USER_PASSWORD";
$dbname = "USER_DATA_BASE_NAME";

$conn = mysqli_connect($servername, $username, $password, $dbname);
// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}

$sql = "SELECT * FROM card_reader";
$result = mysqli_query($conn, $sql);

while ($ligne = mysqli_fetch_array($result))
{
    if ($ligne['id']=='2')
    {
        $ligne_UID = $ligne['valeur'];
    }
    if ($ligne['id']=='3')
    {
        $Date_creation = $ligne['valeur'];
    }
    if ($ligne['id']=='4')
    {
        $Nom = $ligne['valeur'];
    }
    if ($ligne['id']=='5')
    {
        $Prenom = $ligne['valeur'];
    }
    if ($ligne['id']=='6')
    {
        $Nr_client = $ligne['valeur'];
    }
    if ($ligne['id']=='7')
    {
        $Points = $ligne['valeur'];
    }
    if ($ligne['id']=='8')
    {
        $Date_visite = $ligne['valeur'];
    }
}
echo "Nr. de Carte : ".$ligne_UID."<BR>";
echo "Date création Carte : ".$Date_creation."<BR>";
echo "Nom : ".$Nom."<BR>";
echo "Prénom : ".$Prenom."<BR>";
echo "Nr. client : ".$Nr_client."<BR>";
echo "Nbr. points : ".$Points."<BR>";
echo "Date dernière Visite : ".$Date_visite."<BR>";
echo "<BR>";
mysqli_close($conn);
?>