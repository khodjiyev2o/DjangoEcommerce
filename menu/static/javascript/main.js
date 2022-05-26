console.log("hello world");

var updateBtns = document.getElementsByClassName('update-cart')



for(i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
        product=this.dataset.product
        action=this.dataset.action
        orderupdate(product,action);
    })
}



function orderupdate(productId, action){
	console.log('User is authenticated, sending data...')

		var url = 'api/orderitem/update/'

		fetch(url, {
			method:'POST',
			headers:{
				'Content-Type':'application/json',
				'X-CSRFToken':csrftoken,
			},
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		    location.reload()
		});
}

