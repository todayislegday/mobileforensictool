function filter(){
    var name, i, j;

    var keyword = document.getElementById('keyword').value.toUpperCase()
    var list = document.getElementsByClassName('list_data')

    for(i=0; i<list.length; i++) {
        name = list[i].children;
        for(j=0; j<name.length; j++) {
            if(name[j].innerHTML.toUpperCase().indexOf(keyword)>-1) {
               list[i].style.display="";
               break;
            } else {
               list[i].style.display="none";
            }
        }
    }
}

