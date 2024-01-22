


const signup = (e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('submit');
    submitBtn.disabled = true;
    const fullName = document.getElementById('fullName').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const userType = document.getElementById('userType').value;
    // check if the full name is empty
    if (fullName === '') {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'Full name cannot be empty';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // check the phone number
    if (phoneNumber.length !== 10) {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'Phone number must be 10 digits';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // check if the passwords match with the confirm password
    if (password !== confirmPassword) {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'Password does not match';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // send the data to the server
    if (userType === 'diner') {

    fetch('https://176b-2401-4900-5f75-f100-b4cc-cbb2-6ca-86f1.ngrok-free.app/create_customer/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: fullName,
                phone: phoneNumber,
                password: password,
                confirm_password: confirmPassword
            })
        }).then(res => res.json()).then(data => {
            console.log(data);
            if (data.status !== "success") {
                const alertMessage = document.getElementById('alert-message');
                alertMessage.innerHTML = data.message;
                const alert = document.getElementById('alert');
                alert.classList.remove('d-none');
                submitBtn.disabled = false;
                return;
            } else {
                const alertMessage = document.getElementById('alert-message');
                alertMessage.innerHTML = 'Account created successfully';
                const msg = document.getElementById('msg-al');
                msg.innerHTML = 'success';
                const alert = document.getElementById('alert');
                alert.classList.replace('alert-danger', 'alert-success');
                alert.classList.remove('d-none');
                localStorage.setItem('tokenAuth' , JSON.stringify(data.data));

                setTimeout(() => {
                    window.location.pathname = '/client/otp.html';
                }, 3000);
            }
        }
        )
    
    
    } else{
            fetch('https://176b-2401-4900-5f75-f100-b4cc-cbb2-6ca-86f1.ngrok-free.app/create_resturent_owner/'
            ,{
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    fullName: fullName,
                    phoneNumber: phoneNumber,
                    password: password
                })
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('Account created successfully');
                    window.location.pathname = '';
    
    
                }
            }
            )
        }
    }


const login = (e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('submit');
    submitBtn.disabled = true;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const password = document.getElementById('password').value;
    const userType = document.getElementById('userType').value;
    // check the phone number

    if (phoneNumber.length !== 10) {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'Phone number must be 10 digits';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // send the data to the server

    if (userType === 'diner') {
        fetch('https://176b-2401-4900-5f75-f100-b4cc-cbb2-6ca-86f1.ngrok-free.app/customer_login/',

            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    phone: phoneNumber,
                    password: password
                })
            }).then(res => res.json()).then(data => {
                console.log(data);
                if (data.status !== "success") {
                    const alertMessage = document.getElementById('alert-message');
                    alertMessage.innerHTML = data.message;
                    const alert = document.getElementById('alert');
                    alert.classList.remove('d-none');
                    submitBtn.disabled = false;
                    return;
                } else {
                    const alertMessage = document.getElementById('alert-message');
                    alertMessage.innerHTML = 'Login successfully';
                    const msg = document.getElementById('msg-al');
                    msg.innerHTML = 'success';
                    const alert = document.getElementById('alert');
                    alert.classList.replace('alert-danger', 'alert-success');
                    alert.classList.remove('d-none');
                    localStorage.setItem('tokenAuth' , JSON.stringify(data.data));
                    setTimeout(() => {
                        window.location.pathname = '/client/home-02.html';
                    }, 3000);
                }
            }
            )
    }
    else{
        fetch('https://176b-2401-4900-5f75-f100-b4cc-cbb2-6ca-86f1.ngrok-free.app/resturent_owner_login/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                phone: phoneNumber,
                password: password
            })
        }).then(res => res.json()).then(data => {
            console.log(data);
            if (data.status !== "success") {
                const alertMessage = document.getElementById('alert-message');
                alertMessage.innerHTML = data.message;
                const alert = document.getElementById('alert');
                alert.classList.remove('d-none');
                submitBtn.disabled = false;
                return;
            } else {
                const alertMessage = document.getElementById('alert-message');
                alertMessage.innerHTML = 'Login successfully';
                const msg = document.getElementById('msg-al');
                msg.innerHTML = 'success';
                const alert = document.getElementById('alert');
                alert.classList.replace('alert-danger', 'alert-success');
                alert.classList.remove('d-none');
                localStorage.setItem('tokenAuth' , JSON.stringify(data.data));
                setTimeout(() => {
                    window.location.pathname = '/client/home-02.html';
                }, 3000);
            }
        }
        )
    }

}