function quote(){
    document.getElementById("total").innerHTML = "";

    categoryValue = document.getElementById("category").value;
    countValue = document.getElementById("count").value;

    if (countValue > 1000) 
         { price = countValue / 100}
    else 
         {price = 10}
    if (categoryValue != "general") {price = price * 1.1}
    price = Math.round(price).toFixed(2);
    discount = (price / 100 * 80).toFixed(2);


  
  
    category = document.getElementById("category")
 

    count = document.getElementById("count")
    
  

    /*form validation */
    if (countValue <= 0)
         {count.classList.add('fill-error');}
    else
         {count.style.borderColor = "rgb(59, 55, 55)"; }
    
    if (categoryValue == "choose")
         { category.classList.add('fill-error');}
    else
         {category.style.borderColor = "rgb(59, 55, 55)"};

    setTimeout(function() {
              count.classList.remove('fill-error');
              category.classList.remove('fill-error')}, 400);
      if (countValue != 0 && categoryValue != "choose")  
         {document.getElementById("total").innerHTML = "Was" + "<span id=\"crossed\"> €" + price + "</span>"+"<span class=\"handwrite\"> Now only €" + discount + "</span>";}
        
  }




  
  function quote2(){
       category = document.getElementById("category");
       description = document.getElementById("id_description");
       file = document.getElementById("file_label");

       categoryValue = document.getElementById("category").value;
       descriptionValue = document.getElementById("id_description").value;
       fileValue = document.getElementById("file").value;

       if (categoryValue == "choose")
            { category.classList.add('fill-error'); category.style.borderColor = "red"}
          else
            {category.style.borderColor = "rgb(59, 55, 55)"};

       if (fileValue == "")
              { file.classList.add('fill-error'); file.style.borderColor = "red"}
           else
               {file.style.borderColor = "rgb(59, 55, 55)"};

        if (descriptionValue == "")
               { description.classList.add('fill-error'); description.style.borderColor = "red"}
            else
                {description.style.borderColor = "rgb(59, 55, 55)"};      
      
       setTimeout(function() {
          category.classList.remove('fill-error')
          description.classList.remove('fill-error')
          file.classList.remove('fill-error')}, 400);


       if (categoryValue != "choose" && descriptionValue != "" && fileValue != ""){
          document.getElementById("upload").click();
          
       };
  };