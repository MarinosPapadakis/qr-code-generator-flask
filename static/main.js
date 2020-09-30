function changeType(qr_code) {
    
    let content = document.getElementById('content');

    if (qr_code.value == 'Text') {
        content.type = 'text';
        content.placeholder = 'Enter your text to share here';
    } else if (qr_code.value == 'URL') {
        content.type = 'url';
        content.placeholder = 'Enter your URL to share here';
    } else if (qr_code.value == 'Email') {
        content.type = 'email';
        content.placeholder = 'Enter your email to share here';
    } else if (qr_code.value == 'Telephone') {
        content.type = 'tel';
        content.placeholder = 'Enter your telephone to share here';
    } else if (qr_code.value == 'Geolocation') {
        content.type = 'text';
        content.placeholder = 'Enter your GPS coordinates to share here';       
    }
}