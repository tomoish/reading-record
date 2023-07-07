
/* 
LOADING
====================================================*/
window.addEventListener('load', () => {
    const loadingAreaSakura = document.querySelector('#loading-screen');
    const loadingLogo = document.querySelector('.loading-icon');

    setTimeout(() =>{
        loading.classList.add('loaded');
    }, 1500);

    loadingLogo.animate(
        [
            {
                opacity: 1,
                offset: .8,
            },
            {
                opacity: 0,
                offset: 1,
            },
        ],
        {
            duration: 1200,
            easing: 'ease',
            fill: 'forwards',
        }
    );

    loadingAreaSakura.animate(
        {
            translate: ['0 100vh', '0 0', '0 -100vh'],
        },
        {
            duration: 2000,
            delay: 800,
            easing: 'ease',
            fill: 'forwards',
        }
    );
});
