function validar_numero(){
	var number = document.getElementById("cardnumber").value;
	
	if (number == ""){
		mostrar();
		document.getElementById("cardnumber").select();
	        document.getElementById("cardnumber").focus();
		return false;
		
	}
	else if( !(/^\d{16}$/.test(number)) ) {
		document.getElementById("cardnumber").select();
	        document.getElementById("cardnumber").focus();			  	
		mostrar();
	  	return false;
	}
	
	return true;	
}


function validar_cvv(){
	
	var cvv = document.getElementById("cvv").value;
	var tvista = document.getElementById("vista").checked;
	var tmister = document.getElementById("mister").checked;
	var txpress = document.getElementById("xpress").checked;

	
	if(cvv == ""){
				
		mostrar2();	
		document.getElementById("cvv").select();
	        document.getElementById("cvv").focus();
		return false;	
	}
	
	else if( (!(/^\d{3}$/.test(cvv))) && (txpress==false)) {
	 	mostrar2();
		document.getElementById("cvv").select();
	        document.getElementById("cvv").focus();
		return false;	
	}
		
	else if((txpress==true) && (!(/^\d{4}$/.test(cvv)))){
		mostrar2();
		document.getElementById("cvv").select();
	        document.getElementById("cvv").focus();
		return false;	
	}
		
	return true;	
}


function validar_tipo(){

	var tvista = document.getElementById("vista").checked;
	var tmister = document.getElementById("mister").checked;
	var txpress = document.getElementById("xpress").checked;

	
if((txpress==false) && (tvista==false) && (tmister==false)){
		mostrar3();
		return false;	
	}
	return true;	
}


function validar_todo(){
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
	        document.getElementById("cardnumber").focus();
		return false;
		
	}
	else if( !(/^\d{16}$/.test(number)) ) {
	  	mostrar();
	  	return false;
	}	

	else if(cvv == ""){
				
		mostrar2();	
	        document.getElementById("cvv").focus();
		return false;	
	}
	
	else if( (!(/^\d{3}$/.test(cvv))) && (txpress==false)) {
	 	mostrar2();
	        document.getElementById("cvv").focus();
		return false;	
	}
		
	else if((txpress==true) && (!(/^\d{4}$/.test(cvv)))){
		mostrar2();
	        document.getElementById("cvv").focus();
		return false;	
	}
		
	setValue();
	return true;	
}


	
