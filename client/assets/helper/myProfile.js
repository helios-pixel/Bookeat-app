function loadCustomerProfile(){
    console.log("here in loadCustomerProfile")
    const token = JSON.parse(localStorage.getItem('tokenAuth'))
    const first_name = token.name.split(' ')[0]
    const last_name = token.name.split(' ')[1]
    const phone = token.phone
    const email = token.email === undefined ? '' : token.email
    const address = token.address === undefined ? '' : token.address
    console.log(token, first_name, last_name, phone)
    let input_elements = document.getElementsByTagName('input')
    console.log("value is ", input_elements[1].value)
    input_elements[0].value = first_name
    input_elements[1].value = last_name
    input_elements[2].value = email
    input_elements[3].value = phone
    input_elements[4].value = address
}


const loadMyProfile = () => {
    const token = JSON.parse(localStorage.getItem('tokenAuth'))
    if (token === null) {
        window.location.pathname = "/client/siginin.html"
    }
    
    loadCustomerProfile()
}

loadMyProfile()

// update_customer

async function submitMyDetails(e){
    e.preventDefault()
    const token = JSON.parse(localStorage.getItem('tokenAuth'))
    const inputElems = document.getElementsByTagName('input')
    const first_name = inputElems[0].value
    const last_name = inputElems[1].value
    const email = inputElems[2].value
    const phone = token.phone
    const address = inputElems[4].value

    const response = await fetch(`https://bookeat.xyz/api/update_customer/`,{
        method: 'POST',
        body: JSON.stringify({
            fName : first_name,
            lName : last_name,
            email,
            phone,
            address: address,
            role : token.role,
        })
    })
    const data = await response.json()
    console.log(data)
    if (data.status === 'success') {
        alert('Profile updated successfully')
        localStorage.setItem('tokenAuth', JSON.stringify(data.data))
        loadMyProfile()
    }
    else {
        alert('Error updating profile')
    }
}

