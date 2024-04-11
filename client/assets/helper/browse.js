const load = ()=>{
    let signinPlace = document.getElementById('signinPlace');
    let token = JSON.parse(localStorage.getItem('tokenAuth'))
    console.log(token)
    if(token===null){
        window.location.pathname = "/client/siginin.html"
    }
    if(token !== null){
        console.log("here")
        signinPlace.innerHTML = `${token.name}`
    }
    if(token !== null && token.role === 'customer'){
        loadCustomer()
    }
    if(token !== null && token.role === 'resturent_owner'){
        loadRestaurantOwner()
    }
    const logoutElement = document.createElement("div")
    logoutElement.classList.add("logout-screen", "d-none")
    logoutElement.innerHTML = `
    <div class="inner-screen">
        <h3 class="mt-2 mb-3">Are Your sure you want to Logout?</h3>
        <div class="btns d-flex">
            <a class="btn">Cancel</a>
            <button class="common-btn">Logout</button>
        </div>
    </div>
    `
    document.body.appendChild(logoutElement)
}

const loadRestaurantOwner =()=>{
    const element = document.createElement('li');
    element.innerHTML = `
        <a href="addRestaurant.html">Add Restaurant</a>
    `
    document.getElementById('navChilds').appendChild(element)
    const hamburgerMenuListElement = document.createElement("div")
    hamburgerMenuListElement.classList.add("hamburgerMenusList", "d-none")
    hamburgerMenuListElement.innerHTML = `
    <ul>
        <li onclick="editProfile()">Edit Profile</li>
        <li onclick="myRestaurants()">Your Restaurants</li>
        <li onclick="logout()">Logout</li>
    </ul>
    `
    document.body.appendChild(hamburgerMenuListElement)
    return;
} 

const loadCustomer =()=>{
    const element = document.createElement('li');
    element.innerHTML = `
        <a href="./restaurants.html">Restaurants</a>
    `
    document.getElementById('navChilds').appendChild(element)
    const hamburgerMenuListElement = document.createElement("div")
    hamburgerMenuListElement.classList.add("hamburgerMenusList", "d-none")
    hamburgerMenuListElement.innerHTML = `
    <ul>
        <li onclick="editProfile()">Edit Profile</li>
        <li onclick="myOrders()">Your Orders</li>
        <li onclick="logout()">Logout</li>
    </ul>
    `
    document.body.appendChild(hamburgerMenuListElement)
    return;
}

load()


function openMenus(){
    document.querySelector('.hamburgerMenusList').classList.toggle('d-none')
}

function myRestaurants(){
    window.location.pathname = '/client/your_restaurant.html'
}

function myOrders(){
    window.location.pathname = '/client/your_orders.html'
}

function placedOrders(id){
    localStorage.setItem('restaurant_id_instance',id)
    window.location.pathname = '/client/placed_orders.html'
}

function editProfile(){
    window.location.pathname = '/client/editProfile.html'
}