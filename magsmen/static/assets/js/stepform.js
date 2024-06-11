// get started form

function writetous(){

    let name = document.getElementById('name').value;
    let email = document.getElementById('email').value;
    let phone = document.getElementById('phone').value;

    let formdata = {
        name: name,
        email: email,
        phone: phone,
    };

    let formDataJson = JSON.stringify(formdata);
    localStorage.setItem('formdata', formDataJson);
    window.location.href = 'questions/';

}





$(document).ready(function(){
    $('#allformssubmit').click(function(event){
        event.preventDefault();
        alert("its working")
        let brandpositionradio = $('input[name="brandpositionradio"]:checked').val();
        let mission = $('#mission').val()
        let brandtargetradio = $('input[name="brandtargetradio"]:checked').val();
        let engagebrandradio = $('input[name="engagebrandradio"]:checked').val();
        let brandperform = $('#brandperform').val()
        let brandchallenge = $('#brandchallenge').val()
        // let brandcheck = $('input[name=brandcheck]:checked').map(function(){
        //     return $(this).val();
        // }).get();
        var motivations = [];
        $('input[name="brandcheck"]:checked').each(function() {
            motivations.push($(this).val());
        });
        let achieve = $('#achieve').val()
        let brandexpectation = $('#brandexpectation').val()
        let storedFormDataJson = localStorage.getItem('formdata');
        let storedFormData = JSON.parse(storedFormDataJson);
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
        
        



        let data = new FormData();
        data.append('brandposition',brandpositionradio),
        data.append('corevalue',mission),
        data.append('brandtarget',brandtargetradio),
        data.append('customerfeedback',engagebrandradio),
        data.append('brandperform',brandperform),
        data.append('brandchallenge',brandchallenge),
        data.append('brandcheck',motivations),
        data.append('achieve',achieve),
        data.append('brandexpectation',brandexpectation),
        data.append('storedFormData', JSON.stringify(storedFormData));
        data.append('csrfmiddlewaretoken',csrfmiddlewaretoken),

        $.ajax({
            url:"/questions/",
            method: 'POST',
            processData:false,
            contentType:false,
            cache:false,
            data:data,
            success:function(data, status,xhr){
                $('#userAccountSetupForm')[0].reset();
                if(data.success === true){
                    window.location.href = '/';
                } else{
                    alert(data.error)
                    window.location.href ='/questions/'
                }
            },
            error:function(data){
                alert("Fail, submitted data");
            }
            
        })

    })
    
})



document.getElementById('getformdata').addEventListener('submit', function (event) {
    var nameInput = document.getElementById('name');
    var emailInput = document.getElementById('email');
    var phoneInput = document.getElementById('phone');

    // Name validation
    if (!nameInput.value.trim()) {
        nameInput.classList.add('is-invalid');
        document.getElementById('name-feedback').style.display = 'block';
        event.preventDefault();
    } else {
        nameInput.classList.remove('is-invalid');
        document.getElementById('name-feedback').style.display = 'none';
    }

    // Email validation
    if (!emailInput.value.trim() || !isValidEmail(emailInput.value.trim())) {
        emailInput.classList.add('is-invalid');
        document.getElementById('email-feedback').style.display = 'block';
        event.preventDefault();
    } else {
        emailInput.classList.remove('is-invalid');
        document.getElementById('email-feedback').style.display = 'none';
    }

    // Phone validation
    if (!phoneInput.value.trim() || !isValidPhone(phoneInput.value.trim())) {
        phoneInput.classList.add('is-invalid');
        document.getElementById('phone-feedback').style.display = 'block';
        event.preventDefault();
    } else {
        phoneInput.classList.remove('is-invalid');
        document.getElementById('phone-feedback').style.display = 'none';
    }
});

// Email validation function
function isValidEmail(email) {
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Phone validation function
function isValidPhone(phone) {
    var phoneRegex = /^\d{10}$/;
    return phoneRegex.test(phone);
}


//country codes changes
document.getElementById('country-code').addEventListener('change', function() {
    var selectedOption = this.options[this.selectedIndex];
    var countryCode = selectedOption.value;
    document.getElementById('phone').value = countryCode;
});


// flgs code 
document.addEventListener("DOMContentLoaded", function() {
    var select = document.getElementById('country-code');
    var options = select.getElementsByTagName('option');

    for (var i = 0; i < options.length; i++) {
        var countryCode = options[i].getAttribute('data-flag');
        var flagImage = 'url(/static/assets/imgs/flags/' + countryCode + '.png)';
        options[i].style.backgroundImage = flagImage;
        options[i].style.backgroundRepeat = 'no-repeat';
        options[i].style.backgroundPosition = 'left center'; // Adjust as needed
        options[i].style.paddingLeft = '25px'; // Adjust as needed
    }
});




