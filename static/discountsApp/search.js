$(document).ready(function() {

    document.getElementById("ProductsSearch").onsubmit = function() {doTheSearch()}
    console.log($('#searchKeyWord').val());
});

function doTheSearch(){

    var keyWord = {'keyWord':($('#searchKeyWord').val())}; 
    console.log(keyWord)

    $.ajax({

        url: $("#ProductsSearch").attr("action"),
        type: $("#ProductsSearch").attr("method"),
        //data:document.getElementById("ProductsSearch").value,
        data: getFormData($("#ProductsSearch")),
        //data: keyWord,

        success: function(data) {
            console.log(data.keyWord) 
        },
        error: function(data){
            console.log('sth worng')
        }

    }); 


};

function getFormData($form) {
    var unindexed_array = $form.serializeArray();
    var indexed_array = {};
    $.map(unindexed_array, function(n, i) {
      indexed_array[n["name"]] = n["value"];
    });
    return indexed_array;
  }