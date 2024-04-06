async function loadRestaurants(){
    document.getElementById("fillRestaurants").innerHTML = `
    <div class="text-center">Loading...</div>`
    const response = await fetch("https://bookeat.xyz/api/restaurant/get_your_resturent/",{
        method: 'POST',
        body: JSON.stringify({
            id : JSON.parse(localStorage.getItem('tokenAuth')).id,
        })
    })
    const data = await response.json()
    console.log("data is ",data)
    console.log(data.data)
    if(data.status==="success"){
        const restaurantArray = Array.from(data.data)
        const elem = document.getElementById("fillRestaurants")
        elem.innerHTML = restaurantArray.map((restaurant)=>{
            return `
            <div class="col-sm-6 col-lg-4 col-xl-6 wow fadeIn" data-wow-delay=".3s"}">
            <div class="discount-menu-box d-flex flex-column flex-xl-row align-items-center">
                <div class="discount-menu-img flex-shrink-0">
                    <img class="w-100" src="assets/images/food-menu/discount-1.png" alt="">
                </div>
                <div class="discount-menu-info">
                    <h2 class="h2">${restaurant.name}</h2>
                    <h3 style="font-size: large; color: gray;">Owner - (${restaurant.owner})</h3>
                    <p>${restaurant.address}</p>
                    ${restaurant.is_active ? `<span class="discount-price bg-success text-light p-2 rounded my-2 d-inline-block">Open</span>` : `<span class="discount-price bg-danger text-light p-2 rounded my-2 d-inline-block">Closed</span>`}
                    ${restaurant.tables_available ? `<span class="discount-price text-success d-inline-block">Tables Available (${restaurant.tables_available})</span>` : `<span class="discount-price text-danger p-2 d-inline-block">No Tables Available</span>`}
                    <div class="d-flex flex-column">
                        <a class='common-btn p-2 my-1 text-center' href="#" onclick="enterDetails('${restaurant.name}', '${restaurant.address}', ${restaurant.is_active}, '${restaurant.id}')"><span>Enter Details &nbsp; <i class="bi bi-pencil-square"></i></span></a>
                        <a class='common-btn p-2 my-1 text-center' href="#" onclick="updateDetails('${restaurant.name}', '${restaurant.address}', ${restaurant.is_active}, '${restaurant.id}')"><span>Update Details &nbsp; <i class="bi bi-pencil-square"></i></span></a>
                        <a class="common-btn p-2 my-1 text-center" onclick="placedOrders('${restaurant.id}')"><span>Place Order &nbsp; <i class="bi bi-cart-plus"></i></span></a>
                        </div>
                </div>
            </div>
        </div>
            `
    }).join("")}

    else if(data.status==="failed"){
        const elem = document.getElementById("fillRestaurants")
        elem.innerHTML = `<h3 class="text-center">No Restaurants Found</h3>`
    }
}

loadRestaurants()

const enterDetails = (restaurant_name, restaurant_address, restaurant_is_active, restaurent_id) => {
    const elem = document.getElementById("fillRestaurants")

    elem.innerHTML = `
    <div class="containerFull">
    <div class="inner-container p-4 rounded" style="box-shadow: 0px 0px 8px 1px #0000002e;">
        <div class="alert alert-danger d-none" role="alert" id="alert">
            <strong id="msg-al">Oh snap!</strong> <span id="alert-message"></span>
        </div>
        <form onsubmit="enterRestaurantDetails(event, '${restaurent_id}')" method="post" class="form-cont">
            <h2 class="text-center mb-4">Edit Restaurant Details</h2>
            <label for="name">Restaurant Name</label>
            <div class="input-cont">
                <i class="bx bx-home"></i><input type="text" id="name" placeholder="Restaurant Name" value="${restaurant_name}">
            </div>
            <!-- password -->
            <label for="Address">Restaurant Address*</label>
            <div class="input-cont">
                <i class="bx bx-home"></i><input type="text" id="Address" placeholder="Enter Address Here..." value="${restaurant_address}">
            </div>
            <label for="tables">No of Tables?</label>
            <div class="input-cont">
                <i class="bx bx-home"></i><input type="text" id="tables" placeholder="No of Tables">
            </div>
            ${!restaurant_is_active ? `
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
                <label class="form-check-label" for="flexSwitchCheckDefault">Restaurant Closed</label>
            </div>` : `
            <div class="form-check form-switch">
                <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
                <label class="form-check-label" for="flexSwitchCheckChecked">Restaurant Open</label>
            </div>
            `}
            <div class="menu-inputs" style="display: flex; flex-direction: column;">
                <label style="font-size: larger; text-align: center;" class="my-2">Add Items to Menu</label>
                <div class="fillMenuItems" style="display: flex; flex-direction: column;">
                <div class="menu-item d-flex justify-around">
                    <input type="text" placeholder="Item Name" class="item-name input-cont mx-2">
                    <input type="number" placeholder="Item Price" class="item-price input-cont mx-2">
                    <input type="file" placeholder="Item Image" class="item-image input-cont mx-2" accept="image/*">
                    <input type="number" placeholder="stock" class="item-stock input-cont mx-2">
                </div>
                </div>
                <button onclick="addMoreItems(event)" class="common-btn text-center my-2" style="display: flex; align-items: center; flex-direction: row-reverse; justify-content: center; border: none;">Add More Items <i class="bi bi-plus"></i></button>
            <!-- submit -->
            <input id="submit" type="submit" value="Save Details">
        </form>
    </div>
</div>
    `
}

const updateDetails = async (restaurant_name, restaurant_address, restaurant_is_active, restaurent_id) => {
    const elem = document.getElementById("fillRestaurants")

    const response = await fetch("https://bookeat.xyz/api/restaurant/get_your_resturent_details/",{
        method: 'POST',
        body: JSON.stringify({
            uid : JSON.parse(localStorage.getItem('tokenAuth')).id,
            id : restaurent_id,
        })
    })
    const data = await response.json()
    console.log("data is ",data)

    elem.innerHTML = `
    <div class="containerFull">
    <div class="inner-container p-4 rounded" style="box-shadow: 0px 0px 8px 1px #0000002e;">
        <div class="alert alert-danger d-none" role="alert" id="alert">
            <strong id="msg-al">Oh snap!</strong> <span id="alert-message"></span>
        </div>
        <form onsubmit="updateRestaurantDetails(event, '${restaurent_id}')" method="post" class="form-cont">
            <h2 class="text-center mb-4">Edit Restaurant Details</h2>
            <label for="name">Restaurant Name</label>
            <div class="input-cont">
            <i class="bx bx-home"></i><input type="text" id="name" placeholder="Restaurant Name" value="${restaurant_name}">
            </div>
            <!-- password -->
            <label for="Address">Restaurant Address*</label>
            <div class="input-cont">
                <i class="bx bx-home"></i><input type="text" id="Address" placeholder="Enter Address Here..." value="${restaurant_address}">
            </div>
            <label for="tables">No of Tables?</label>
            ${data.data.tables.map((table)=>{
                return `
                <div class="d-flex">
                    <div class="input-cont" style="background: #d3d3d3 !important; width: fit-content;">
                        <i class="bx bx-home"></i><span id="tables">${table.table_number}</span>
                    </div>
                    <div class="d-flex align-items-center">
                    ${!table.is_available? `<i class="bi bi-x-circle-fill" style="font-size: 2rem; color: red; margin-left: 1rem;"></i> 
                        <select class="form-select" aria-label="Default select example" style="margin-left: 1rem;">
                        <option>Available</option>
                            <option selected>Booked by - ${table.booked_by ? table.booked_by : "Owner"}</option>
                        </select>
                    ` : `<i class="bi bi-check-circle-fill" style="font-size: 2rem; color: green; margin-left: 1rem;"></i> 
                        <select class="form-select" aria-label="Default select example" style="margin-left: 1rem;">
                        <option>Booked</option>
                        <option selected>Available</option>
                        </select>
                    ` }
                    </div>
                </div>
                `
            }).join("")}
            ${!restaurant_is_active ? `
            <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" id="flexSwitchCheckDefault">
            <label class="form-check-label" for="flexSwitchCheckDefault">Restaurant Closed</label>
            </div>` : `
            <div class="form-check form-switch">
            <input class="form-check-input" type="checkbox" id="flexSwitchCheckChecked" checked>
            <label class="form-check-label" for="flexSwitchCheckChecked">Restaurant Open</label>
            </div>
            `}
            <div class="menu-inputs" style="display: flex; flex-direction: column;">
                <label style="font-size: larger; text-align: center;" class="my-2">Update Menu Items</label>
                <div class="fillMenuItems" style="display: flex; flex-direction: column;">
                ${data.data.menu_items.map((item)=>{
                    return `
                    <div class="menu-item d-flex justify-around">
                        <input type="text" placeholder="Item Name" id="${item.id}" class="item-name input-cont mx-2" value="${item.name}">
                        <input type="number" placeholder="Item Price" class="item-price input-cont mx-2" value="${item.price}">
                        <input type="file" placeholder="Item Image" class="item-image input-cont mx-2" accept="image/*">
                        <input type="number" placeholder="stock" class="item-stock input-cont mx-2" value="${item.stock}">
                    </div>
                    `
                }
                ).join("")}
                </div>
            </div>
            <!-- submit -->
            <div class="d-flex justify-content-center">
                <button type="button" class="common-btn mx-2 border-0" onclick="loadRestaurants()"> Cancel </button>
                <input id="submit" type="submit" value="Save Details">
            </div>
        </form>
    </div>
</div>
`
}


const updateRestaurantDetails = async (e, restaurent_id) => {
    e.preventDefault()
    const submitBtn = document.getElementById('submit')
    submitBtn.disabled = true
    submitBtn.value = 'Updating...'
    // checks

    const user_id = JSON.parse(localStorage.getItem('tokenAuth')).id
    const name = document.getElementById('name').value
    const address = document.getElementById('Address').value
    const menu_items = document.querySelectorAll(".menu-item")
    const table_status = document.querySelectorAll(".form-select")
    const tables = document.getElementById('tables').value
    let is_active = false
    if (document.getElementById('flexSwitchCheckDefault')) {
        if(document.getElementById('flexSwitchCheckDefault').checked){
            is_active = true
        }
    }

    if(document.getElementById('flexSwitchCheckChecked')){
        if(document.getElementById('flexSwitchCheckChecked').checked){
            is_active = true
        }
    }

    if(name === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Name cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
        return

    }

    if(address === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Address cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
        return
    }

    // send data to server

    const menu_items_array = Array.from(menu_items).map((item)=>{
        return {
            id: item.querySelector(".item-name").id,
            name: item.querySelector(".item-name").value,
            price: item.querySelector(".item-price").value,
            image: item.querySelector(".item-image").value,
            stock: item.querySelector(".item-stock").value,
        }
    })

    const table_status_array = Array.from(table_status).map((item)=>{
        return {
            table_number: item.parentElement.parentElement.querySelector("#tables").innerHTML,
            is_available: item.value === "Available" ? true : false,
        }
    })

    const server_response = await fetch('https://bookeat.xyz/api/restaurant/update_resturent_details/',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            uid : user_id,
            id : restaurent_id,
            name: name,
            address: address,
            is_active: is_active,
            menu_items: menu_items_array,
            table_status: table_status_array,
        })
    })

    const data = await server_response.json()
    console.log(data)
    if (data.status === "success") {
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = data.message
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
        loadRestaurants()
    }

    else {
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = data.message
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
    }
}


const addMoreItems = (e) => {
    e.preventDefault()
    const elem = document.querySelector(".fillMenuItems")
    elem.innerHTML += `
    <div class="menu-item d-flex justify-around">
        <input type="text" placeholder="Item Name" class="item-name input-cont mx-2">
        <input type="number" placeholder="Item Price" class="item-price input-cont mx-2">
        <input type="file" placeholder="Item Image" class="item-image input-cont mx-2" accept="image/*">
        <input type="number" placeholder="stock" class="item-stock input-cont mx-2">
    </div>
    `
}

const enterRestaurantDetails = (e, restaurent_id) => {
    e.preventDefault()
    const submitBtn = document.getElementById('submit')
    submitBtn.disabled = true
    submitBtn.value = 'Updating...'

    // checks

    const user_id = JSON.parse(localStorage.getItem('tokenAuth')).id
    const name = document.getElementById('name').value
    const address = document.getElementById('Address').value
    const menu_items = document.querySelectorAll(".menu-item")
    const tables = document.getElementById('tables').value
    let is_active = false
    if (document.getElementById('flexSwitchCheckDefault')) {
        if(document.getElementById('flexSwitchCheckDefault').checked){
            is_active = true
        }
    }

    if(document.getElementById('flexSwitchCheckChecked')){
        if(document.getElementById('flexSwitchCheckChecked').checked){
            is_active = true
        }
    }

    if(name === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Name cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
        return
    }

    if(address === ''){
        const alertMessage = document.getElementById('alert-message')
        alertMessage.innerHTML = 'Address cannot be empty'
        const alert = document.getElementById('alert')
        alert.classList.remove('d-none')
        submitBtn.disabled = false
        submitBtn.value = 'Save Details'
        return
    }

    // send data to server

    fetch('https://bookeat.xyz/api/restaurant/update_resturent/',
    {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            uid : user_id,
            id : restaurent_id,
            name: name,
            address: address,
            is_active: is_active,
            menu_items: Array.from(menu_items).map((item)=>{
                return {
                    name: item.querySelector(".item-name").value,
                    price: item.querySelector(".item-price").value,
                    image: item.querySelector(".item-image").value,
                    stock: item.querySelector(".item-stock").value,
                }
            }),
            tables: tables,
        })
    }).then(res => res.json()).then(data => {
        console.log(data)
        if (data.status === "success") {
            const alertMessage = document.getElementById('alert-message')
            alertMessage.innerHTML = data.message
            const alert = document.getElementById('alert')
            alert.classList.remove('d-none')
            submitBtn.disabled = false
            submitBtn.value = 'Save Details'
            loadRestaurants()
        } else {
            const alertMessage = document.getElementById('alert-message')
            alertMessage.innerHTML = data.message
            const alert = document.getElementById('alert')
            alert.classList.remove('d-none')
            submitBtn.disabled = false
            submitBtn.value = 'Save Details'
        }
    }
    ).catch(err => {
        console.log(err)
    })
}