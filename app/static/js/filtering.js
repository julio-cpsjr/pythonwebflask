function filter(){
   var input,
   filter,
   td,
   a,
   i,
   tab,
   txtValue,
   count = 0

   input = document.getElementById('inputBusca');
   tab = document.getElementById('table_helloworld_table');

   //Filtro
   filter = input.value.toUpperCase();
   
   //PEGAR TODAS TH DA TABLE
   td = tab.getElementsByTagName("td");

   for(i =0; i < th.lenght;i++){
        // PEGAR TAG A DENTRO DO ELEMENTO
        a = td[i].getElementsByTagName("a")[0]
        //PEGAR O TEXTO DENTRO DA TAG A 
        txtValue = a.textContent || a.innerText;
        //VERIFICAR SE O QUE O USUARIO DIGITOU
        if(txtValue.toUpperCase().indexOf(filter) > -1){
            //VALOR BATEU
            td[i].style.display = "";
            //INCREMENT O CONTADOR
            count ++;
            
        }else {
            td[i].style.display = "none";
        }
   }

   if(count === 0){
    tab.style.display = "none";
   } else {
    tab.style.display = "block";
   }
}