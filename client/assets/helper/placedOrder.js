function loadCustomerFoodItems(data2){
    const elem2 = document.getElementById('order-pickup')
    const table2 = elem2.querySelector('tbody')
    let sno2 = 1
    table2.innerHTML = ''
    data2.forEach((item)=>{
        const tr = document.createElement('tr')
        tr.innerHTML = `
            <td>${sno2}</td>
            <td>${item.user_name}</td>
            <td>${item.restaurant_name}</td>
            <td>${item.order_id}</td>
            <td class="text-success">₹${item.amount_paid}</td>
            <td>${item.time}</td>
            <td>
                <ul>
                    ${item.menu_items.map((items, index)=>{return `<li>${items} ( x ${item.quantity[index]}) </li>`})}
                </ul>
            </td>
        `
        table2.appendChild(tr)
        sno2++
    })
}

const loadRestaurantOrders = async (id)=>{
    console.log("hello")
    const response2 = await fetch(`https://bookeat.xyz/api/restaurant/get_customer_purchase_for_owner/`,{
        method: 'POST',
        body: JSON.stringify({
            id:id
        })
    })
    const data2 = await response2.json()
    console.log(data2)
    if(data2.status === 'success'){
        console.log("data in second",data2.data)
        console.log(data2.data)
        loadCustomerFoodItems(data2.data)
    }
}

function loadMyOrders(){
    const token = JSON.parse(localStorage.getItem('tokenAuth'))
    console.log("hello 1")
    if(token === null){
        window.location.pathname = "/client/siginin.html"
    }
    if(token === null){
        window.location.pathname = "/client/siginin.html"
    }
    if(token !== null && token.role === 'resturent_owner'){
        const restId = localStorage.getItem('restaurant_id_instance')
        loadRestaurantOrders(restId);
    }
}

loadMyOrders();
