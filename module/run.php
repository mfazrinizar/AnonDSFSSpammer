<?php
include 'func.php';

/*
    https://github.com/Anon6372098 
    Github : Anon6372098
*/

$init = new Bom();

//Eksekusi Call/Sms Boomber (Limit 3x/Jam)
$init->type = 2; //Ketik 2 untuk telpon, Ketik 1 untuk sms
$init->no = ""; //Nomor Hp tujuan

if ($init->type == 1) {
	for ($i=0; $i < 2; $i++) { 
	    $init->Verif($init->no,$init->type);
	}
}elseif ($init->type == 2) {
	 $init->Verif($init->no,$init->type);
}
