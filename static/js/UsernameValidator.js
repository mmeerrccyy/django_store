const usernameField = document.getElementById('id_username');

usernameField.addEventListener("keyup", (e) => {
    const usernameValue = e.target.value;

    usernameField.classList.remove('is-invalid');

    if(usernameValue.length > 0){
        fetch('/api/validate-username/', {
            body: JSON.stringify({
                username: usernameValue
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if(data.username_error){
                usernameField.classList.add('is-invalid')
            }
        })
    }
});
