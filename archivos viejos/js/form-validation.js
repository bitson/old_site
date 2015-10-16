$(document).ready(function(){

	// hide messages 
	$("#error").hide();
	$("#success").hide();
	
	// on submit...
	$("#contactForm #submit").click(function() {
		$("#error").hide();
		
		//required:
		
		//name
		var name = $("input#name").val();
		if(name == ""){
			$("#error").fadeIn().text("Ingresar nombre y apellido.");
			$("input#name").focus();
			return false;
		}
		var name = $("input#empresa").val();
		if(name == ""){
			$("#error").fadeIn().text("Ingresar nombre de la Empresa.");
			$("input#empresa").focus();
			return false;
		}
		
		// email
		var email = $("input#email").val();
		if(email == ""){
			$("#error").fadeIn().text("Ingresar E-mail.");
			$("input#email").focus();
			return false;
		}
		
		// telefono
		var web = $("input#telefono").val();
		if(web == ""){
			$("#error").fadeIn().text("Ingresar su teléfono.");
			$("input#web").focus();
			return false;
		}
		// asunto
		var web = $("input#subject").val();
		if(web == ""){
			$("#error").fadeIn().text("Ingresar su teléfono.");
			$("input#subject").focus();
			return false;
		}
		
		// comments
		var comments = $("#comments").val();
		
		// send mail php
		var sendMailUrl = $("#sendMailUrl").val();
		
		//to, from & subject
		var to = $("#to").val();
		var from = $("#from").val();
		var subject = $("#subject").val();
		
		// data string
		var dataString = 'name='+ name
						+ '&email=' + email        
						+ '&web=' + web
						+ '&comments=' + comments
						+ '&to=' + to
						+ '&from=' + from
						+ '&subject=' + subject;						         
		// ajax
		$.ajax({
			type:"POST",
			url: sendMailUrl,
			data: dataString,
			success: success()
		});
	});  
		
		
	// on success...
	 function success(){
	 	$("#success").fadeIn();
	 	$("#contactForm").fadeOut();
	 }
	
    return false;
});

