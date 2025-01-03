const btnsAnswer = document.querySelectorAll('#btnAnswer');

btnsAnswer.forEach((btn) => {
    btn.addEventListener('click', sendAnswer);
})

function sendAnswer(e){
    const applicationID = e.target.dataset.id;
    const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const answer = e.target.value;
    fetchData(applicationID, answer, csrf);
}

async function fetchData(id, newStatus, csrf){
    const result = await fetch(`${location.origin}/api/application/${id}`, {
        method: 'POST',
        headers: {
            "X-CSRFToken": csrf,
        },
        body: JSON.stringify({
            id: id,
            newStatus: newStatus,
        })
    });
    const data = await result.json();
    // console.log(data);
    location.reload();
}