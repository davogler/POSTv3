$(document).ready(function() { 
      
    $('#email_signup_form').ajaxForm({
    	dataType: 'json',
    	success: processJson
    	
    });
    
    
    function processJson(data){
        if(data.status == true) { //form submission was successful
        	//alert(data.message + '/n' + data.status);
        	$('#signerupper').load('/signups/messages.html #successkid').hide().fadeIn('slow');
        	
        }
        
        else { //form submission was NIT successful
            //alert(data.message + '/n' + data.status);
            
            $('<span></span').insertAfter('.cta').load('/signups/messages.html #msg-bubble', function() {
              $('.msg').empty().append(data.message);
            }).hide().fadeIn('slow');
            
        	$('#id_email_signup').keyup(function() {
        	  $('.msg-bubble').fadeOut('fast');
        	});
        }
        
    	
    }
    
    $(function(){
    	$('input:text').each(function(){
    		var txtval = $(this).val();
    		$(this).focus(function(){
    			$(this).val('').css('color', 'black')
    		});
    		$(this).blur(function(){
    			if($(this).val() == ""){
    				$(this).val(txtval).css('color', '#bab9b9');
    			}
    		});
    	});
    });     
    

// This function will be executed when the user scrolls the page.
$(window).scroll(function(e) {
	if ( $("section.content").length ) {
		var content_start = $("section.content").offset().top;
		var head_ht = $("header.banner").height();
		var where_at = $(this).scrollTop();
		var title_at = $("article.full header .hgroup").offset().top;
		var op = (3*((title_at-head_ht)-where_at))/(title_at-head_ht)
		
		 $("article.full header .hgroup").css("opacity",op);
	}
    // Get the position of the location where the scroller starts.
   
     //when scrolltop is equal to or greater than content_start - head ht, put a black border on the bottom of header.banner
    
        
    if (where_at >= (content_start-head_ht)-10){
    	
    	$("div.hr").css("display","block");
    	
    }
    else{
       	$("div.hr").css("display","none");
    }
    
       
    });



$( ".chiclets li" )
  .mouseenter(function() {
    $( this ).animate({marginLeft:"+=3px"}, 100);
  })
  .mouseleave(function() {
    $( this ).animate({marginLeft:"-=3px"}, 100);
  });
  
   
  
 $('.socialper').one('mouseenter', function()
                  {
                          Socialite.load($(this)[0]);
                  });
  
     
var $container = $('.bios');
// initialize
$container.masonry({
  gutter: 25,
  isFitWidth: true,
  itemSelector: '.person'
});


}); 


