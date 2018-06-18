function api_call(input) {
    $.ajax({
        
	url: "http://0.0.0.0:5000/importantWords?url=http://www.fullychargedshow.co.uk/electric-cars/coal-is-king",
        method: 'GET'
    });
}

$( document ).ready(function() {
    // request when clicking on the button
    $('#btn').click(function() {
        var input = $("#input").val();
        api_call(input);
        input = "";
    });
});

