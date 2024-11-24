const scrollBarID = document.querySelector('#scrollBarID');
const scrollLeftID = document.querySelector('#scrollLeftID');
const scrollRightID = document.querySelector('#scrollRightID');

const TRAVEL_DISTANCE = 200;

function disappearLeftBtn(distance, btn, scrollWidth, visibleWidth){
    if (distance === 0){
        btn.style.display = 'none';
    } else {
        btn.style.display = 'flex';
    }
}

function disappearRightBtn(distance, btn, scrollWidth, visibleWidth){
    if (distance + visibleWidth === scrollWidth){
        btn.style.display = 'none';
    } else {
        btn.style.display = 'flex';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    let scrolledBy = scrollBarID.scrollLeft;
    const scrollWidth = scrollBarID.scrollWidth;
    let visibleWidth = Math.floor(scrollBarID.getBoundingClientRect().width);
    disappearLeftBtn(scrolledBy, scrollLeftID, scrollWidth, visibleWidth);
    disappearRightBtn(scrolledBy, scrollRightID, scrollWidth, visibleWidth);
})

scrollBarID.addEventListener('scroll', () => {
    let scrolledBy = scrollBarID.scrollLeft;
    const scrollWidth = scrollBarID.scrollWidth;
    let visibleWidth = Math.floor(scrollBarID.getBoundingClientRect().width);
    disappearLeftBtn(scrolledBy, scrollLeftID, scrollWidth, visibleWidth);
    disappearRightBtn(scrolledBy, scrollRightID, scrollWidth, visibleWidth);
})

scrollLeftID.addEventListener('click', () => {
    scrollBarID.scrollBy({
        left: -TRAVEL_DISTANCE,
        behavior: 'smooth'
    })
})

scrollRightID.addEventListener('click', () => {
    scrollBarID.scrollBy({
        left: TRAVEL_DISTANCE,
        behavior: 'smooth'
    })
})