$(document).ready(function() {
    $( "#slider-range" ).slider({
        range: true,
        min: 0,
        max: 200000,
        values: [ 50000, 140000 ],
        slide: function( event, ui ) {
          $( "#amount" ).val( "0 ₸ " + "            " + ui.values[ 0 ] + " ₸ " + "                        " + ui.values[ 1 ] + " ₸" );
        }
    });
    $( "#amount" ).val("0 ₸ " + "            " + $( "#slider-range" ).slider( "values", 0 ) + " ₸  " + "                        "
     + $( "#slider-range" ).slider( "values", 1 ) + " ₸" );
});