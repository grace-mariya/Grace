const convertForm = document.getElementById('convert-form');
const convertBtn = document.getElementById('convert-btn');
const resultDiv = document.getElementById('result');


convertForm.addEventListener('submit', function(e)
{
    e.preventDefault();

const sourceCurrency = document.getElementById('source_currency').value;
const targetCurrency = document.getElementById('target_currency').value;
const amount = document.getElementById('amount').value;
const data =
{
    'source_currency': sourceCurrency,
    'target_currency': targetCurrency,
    'amount'         : amount
};

fetch('/convert',{
    method: 'POST',
    headers:{
        'Content-Type': 'application/json'

    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => {
    resultDiv.innerHTML = '<p>${result.amount} ${result.source_currency} is equal to ${result.converted_amount} ${result.target_currency}</p> ';
})
.catch(error => {
    resultDiv.innerHTML = '<p>Something went wrong. Please try again later.</p>';
    console.error(error);
});
});