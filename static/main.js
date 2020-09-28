let content = document.getElementById('content');

function changeType(qr_code) {
    if (qr_code.value == 'text') {
        content.type = 'text';
        content.placeholder = 'Enter your text to share here';
    } else if (qr_code.value == 'url') {
        content.type = 'url';
        content.placeholder = 'Enter your URL to share here';
    } else if (qr_code.value == 'email') {
        content.type = 'email';
        content.placeholder = 'Enter your email to share here';
    } else if (qr_code.value == 'telephone') {
        content.type = 'tel';
        content.placeholder = 'Enter your telephone to share here';
    } else if (qr_code.value == 'geo') {
        content.type = 'text';
        content.placeholder = 'Enter your GPS coordinates to share here';       
    }
}