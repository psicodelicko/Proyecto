(function() {
    'use strict';
    window.addEventListener('load', function() {
      // Fetch all the forms we want to apply custom Bootstrap validation styles to
      var forms = document.getElementsByClassName('needs-validation');
      // Loop over them and prevent submission
      var validation = Array.prototype.filter.call(forms, function(form) {
        form.addEventListener('submit', function(event) {
          if (form.checkValidity() === false) {
            event.preventDefault();
            event.stopPropagation();
            form.classList.add('was-validated');
          }else{
              event.preventDefault();
              event.stopPropagation();
              var fid = $(this).attr('id');
              var nextform = parseInt(fid)+1;
              var percent = nextform*33.3333333333;
              if(nextform==3){
                  percent=100;
              }
              $(".loader").show();
              $(".progress-bar").css("width", percent + '%');
              setTimeout(function(){
                  $(".step-"+fid).hide();
                  $(".step-"+nextform).show();
                  $(".loader").hide();				
              }, 2000);
          }
          
        }, false);
      });
    }, false);
  })();
  
  // For Reffered
  $(document).ready(function(){
    $(".reffered").click(function(){
          $(this).hide();
          $("#referral-code").show();
      });
      
      // Masking Numbers
      $(document).ready(function () {
          $('#phone').usPhoneFormat({
                  format: '(xxx) xxx-xxxx',
          });
          
          $('#ssn').usPhoneFormat();
  });
  
  });
  
  // For type number jQuery
  function maxLengthCheck(object){
      if (object.value.length > object.maxLength)
          object.value = object.value.slice(0, object.maxLength)
  }
  
  // For Masking Numbers
  
  (function ($) {
      $.fn.usPhoneFormat = function (options) {
              var params = $.extend({
                      format: 'xxx-xx-xxxx',
                      international: false,
  
              }, options);
  
              if (params.format === 'xxx-xx-xxxx') {
                      $(this).bind('paste', function (e) {
                              e.preventDefault();
                              var inputValue = e.originalEvent.clipboardData.getData('Text');
                              if (!$.isNumeric(inputValue)) {
                                      return false;
                              } else {
                                      inputValue = String(inputValue.replace(/(\d{3})(\d{2})(\d{4})/, "$1-$2-$3"));
                                      $(this).val(inputValue);
                                      $(this).val('');
                                      inputValue = inputValue.substring(0, 12);
                                      $(this).val(inputValue);
                              }
                      });
                      $(this).on('keypress', function (e) {
                              if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                                      return false;
                              }
                              var curchr = this.value.length;
                              var curval = $(this).val();
                              if (curchr == 3) {
                                      $(this).val(curval + "-");
                              } else if (curchr == 6) {
                                      $(this).val(curval + "-");
                              }
                              $(this).get(maxLengthCheck(object));
                      });
  
              } else if (params.format === '(xxx) xxx-xxxx') {
                      $(this).on('keypress', function (e) {
                              if (e.which != 8 && e.which != 0 && (e.which < 48 || e.which > 57)) {
                                      return false;
                              }
                              var curchr = this.value.length;
                              var curval = $(this).val();
                              if (curchr == 3) {
                                      $(this).val('(' + curval + ')' + " ");
                              } else if (curchr == 9) {
                                      $(this).val(curval + "-");
                              }
                              $(this).get(maxLengthCheck(object));
                      });
                      $(this).bind('paste', function (e) {
                              e.preventDefault();
                              var inputValue = e.originalEvent.clipboardData.getData('Text');
                              if (!$.isNumeric(inputValue)) {
                                      return false;
                              } else {
                                      inputValue = String(inputValue.replace(/(\d{3})(\d{3})(\d{4})/, "($1) $2-$3"));
                                      $(this).val(inputValue);
                                      $(this).val('');
                                      inputValue = inputValue.substring(0, 14);
                                      $(this).val(inputValue);
                              }
                      });
  
              }
      }
  }(jQuery));