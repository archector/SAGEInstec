function validar(){
	var number = document.getElementById("cardnumber").value;
	var cvv = document.getElementById("cvv").value;
	var tvista = document.getElementById("vista").checked;
	var tmister = document.getElementById("mister").checked;
	var txpress = document.getElementById("xpress").checked;

	
if((txpress==false) && (tvista==false) && (tmister==false)){
		mostrar3();
		return false;	
	}
	
	else if (number == ""){
		mostrar();	
		return false;
		
	}
	else if( !(/^\d{16}$/.test(number)) ) {
	  	mostrar();
	  	return false;
	}
	else if (cvv == ""){
				
		mostrar2();	
		return false;	
	}
	
	else if( (!(/^\d{3}$/.test(cvv))) && (txpress==false)) {
	 	mostrar2();
		return false;	
	}
		
	else if((txpress==true) && (!(/^\d{4}$/.test(cvv)))){
		mostrar2();
		return false;	
	}
		
	setValue();
	return true;	
}



	
