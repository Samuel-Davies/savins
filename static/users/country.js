document.addEventListener('DOMContentLoaded', () => {
    const selectDrop = document.querySelector('#countries');
    //const selectDrop = document.getElementById('countries');

    fetch('https://restcountries.com/v3.1/all').then(res =>{
        return res.json();
    }).then(data =>{
        console.log(data);
        let output = "";
        data.forEach(country => {
           // console.log(country.name);
           output += `<option>${country.name.common}</option>`;
        })

        selectDrop.innerHTML = output;
    }).catch(err =>{
        console.log(err);
    })
});