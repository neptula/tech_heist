$(function () {
    $('#selectpickerid').selectpicker();



  });


  $(document).ready(function () {


    $('#selectpickerid').on('change', function () {
      var textDisplay = $('#selectpickerid option:selected').text();
      $("#hiddenSelected").val(textDisplay);
    })

  })


  $(document).ready(function () {

    var last_valid_selection = null;

    $('#selectpickerid').change(function (event) {

      if ($(this).val().length >= 5) {

        $(this).val(last_valid_selection);
      } else {
        last_valid_selection = $(this).val();
      }
    });
  });
