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

$( document ).ready(function() {
    console.log( "ready!" );
    $("#keyword").keyup(function(e) {
        if($(this).val()==''){
console.log(1)
console.log( $("#buttonset").find('li[class="page-item active"]').children("button").attr("id") );
     var id=$("#buttonset").find('li[class="page-item active"]').children("button").attr("id")
     id=id.substring(2,3)
    $(`.list_data[id!=${id}]`).css("display","none")
}
    });
});