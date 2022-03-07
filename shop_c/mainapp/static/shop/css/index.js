const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);


// active

// const currentLocation = location.href;
// const menuItem = document.querySelectorAll('a');
// const menuLength = menuItem.length
// for (let i = 0;i<menuLength;i++){
//     if (menuItem[i].href === currentLocation){
//         menuItem[i].className = "a:hover:after"
//     }
// }