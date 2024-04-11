async function loadRestaurants(){
    const elem = document.getElementById("fillRestaurants")
    elem.innerHTML = `<h3 class="text-center">Loading...</h3>`
    const response = await fetch("https://bookeat.xyz/api/restaurant/get_resturent/")
    const data = await response.json()
    console.log("data is ",data)
    if(data.status==="success"){
        console.log(data.data)
        const restaurantArray = Array.from(data.data)
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
                    <a class='common-btn' href='#' onclick="loadDetails(${restaurant.id})"><span>See Details <hello class="bi bi-eye"></hello></span></a>
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

async function lookupRestaur(e){
    e.preventDefault()
    const source = document.getElementById("sourceRestaur").value
    const destination = document.getElementById("destRestaur").value
    const elem = document.getElementById("fillRestaurants")
    elem.innerHTML = `<h3 class="text-center">Loading...</h3>`
    const response = await fetch("https://bookeat.xyz/api/restaurant/get_resturent/")
    const data = await response.json()
    console.log("data is ",data)
    if(data.status==="success"){
        console.log(data.data)
        const restaurantArray = Array.from(data.data)
        const filteredRestaurants = restaurantArray.filter((restaurant)=>{
            return restaurant.source?.toLowerCase().includes(source.toLowerCase()) && restaurant.destination?.toLowerCase().includes(destination.toLowerCase())
        });

        if (filteredRestaurants.length === 0) {
            elem.innerHTML = `<h3 class="text-center">No Restaurants Found</h3>`;
        } else {
            elem.innerHTML = `
            <div class="alert alert-success" role="alert">
                <strong>Restaurants Found</strong> ${filteredRestaurants.length} Restaurants Found from <strong>${source}</strong> to <strong>${destination}</strong>, <a href="#" class="text-end" onclick="loadRestaurants()"><u>Clear Search<u></a>
            </div>
            ` 
            elem.innerHTML += filteredRestaurants.map((restaurant)=>{
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
                        <a class='common-btn' href='#' onclick="loadDetails(${restaurant.id})"><span>See Details <hello class="bi bi-eye"></hello></span></a>
                    </div>
                </div>
            </div>
                `;
            }).join("");
        }
    }
    
        else if(data.status==="failed"){
            const elem = document.getElementById("fillRestaurants")
            elem.innerHTML = `<h3 class="text-center">No Restaurants Found</h3>`
        }
}

loadRestaurants()

async function loadDetails(id){
    let elem = document.getElementById("fillRestaurants")
    elem.innerHTML = `<h3 class="text-center">Loading...</h3>`
    const response  = await fetch(`https://bookeat.xyz/api/restaurant/get_resturent_menu/`,{
        method:"POST",
        body:JSON.stringify({
            id
        })
    })
    const data = await response.json()
    console.log(data)
    if(data.status==="success"){
    elem.innerHTML = `<div class="menu-book-box-wrap" id="menu-book" id= "menu" style= "box-shadow: 27px 21px 18px 13px rgba(133,133,133,1);"></div>`
    elem = document.getElementById("menu-book")
        const menus = Array.from(data.data)
        elem.innerHTML = menus.map((menu)=>{
            return `
            
            <div class="menu-book-box d-flex justify-content-between align-items-center" ${!menu.stock ? `style= "background: #e7e7e7; "` : ""}>
            <div class="menu-book-info-wrap d-flex flex-column flex-xl-row align-items-xl-center">
               <div class="menu-book-img flex-shrink-0">
                  <img class="w-100" src="assets/images/food-menu/menu-book-11.png" alt="">
               </div>
               <div class="menu-book-info">
                  <h2 class="h2 mb-1">${menu.name}</h2>
                ${menu.stock ? `<i style="font-size: large; color: gray;" class="text-success">In Stock</i>` : ""}
               </div>
            </div>
            <div class="dots"></div>
            <div class="menu-book-price">
               <h2>₹${menu.price}</h2>
            </div>
         </div>
            `
        }).join("")
    
        elem = document.getElementById("fillRestaurants")
        elem.innerHTML += ` <div class="col-12 text-center mt-4"> <a class="common-btn" onclick="loadRestaurants()"><span>Back <hello class="bi bi-arrow-left"></hello></span></a>
        <a class="common-btn" onclick="bookTable(${id})"><span>Book Table &nbsp;<hello class="bi bi-cart"></hello></span></a>
        <a class="common-btn" onclick="orderPickup(${id})"><span>Preorder Food &nbsp;<hello class="bi bi-cart"></hello></span></a> </div>
        `
    }
    else if(data.status==="failed"){
        elem.innerHTML = `<h3 class="text-center">No Menus Found</h3>`
        elem.innerHTML += ` <div class="col-12 text-center mt-4"> <a class="common-btn" onclick="loadRestaurants()"><span>Back <hello class="bi bi-arrow-left"></hello></span></a> </div>`
    }
}

function bookTable(id){
    let elem = document.getElementById("fillRestaurants")
    document.getElementsByClassName("containerFull")[0] ? document.getElementsByClassName("containerFull")[0].remove() : ""
    elem.innerHTML += `
    <div class="containerFull">
    <div class="inner-container p-4 rounded" style="box-shadow: 0px 0px 8px 1px #0000002e;">
        <div class="alert alert-danger d-none" role="alert" id="alert">
            <strong id="msg-al">Oh snap!</strong> <span id="alert-message"></span>
        </div>
        <form onsubmit="paymentTable(event, ${id})" method="post" class="form-cont">
            <h3 class="text-center mb-2">Book Your Tables</h3><span class="text-center"> ( Max. Cpacity 4 ) </span>
            <label for="name">Your Name</label>
            <div class="input-cont">
                <i class="bx bx-user"></i><input type="text" id="name" placeholder="Your Name">
            </div>
            <!-- password -->
            <label for="noofpeople">Number Of Diners*</label>
            <div class="input-cont">
                <i class="bx bx-user"></i><input type="number" oninput="setTableCount(event)" id="noofpeople" placeholder="No of Diners">
            </div>
            <label for="tables">No of Tables?</label>
            <div class="input-cont" style="background: #e0e0e0;">
                <i class="bx bx-home"></i><input type="text" style="background: transparent;" id="tables" readonly placeholder="No of Tables">
            </div>
            <input id="submit" type="submit" value="Save Details">
        </form>
    </div>
</div>
    `
}

function setTableCount(e){
    console.log("enter")
    const elem = document.getElementById("tables")
    elem.value = Math.ceil(e.target.value/4)
}

function up(e,max, id) {
    e.preventDefault()
    const elem = document.getElementById(`label${id}`)
    if(elem.classList.contains("click_here")){
        console.log("called")
        document.getElementById(`myNumber${id}`).value = parseInt(document.getElementById(`myNumber${id}`).value) + 1;
        if (document.getElementById(`myNumber${id}`).value >= parseInt(max)) {
            document.getElementById(`myNumber${id}`).value = max;
        }
        let total = document.getElementById("total").innerHTML;
        total = parseInt(total) + parseInt(elem.innerHTML.split("₹")[1].split("/-")[0])
        document.getElementById("total").innerHTML = total;
    }
}
function down(e, min, id) {
    e.preventDefault()
    const elem = document.getElementById(`label${id}`)
    if(elem.classList.contains("click_here")){
        console.log("called")   
        document.getElementById(`myNumber${id}`).value = parseInt(document.getElementById(`myNumber${id}`).value) - 1;
        if (document.getElementById(`myNumber${id}`).value <= parseInt(min)) {
            document.getElementById(`myNumber${id}`).value = min;
        }
        let total = document.getElementById("total").innerHTML;
        total = parseInt(total) - parseInt(elem.innerHTML.split("₹")[1].split("/-")[0])
        document.getElementById("total").innerHTML = total;
    }
}


async function orderPickup(id){
    let elem = document.getElementById("fillRestaurants")
    document.getElementsByClassName("containerFull")[0] ? document.getElementsByClassName("containerFull")[0].remove() : ""
    elem.innerHTML += "<h3 class='text-center' id='loading'>Loading...</h3>"
    const response = await fetch(`https://bookeat.xyz/api/restaurant/get_resturent_menu/`,{
        method:"POST",
        body:JSON.stringify({
            id
        })
    })
    const data = await response.json()
    if (data.status === "success") {
            const menu_items = Array.from(data.data)
            const loader = document.getElementById("loading")
            loader.remove()
            elem.innerHTML += `
            <div class="containerFull">
            <div class="inner-container p-4 rounded" style="box-shadow: 0px 0px 8px 1px #0000002e;">
                <div class="alert alert-danger d-none" role="alert" id="alert">
                    <strong id="msg-al">Oh snap!</strong> <span id="alert-message"></span>
                </div>
                <form onsubmit="payOrder(event, ${id})" method="post" class="form-cont">
                    <h3 class="text-center mb-2">Preorder Food</h3>
                    <label for="name">Your Name</label>
                    <div class="input-cont">
                        <i class="bx bx-user"></i><input type="text" id="name" placeholder="Your Name">
                    </div>
                    <label for="name">Arrival Time (24h format): </label>
                    <div class="input-cont">
                        <i class="bx bx-user"></i><input type="time" required id="time" placeholder="Enter time of today only...">
                    </div>
                    <!-- select multiple -->
                    <label>Select Menu Items*</label>
                    
                    <div class="menu-items my-2" style="display: flex; flex-wrap: wrap; justify-content: space-between; width: 100%;">
                        ${
                            menu_items.map((menu)=>{
                                return `
                                <div class="menu-item my-2" style="width: 40%;">
                                    <input class="d-none" type="checkbox" id="menu${menu.id}" name="menu${menu.id}" value="menu${menu.id}">
                                    <label id="label${menu.id}" class="p-2 my-2 rounded" for="menu${menu.id}" style="width: 100%; box-shadow: 0px 0px 15px #0000003b;" onclick="selectMenu('label${menu.id}')">${menu.name} <span style="font-weight: bold; color: #ff9900;">₹${menu.price}/-</span></label>
                                    <div class="input-group">
                                        <div class="input-group-btn bg-danger">
                                            <button type="button" id="ifdown${menu.id}" class="btn btn-default" onclick=" down(event, '0', ${menu.id})"><span class="bx bx-minus text-white"></span></button>
                                        </div>
                                        <input style="padding: 0.7rem 0.5rem;" type="text" readonly id="myNumber${menu.id}" class="form-control input-number" value="0" />
                                        <div class="input-group-btn bg-success">
                                            <button type="button" id="ifup${menu.id}" class="btn btn-default" onclick="up(event, '10', ${menu.id})"><span class="bx bx-plus text-white"></span></button>
                                        </div>
                                    </div>
                                </div>
                                `
                            }).join("")
                        }
                    </div>
                    <button class="common-btn d-flex justify-content-center" id="submit" type="submit">Pay ₹<span id="total">0</span>/-</button>
                </form>
            </div>
        </div>
            `
    }
    else if(data.status==="failed"){
        elem.innerHTML = `<h3 class="text-center">No Menus Found</h3>`
        elem.innerHTML += ` <div class="col-12 text-center mt-4"> <a class="common-btn" onclick="loadRestaurants()"><span>Back <hello class="bi bi-arrow-left"></hello></span></a> </div>`
    }
}

function selectMenu(id){
    const elem = document.getElementById(id)
    elem.classList.toggle("click_here")
    const total = document.getElementById("total")
    let totalAmount = parseInt(total.innerHTML)
    if(elem.classList.contains("click_here")){
        document.getElementById("myNumber"+id.split("label")[1]).value = 1
        console.log("here")
        totalAmount += parseInt(elem.innerHTML.split("₹")[1].split("/-")[0])
    }
    else{
        console.log(totalAmount)
        let quantity = document.getElementById("myNumber"+id.split("label")[1]).value
        console.log(totalAmount - (parseInt(elem.innerHTML.split("₹")[1].split("/-")[0]) * parseInt(quantity)))
        totalAmount = totalAmount - (parseInt(elem.innerHTML.split("₹")[1].split("/-")[0]) * parseInt(quantity))
        document.getElementById("myNumber"+id.split("label")[1]).value = 0
    }
    total.innerHTML = totalAmount
}

async function paymentTable(e, resturent){
    e.preventDefault()
    const name = document.getElementById("name").value
    const tables = document.getElementById("tables").value
    const no_of_diners = document.getElementById("noofpeople").value
    const elem = document.getElementById("alert")
    const message = document.getElementById("alert-message")
    const msg_al = document.getElementById("msg-al")
    if(name.length===0 || tables.length===0 || no_of_diners.length===0){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Fill All The Fields"
        msg_al.innerHTML = "Oh Snap!"
        return
    }
    if(tables === "0"){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Enter Valid Number Of Diners"
        msg_al.innerHTML = "Oh Snap!"
        return
    }
    no_of_tables_shoud_be = Math.ceil(no_of_diners/4)
    if(tables !== no_of_tables_shoud_be.toString()){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Enter Valid Number Of Diners"
        msg_al.innerHTML = "Oh Snap!"
        return
    }

    const response = await fetch("https://bookeat.xyz/api/restaurant/get_table_amount/",{
        method:"POST",
        body:JSON.stringify({
            name,
            tables,
            no_of_diners,
            resturent
        })
    })
    const data = await response.json()
    console.log(data)
    if(data.status === "success"){
        const userDetails = localStorage.getItem("tokenAuth")
        console.log(userDetails, userDetails.id)
        const amount = data.data.amount
        const key_id = data.data.key_id
        const order_id = data.data.order_id
        var options = {
            "key": key_id, // Enter the Key ID generated from the Dashboard
            "amount": amount, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "BookEat", //your business name
            "description": "Make Purchase",
            "image": "./",
            "order_id": order_id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            // "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
            "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information especially their phone number
                "name": name, //your customer's name
                "contact": userDetails.phone //Provide the customer's phone number for better conversion rates 
            },
            "theme": {
                "color": "#3399cc"
            },
            handler : async (response)=>{
                // save the order
                const order_id = await response.razorpay_order_id
                const payment_id = await response.razorpay_payment_id
                const signature = await response.razorpay_signature
                const data = {
                    order_id,
                    payment_id,
                    signature,
                    amount,
                    customer : JSON.parse(userDetails).id,
                    restaurant : resturent,
                    no_of_diners,
                    tables,
                    is_paid : true,
                }
                console.log(data)
                const send_success_response = await fetch("https://bookeat.xyz/api/restaurant/create_customer_table_booking/",{
                    method:"POST",
                    body:JSON.stringify(data)
                })
                const send_success_data = await send_success_response.json()
                console.log(send_success_data)
                if(send_success_data.status==="success"){
                    elem.classList.remove("d-none")
                    message.innerHTML = "Your Table Has Been Booked"
                    msg_al.innerHTML = "Congrats!"
                    const alert = document.getElementById('alert');
                    alert.classList.replace('alert-danger', 'alert-success');
                    setTimeout(()=>{
                        elem.classList.add("d-none")
                    }, 5000)
                    // make fields empty
                    document.getElementById("name").value = ""
                    document.getElementById("tables").value = ""
                    document.getElementById("noofpeople").value = ""
                }
                else if(send_success_data.status==="failed"){
                    elem.classList.remove("d-none")
                    message.innerHTML = data.message
                    msg_al.innerHTML = "Oh Snap!"
                }
            }
        }
        var rzp1 = new Razorpay(options);
        rzp1.open();
    }
    else if(data.status === "failed"){
        elem.classList.remove("d-none")
        message.innerHTML = data.message
        msg_al.innerHTML = "Oh Snap!"
    }

}

async function payOrder(e, resturent){
    e.preventDefault()
    const name = document.getElementById("name").value
    const time = document.getElementById("time").value
    const elem = document.getElementById("alert")
    const message = document.getElementById("alert-message")
    const msg_al = document.getElementById("msg-al")
    const menu_items = document.getElementsByClassName("menu-item")
    const menu_items_array = Array.from(menu_items)
    const selected_menu_items = menu_items_array.filter((menu)=>{
        return menu.children[0].checked
    })
    if(name.length===0){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Fill All The Fields"
        msg_al.innerHTML = "Oh Snap!"
        return
    }

    if(time.length===0){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Enter Time"
        msg_al.innerHTML = "Oh Snap!"
        return
    }

    if(selected_menu_items.length===0){
        elem.classList.remove("d-none")
        message.innerHTML = "Please Select Atleast One Menu Item"
        msg_al.innerHTML = "Oh Snap!"
        return
    }
    const menu_items_ids = selected_menu_items.map((menu)=>{
        return {
            id : menu.children[0].id.split("menu")[1],
            quantity : document.getElementById("myNumber"+menu.children[0].id.split("menu")[1]).value
        }
    })

    const response = await fetch("https://bookeat.xyz/api/restaurant/get_order_amount/",{
        method:"POST",
        body:JSON.stringify({
            menu_items_ids,
            resturent
        })
    })
    const data = await response.json()
    console.log(data)

    if(data.status === "success"){
        const userDetails = localStorage.getItem("tokenAuth")
        console.log(userDetails, userDetails.id)
        const amount = data.data.amount
        const key_id = data.data.key_id
        const order_id = data.data.order_id
        var options = {
            "key": key_id, // Enter the Key ID generated from the Dashboard
            "amount": amount, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
            "currency": "INR",
            "name": "BookEat", //your business name
            "description": "Make Purchase",
            "image": "./",
            "order_id": order_id, //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
            // "callback_url": "https://eneqd3r9zrjok.x.pipedream.net/",
            "prefill": { //We recommend using the prefill parameter to auto-fill customer's contact information especially their phone number
                "name": name, //your customer's name
                "contact": userDetails.phone //Provide the customer's phone number for better conversion rates 
            },
            "theme": {
                "color": "#3399cc"
            },
            handler : async (response)=>{
                // save the order
                const order_id = await response.razorpay_order_id
                const payment_id = await response.razorpay_payment_id
                const signature = await response.razorpay_signature
                const data = {
                    order_id,
                    payment_id,
                    signature,
                    amount,
                    time,
                    customer : JSON.parse(userDetails).id,
                    restaurant : resturent,
                    is_paid : true,
                    menu_items : menu_items_ids
                }
                console.log(data)
                const send_success_response = await fetch("https://bookeat.xyz/api/restaurant/create_customer_purchase/",{
                    method:"POST",
                    body:JSON.stringify(data)
                })
                const send_success_data = await send_success_response.json()
                console.log(send_success_data)
                if(send_success_data.status==="success"){
                    elem.classList.remove("d-none")
                    message.innerHTML = "Your Order Has Been Placed"
                    msg_al.innerHTML = "Congrats!"
                    const alert = document.getElementById('alert');
                    alert.classList.replace('alert-danger', 'alert-success');
                    setTimeout(()=>{
                        elem.classList.add("d-none")
                    }
                    , 5000)
                    // make fields empty
                    document.getElementById("name").value = ""
                    const menu_items = document.getElementsByClassName("menu-item")
                    const menu_items_array = Array.from(menu_items)
                    menu_items_array.forEach((menu)=>{
                        menu.children[0].checked = false
                        menu.classList.remove("click_here")
                    })
                }
                else if(send_success_data.status==="failed"){
                    elem.classList.remove("d-none")
                    message.innerHTML = data.message
                    msg_al.innerHTML = "Oh Snap!"
                }
            }
        }
        var rzp1 = new Razorpay(options);
        rzp1.open();
    }
}

async function searchRestaur(e) {
    e.preventDefault();
    const name = document.getElementById("sourceRestaur").value.trim(); // Retrieving restaurant name from the input field
    const elem = document.getElementById("fillRestaurants");
    elem.innerHTML = `<h3 class="text-center">Loading...</h3>`;
    
    try {
        // Fetch restaurant data with the name parameter
        const response = await fetch(`https://bookeat.xyz/api/restaurant/get_resturent/?name=${name}`);
        const data = await response.json();
        
        if (data.status === "success") {
            console.log(data.data);
            const restaurantArray = Array.from(data.data);
            
            const filteredRestaurants = restaurantArray.filter((restaurant) => {
                // Filter restaurants by name
                return restaurant.name.toLowerCase().includes(name.toLowerCase());
            });

            if (filteredRestaurants.length === 0) {
                elem.innerHTML = `<h3 class="text-center">No Restaurants Found</h3>`;
            } else {
                elem.innerHTML = `
                <div class="alert alert-success" role="alert">
                    <strong>Restaurants Found</strong> ${filteredRestaurants.length} Restaurants Found with name <strong>${name}</strong>, <a href="#" class="text-end" onclick="loadRestaurants()"><u>Clear Search</u></a>
                </div>
                `;

                // Render filtered restaurants
                elem.innerHTML += filteredRestaurants.map((restaurant) => {
                    return `
                    <div class="col-sm-6 col-lg-4 col-xl-6 wow fadeIn" data-wow-delay=".3s">
                        <div class="discount-menu-box d-flex flex-column flex-xl-row align-items-center">
                            <div class="discount-menu-img flex-shrink-0">
                                <img class="w-100" src="assets/images/food-menu/discount-1.png" alt="">
                            </div>
                            <div class="discount-menu-info">
                                <h2 class="h2">${restaurant.name}</h2>
                                
                                <p>${restaurant.address}</p>
                                ${restaurant.is_active ? `<span class="discount-price bg-success text-light p-2 rounded my-2 d-inline-block">Open</span>` : `<span class="discount-price bg-danger text-light p-2 rounded my-2 d-inline-block">Closed</span>`}
                                ${restaurant.tables_available ? `<span class="discount-price text-success d-inline-block">Tables Available (${restaurant.tables_available})</span>` : `<span class="discount-price text-danger p-2 d-inline-block">No Tables Available</span>`}
                                <a class='common-btn' href='#menu' onclick="loadDetails(${restaurant.id})"><span>See Details <hello class="bi bi-eye"></hello></span></a>
                            </div>
                        </div>
                    </div>`;
                }).join("");
            }
        } else if (data.status === "failed") {
            elem.innerHTML = `<h3 class="text-center">No Restaurants Found</h3>`;
        }
    } catch (error) {
        console.error("Error fetching restaurant data:", error);
        elem.innerHTML = `<h3 class="text-center">An error occurred while fetching data. Please try again later.</h3>`;
    }
}