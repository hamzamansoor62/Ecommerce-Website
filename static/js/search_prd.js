let search_product = function () { 
    let input = document.getElementById('s').value
    
    //input=input.toLowerCase(); 
    let x = document.getElementsByClassName('product-name'); 
    // let x = y.querySelectorAll(".product-name");
    console.log(x[1].innerText)
    // x[0].style.display = "list-items"
    //document.write(input);
    for (i = 0; i < x.length; i++) {  
        if (!x[i].innerText.includes(input)) { 
            x[i].style.display="none"; 
        } 
        else { 
            x[i].style.display="inherit";                  
        } 
    } 
} 