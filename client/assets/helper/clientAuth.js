const signup = (e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('submit');
    submitBtn.disabled = true;
    const fullName = document.getElementById('fullName').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const userType = document.getElementById('userType').value;
    const license = document.getElementById('license').value;
    const pan = document.getElementById('pan').value;
    const gstin = document.getElementById('gstin').value;

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

    fetch('https://bookeat.xyz/api/create_customer/',
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
        // Check if the license, pan and gstin are empty

        if (license === '' || pan === '' || gstin === '') {
            const alertMessage = document.getElementById('alert-message');
            alertMessage.innerHTML = 'License, PAN and GSTIN cannot be empty';
            const alert = document.getElementById('alert');
            alert.classList.remove('d-none');
            submitBtn.disabled = false;
            return;
        }


        fetch('https://bookeat.xyz/api/create_resturent_owner/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: fullName,
                phone: phoneNumber,
                password: password,
                confirm_password: confirmPassword,
                license_num: license,
                pan: pan,
                gstin: gstin
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
        fetch('https://bookeat.xyz/api/customer_login/',

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
        fetch('https://bookeat.xyz/api/resturent_owner_login/',
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

const logout = () => {
    const logoutElement = document.querySelector(".logout-screen")
    logoutElement.classList.remove("d-none")
    const cancelBtn = logoutElement.querySelector(".btn")
    const logoutBtn = logoutElement.querySelector(".common-btn")
    cancelBtn.addEventListener("click", () => {
        logoutElement.classList.add("d-none")
    })
    logoutBtn.addEventListener("click", () => {
        // fake timer
        setTimeout(() => {
            localStorage.removeItem('tokenAuth')
            window.location.pathname = "/client/siginin.html"
        }, 1000)
        logoutBtn.innerHTML = "Logging out..."
    })
}

const submitPhnForPwd=(e) => {
    e.preventDefault();
    const submitBtn = document.getElementById('submit');
    submitBtn.disabled = true;
    const phoneNumber = document.getElementById('phoneNumber').value;
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

    const response = fetch('https://bookeat.xyz/api/forgot_password/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                phone: phoneNumber
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
                alertMessage.innerHTML = 'OTP sent successfully';
                const msg = document.getElementById('msg-al');
                msg.innerHTML = 'success';
                const alert = document.getElementById('alert');
                alert.classList.replace('alert-danger', 'alert-success');
                alert.classList.remove('d-none');
                localStorage.setItem('tokenAuth' , JSON.stringify(data.data));
                document.getElementById('phoneNumber').setAttribute('readonly', 'true');
                const form = document.getElementById('formForFOrgotpwd');
                const label = document.createElement('label');
                label.setAttribute('for', 'otp');
                label.innerHTML = 'OTP*';
                form.appendChild(label);
                const div = document.createElement('div');
                div.classList.add('input-cont');
                form.appendChild(div);
                const i = document.createElement('i');
                i.classList.add('bx');
                i.classList.add('bx-phone');
                div.appendChild(i);
                const input = document.createElement('input');
                input.setAttribute('type', 'number');
                input.setAttribute('id', 'otp');
                input.setAttribute('placeholder', 'OTP');
                div.appendChild(input);
                form.setAttribute('onsubmit', `submitOtpForPwd(event, ${phoneNumber})`);
                form.removeChild(submitBtn);
                const btn = document.createElement('button');
                btn.classList.add('common-btn');
                btn.innerHTML = 'Submit OTP';
                form.appendChild(btn);
                const pOld = document.querySelector('.form-cont > p');
                pOld.remove();
                const p = document.createElement('p');
                p.className = 'text-center';
                p.classList.add('mt-3');
                p.innerHTML = "Don't have an account? <a href='../client/register.html'>Sign Up</a>";
                form.appendChild(p);
            }
        }
        )
}

const submitOtpForPwd=(e, phone) => {
    e.preventDefault();
    const submitBtn = document.querySelector('.common-btn');
    submitBtn.disabled = true;
    const otp = document.getElementById('otp').value;
    // check the phone number

    if (otp.length !== 6) {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'OTP must be 6 digits';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // send the data to the server

    const response = fetch('https://bookeat.xyz/api/validate_otp/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                otp: otp,
                phone: phone
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
                alertMessage.innerHTML = 'OTP verified successfully';
                const msg = document.getElementById('msg-al');
                msg.innerHTML = 'success';
                const alert = document.getElementById('alert');
                alert.classList.replace('alert-danger', 'alert-success');
                alert.classList.remove('d-none');
                localStorage.setItem('tokenAuth' , JSON.stringify(data.data));
                document.getElementById('otp').setAttribute('readonly', 'true');
                const form = document.getElementById('formForFOrgotpwd');
                form.innerHTML = '';
                form.setAttribute('onsubmit', `submitNewPwd(event, ${phone})`);
                // form.removeChild(submitBtn);
                const label = document.createElement('label');
                label.setAttribute('for', 'password');
                label.innerHTML = 'New Password*';
                form.appendChild(label);
                const div = document.createElement('div');
                div.classList.add('input-cont');
                form.appendChild(div);
                const i = document.createElement('i');
                i.classList.add('bx');
                i.classList.add('bx-lock');
                div.appendChild(i);
                const input = document.createElement('input');
                input.setAttribute('type', 'password');
                input.setAttribute('id', 'password');
                input.setAttribute('placeholder', 'New Password');
                div.appendChild(input);
                const label1 = document.createElement('label');
                label1.setAttribute('for', 'confirmPassword');
                label1.innerHTML = 'Confirm Password*';
                form.appendChild(label1);
                const div1 = document.createElement('div');
                div1.classList.add('input-cont');
                form.appendChild(div1);
                const i1 = document.createElement('i');
                i1.classList.add('bx');
                i1.classList.add('bx-lock');
                div1.appendChild(i1);
                const input1 = document.createElement('input');
                input1.setAttribute('type', 'password');
                input1.setAttribute('id', 'confirmPassword');
                input1.setAttribute('placeholder', 'Confirm Password');
                div1.appendChild(input1);
                const btn = document.createElement('button');
                btn.classList.add('common-btn');
                btn.innerHTML = 'Submit';
                form.appendChild(btn);
            }
        }
        )
}

const submitNewPwd = (e, phone) => {
    e.preventDefault();
    const submitBtn = document.querySelector('.common-btn');
    submitBtn.disabled = true;
    const password = document.getElementById('password').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    // check the phone number

    if (password !== confirmPassword) {
        const alertMessage = document.getElementById('alert-message');
        alertMessage.innerHTML = 'Password does not match';
        const alert = document.getElementById('alert');
        alert.classList.remove('d-none');
        submitBtn.disabled = false;
        return;
    }
    // send the data to the server

    const response = fetch('https://bookeat.xyz/api/reset_password/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                password: password,
                phone: phone
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
                alertMessage.innerHTML = 'Password reset successfully';
                const msg = document.getElementById('msg-al');
                msg.innerHTML = 'success';
                const alert = document.getElementById('alert');
                alert.classList.replace('alert-danger', 'alert-success');
                alert.classList.remove('d-none');
                localStorage.setItem('tokenAuth' , JSON.stringify(data.data));
                setTimeout(() => {
                    window.location.pathname = '/client/siginin.html';
                }, 3000);
            }
        }
        )
}
