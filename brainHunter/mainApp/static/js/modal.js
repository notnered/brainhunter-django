const modal = document.querySelector('#modal');
const closeModal = document.querySelector('#closeModal');
const vacancyID = document.querySelectorAll('#vacancyID');
const sendApplicationBtn = document.querySelectorAll('#sendApplicationBtn');

sendApplicationBtn.forEach((item) => {
    item.addEventListener('click', () => {
        console.log(item);
    })
})

for (let i = 0; i < vacancyID.length; i++){
    console.log(vacancyID[i].dataset.id);
}

closeModal.addEventListener('click', () => {
    modal.classList.toggle('hidden');
})

