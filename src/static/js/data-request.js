function submitForm(event) {
    event.preventDefault(); 
    var value1 = document.getElementById('currency1').value;
    var value2 = document.getElementById('currency2').value;
    var xhr = new XMLHttpRequest();
    var body = 'http://127.0.0.1:8000/currency/add_track/' + encodeURIComponent(value1) +'-' + encodeURIComponent(value2);
    xhr.open('POST', 'http://127.0.0.1:8000/currency/add_track/' + encodeURIComponent(value1) +'-' + encodeURIComponent(value2), true);
    xhr.send();
}

function refreshValue(currency, buttonElement) {
    const currency_value = document.getElementsByClassName(`${currency}-value`);
    let values = currency.split('-');
    fetch(`http://127.0.0.1:8000/currency/value/?first_currency=${values[0]}&second_currency=${values[1]}`)
      .then(response => response.json())
      .then(data => {
        currency_value.textContent = data.value;
      })
      .catch(error => {
        console.error(`Ошибка при получении значения курса ${currency}`, error);
      });
  }