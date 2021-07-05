$(function() {
    $('#date_range').datepicker({
      range: 'period',
      numberOfMonths: 1,
      
      onSelect: function(dateText, inst, extensionRange) {
      }
    });
  });