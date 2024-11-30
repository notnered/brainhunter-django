const modal = document.querySelector('#modal');
const closeModal = document.querySelector('#closeModal');
const vacancyID = document.querySelectorAll('#vacancyID');
const sendApplicationBtn = document.querySelectorAll('#sendApplicationBtn');

const formModal = document.querySelector('#formModal');
const modalName = document.querySelector('#modalName');
const modalSalary = document.querySelector('#modalSalary');
const modalLocation = document.querySelector('#modalLocation');
const modalCompany = document.querySelector('#modalCompany');
const coverLetter = document.querySelector('#coverLetter');


sendApplicationBtn.forEach((item) => {
    item.addEventListener('click', () => {
        let dataArray = (item.dataset.btnId).split(':');
        console.log(dataArray);
        openModal(dataArray);
    })
})


function openModal(data){
    formModal.action = `create-application/${data[0]}`
    modal.classList.remove('hidden');
    modalName.textContent = data[2];
    modalSalary.textContent = `${data[4]} руб.`;
    modalLocation.textContent = data[3];
    modalCompany.textContent = data[1];
}

// for (let i = 0; i < vacancyID.length; i++){
//     console.log(vacancyID[i].dataset.id);
// }

closeModal.addEventListener('click', () => {
    modal.classList.toggle('hidden');
})




