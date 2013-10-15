$(document).ready(function() { 
    
   
    
        
    $('#email_signup_form').ajaxForm({
    	dataType: 'json',
    	success: processJson
    	
    });
    
    
    function processJson(data){
        if(data.status == true) { //form submission was successful
        	//alert(data.message + '/n' + data.status);
        	$('#signerupper').load('signups/messages.html #successkid').hide().fadeIn('slow');
        	
        }
        
        else { //form submission was NIT successful
            //alert(data.message + '/n' + data.status);
            
            $('<span></span').insertAfter('.cta').load('signups/messages.html #msg-bubble', function() {
              $('.msg').empty().append(data.message);
            }).hide().fadeIn('slow');
            
        	$('#id_email_signup').keyup(function() {
        	  $('.msg-bubble').fadeOut('fast');
        	});
        }
        
        
        
    	
    }
    
    
    
   
    $(function(){
    			
    			
    			$('#maximage').maximage({
    				cycleOptions: {
    					fx: 'fade',
    					speed: 1000, // Has to match the speed for CSS transitions in jQuery.maximage.css (lines 30 - 33)
    					timeout: 6000, // 0 for stop 6000 live
    					prev: '#arrow_left',
    					next: '#arrow_right',
    					pause: 1,
    					
    					before: function(last,current){
    						
    						if(!$.browser.msie){
    							// Start HTML5 video when you arrive
    							if($(current).find('video').length > 0) $(current).find('video')[0].play();
    						}
    					},
    					after: function(last,current){
    						if(!$.browser.msie){
    							// Pauses HTML5 video when you leave it
    							if($(last).find('video').length > 0) $(last).find('video')[0].pause();
    						}
    						//var elementht = $('#bigslide').height();
    						//var pageht = $('.page-wrap').height();
    						//alert('element :' + elementht + '\n page:'+ pageht);
    					}
    				},
    				onFirstImageLoaded: function(){
    					jQuery('#cycle-loader').hide();
    					jQuery('#maximage').fadeIn('fast');
    					jQuery('#aheadlist').cycle({
    						fx: 'fade',
    						speed: 300,
    						timeout: 300,
    					});
    					
    				}
    			});
    
    			// Helper function to Fill and Center the HTML5 Video
    			jQuery('video,object').maximage('maxcover');
    
    			// To show it is dynamic html text
    			jQuery('.in-slide-content').delay(1200).fadeIn();
    		});
    
    
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
    // Get the position of the location where the scroller starts.
    var content_start = $("section.content").offset().top;
    var head_ht = $("header.banner").height();
    var where_at = $(this).scrollTop();
    var title_at = $("article.full header .hgroup").offset().top;
    var op = (3*((title_at-head_ht)-where_at))/(title_at-head_ht)
    
     
     //when scrolltop is equal to or greater than content_start - head ht, put a black border on the bottom of header.banner
    
    $("p.scrollthang").text('content at' + content_start + 'head is' + head_ht + 'where?' + where_at + 'title at: ' + title_at +'op: '+op);
    
    if (where_at >= (content_start-head_ht)-10){
    	//$("header.banner").css("border-bottom","10px solid #333");
    	$("div.hr").css("display","block");
    	
    }
    else{
    	//$("header.banner").css("border-bottom","none");
    	$("div.hr").css("display","none");
    }
    
    $("article.full header .hgroup").css("opacity",op);
   
    });



     
}); 



