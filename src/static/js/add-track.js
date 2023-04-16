
const trackAddOperation = () => {
    var value1 = document.getElementById('currency1').value;
    var value2 = document.getElementById('currency2').value;
    var xhr = new XMLHttpRequest();
    var body = 'first_currency=' + encodeURIComponent(value1) +'&second_currency=' + encodeURIComponent(value2);
    xhr.open('POST', 'http://127.0.0.1:8000/currency/add_track/?first_currency=' + encodeURIComponent(value1) +'&second_currency=' + encodeURIComponent(value2), true);
    xhr.send();
}
   
function submitForm(event) {
    event.preventDefault(); 
    var value1 = document.getElementById('currency1').value;
    var value2 = document.getElementById('currency2').value;
    var xhr = new XMLHttpRequest();
    var body = 'first_currency=' + encodeURIComponent(value1) +'&second_currency=' + encodeURIComponent(value2);
    xhr.open('POST', 'http://127.0.0.1:8000/currency/add_track/?first_currency=' + encodeURIComponent(value1) +'&second_currency=' + encodeURIComponent(value2), true);
    xhr.send();
  }