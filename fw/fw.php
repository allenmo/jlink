<?php
#header("Content-Type: text/json");

$phpInput = file_get_contents("php://input");
$jsonObj = json_decode($phpInput, true);
$customer = $jsonObj['customer'];
$model = $jsonObj['model'];
$component_designator = $jsonObj['component_designator'];
$fw_version = $jsonObj['fw_version'];
$fw_checksum = $jsonObj['fw_checksum'];

/*echo $customer . "\n";
echo $model . "\n";
echo $component_designator . "\n";
*/

require_once('connectvars_prog.php');
$conn = mysqli_connect(DB_HOST, DB_USER, DB_PASSWORD, DB_NAME);
//-------------- customer,    model,    component_designator,fw_verison,fw_checksum
$sql = "call `programming`.`ups_new_fw_available`('{$customer}', '{$model}', '{$component_designator}', @fw_version, @fw_checksum, @fw_pathname)";
$result = mysqli_query($conn, $sql);
$result = mysqli_query($conn, "select @fw_version AS fw_version, @fw_checksum AS fw_checksum, @fw_pathname AS fw_pathname");

$len = mysqli_num_rows($result);
// echo "len:" . $len . "<br/>";
if($len == 1){
	$row = mysqli_fetch_array($result);
	$fw_version_db = $row['fw_version'];
	$fw_checksum_db = $row['fw_checksum'];
	$fw_pathname = $row['fw_pathname'];
	
	$available = 0;
	if($fw_version != $fw_version_db && fw_version != "" && $fw_version_db != ""){
		$result_arr = array("available" => 1,
								"fw_version" => $fw_version_db,
								"fw_checksum" => $fw_checksum_db,
								"fw_pathname" => $fw_pathname);
	}else{
		$result_arr = array("available" => 0,
								"fw_version" => $fw_version_db,
								"fw_checksum" => $fw_checksum_db,
								"fw_pathname" => $fw_pathname);
	}
	echo json_encode($result_arr);
		 //print_r($row);
}else{//will not come here if store procedure have "limit 1" sql
	$result_arr = array("available" => 0,
								"fw_version" => "",
								"fw_checksum" => "",
								"fw_pathname" => "");
	echo json_encode($result_arr);
}














?>
