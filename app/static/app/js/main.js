function openSearchField() {
    const search = document.getElementById('search');
    const animationName = 'search-animation'
    const animationCloseName = 'search-close-animation';

    if (search.classList.contains(animationName)) {
        search.classList.remove(animationName)
        search.classList.add(animationCloseName)

    }
    else {
        if (search.classList.contains(animationCloseName)) {
            search.classList.remove(animationCloseName);   
        }
        search.classList.add(animationName);
    }
}