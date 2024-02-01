

if (localStorage.getItem('tokenAuth') === null) {
    window.location.pathname = '/client/register.html'
}

const verifyOTP = (e) => {

    e.preventDefault()
    const submitBtn = document.getElementById('submit')
    submitBtn.disabled = true
    const otp = document.getElementById('otp').value

    if (otp === '') {
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'OTP cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        return
    }

    const phoneNumber = JSON.parse(localStorage.getItem('tokenAuth')).phone

    if(phoneNumber === null){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Phone number cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        return
    }

    fetch('https://bookeat.xyz/api/customer_otp_verify/',

        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                phone: phoneNumber,
                otp: otp
            })
        }).then(res => res.json()).then(data => {
            console.log(data)
            if (data.status !== "success") {
                const alertMessage = document.getElementById('alert-message')
                alertMessage.innerHTML = data.message
                const alert = document.getElementById('alert')
                alert.classList.remove('d-none')
                submitBtn.disabled = false
                return
            } else {
                window.location.pathname = '/client/home-02.html'
            }
        }).catch(err => {
            console.log(err)
        }
    )
}