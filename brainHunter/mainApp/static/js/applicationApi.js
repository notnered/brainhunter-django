const btnsAnswer = document.querySelectorAll('#btnAnswer');

// const number = 1;
// const fetchFunction = () => {
//     const result = fetch(`${location.origin}/api/application/${number}`);
//     result.then((data) => {
//         data = data.json();
//         return data;
//     }).then((data) => {
//         console.log(data);
//     })
// }

// btnAnswer.addEventListener('click', fetchData);

// btnsAnswer.forEach((element) => {
//     element.addEventListener('click', fetchData(1));
// })

btnsAnswer.forEach((btn) => {
    btn.addEventListener('click', sendAnswer);
})

function sendAnswer(e){
    const applicationID = e.target.dataset.id;
    console.log(applicationID);
    fetchData(applicationID);
}

async function fetchData(id){
    const result = await fetch(`${location.origin}/api/application/${id}`);
    const data = await result.json();
    console.log(data);
}