console.log("hello world");

var updateBtns = document.getElementsByClassName('update-cart')



for(i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
        product=this.dataset.product
        action=this.dataset.action
        orderupdate(product,action);
    })
}


function orderupdate(product,action){
    console.log("active")
    var url = 'http://127.0.0.1:8000/api/orderitem/1/'
    fetch(url, {
				method:'POST',
				headers:{
					'Content-type':'application/json',
					'X-CSRFToken':csrftoken,
				},
				body:JSON.stringify({'product':product,'action':action})
			}
			).then(function(response){
				console.log(response)
			})


}

