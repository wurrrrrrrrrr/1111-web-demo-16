function showpage(index) {

    const p = document.querySelector('.show-classdemo');
    console.log('p',p);
    switch(index) {
        case 1:
            p.innerHTML = `<iframe src="./demo/w02/" width=100% height="100%" />`
            break;
        case 2:
            p.innerHTML = `<iframe src="./demo/w02/w03/card_16.html" width=100% height="100%" />`
            break;
        case 3:
            p.innerHTML = `<iframe src="./demo/w02/w05/blog_16.html" width=100% height="100%" />`
            break;
        case 4:
            p.innerHTML = `<iframe src="./demo/w02/w05/blog_16.html" width=100% height="100%" />`
            break;
        case 5:
            p.innerHTML = `<iframe src="./demo/w02/w08/landing_16.html" width=100% height="100%" />`
            break;
    }
}