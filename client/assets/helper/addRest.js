function addRestaurant(e){
    e.preventDefault()
    const submitBtn = document.getElementById('submit')
    submitBtn.disabled = true
    submitBtn.value = 'Adding...'
    
    // checks

    const name = document.getElementById('name').value
    const address = document.getElementById('address').value
    const image = document.getElementById('image').value
    const source = document.getElementById('source').value
    const destination = document.getElementById('destination').value

    if(name === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Name cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Add Restaurant'
        return
    }

    if(address === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Address cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Add Restaurant'
        return
    }

    if(image === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Image cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Add Restaurant'
        return
    }

    if(source === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Source cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Add Restaurant'
        return
    }

    if(destination === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Destination cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Add Restaurant'
        return
    }

    // send data to server

    fetch('https://bookeat.xyz/api/restaurant/create_resturent/',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id : JSON.parse(localStorage.getItem('tokenAuth')).id,
            name: name,
            address: address,
            restaurant_image: image,
            is_active: true,
            source: source,
            destination: destination
        })
    }).then(res => res.json()).then(data => {
        console.log(data)
        if (data.status === "success") {
            const alertMessage = document.getElementById('alert-message')
            alertMessage.innerHTML = data.message
            const alert = document.getElementById('alert')
            alert.classList.remove('alert-danger')
            alert.classList.add('alert-success')
            const elem = document.getElementById("msg-al")
            elem.innerHTML = 'Success'
            alert.classList.remove('d-none')
            submitBtn.disabled = false
            submitBtn.value = 'Add Restaurant'
            return
        } else {
            window.location.pathname = '/client/home-02.html'
        }
    }).catch(err => {
        console.log(err)
    })
}