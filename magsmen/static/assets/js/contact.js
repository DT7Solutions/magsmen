// contact form 
$(document).on('submit', '#contactform', function(event){
    event.preventDefault();
     let name= $('#name').val()
     let email = $('#email').val()
     let phone =$('#phone').val()
     let subject = $('#subject').val()
     let message = $('#message').val()
     csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
     
     let data = new FormData();
     data.append("name", name);
     data.append("email",email);
     data.append("phone",phone);
     data.append("subject",subject);
     data.append("message",message);
     data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
     
   
   
     $.ajax({
           url:"/contact/",
           method: 'Post',
           processData:false,
           contentType:false,
           cache:false,
           mimeType:"multipart/form-data",
           data:data,
           
           success:function(data){
               $('#contactform')[0].reset();
               alert("sucessfully sending message")
            //    $('.returnmessage').append("Your message has been received, We will contact you soon.")
           },
           error:function(data){
            alert("Your message has been faild, please try agian.")
            //    $('.returnmessage').append("Your message has been faild, please try agian.")
           }
       })

})
    

