document.addEventListener("DOMContentLoaded", function() {
    const menuItems = document.querySelectorAll("#menu li a");

    menuItems.forEach(item => {
        item.addEventListener("mouseenter", function() {
            item.style.color = "#333";
            item.style.backgroundColor = "#64ff6c";
        });

        item.addEventListener("mouseleave", function() {
            item.style.color = "white";
            item.style.backgroundColor = "";
        });
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const currentYearElement = document.getElementById("current-year");
    const currentYear = new Date().getFullYear();
    currentYearElement.textContent = currentYear;
});

// funkce pro přechod na další nebo předchozí stránku Hearthstone
document.addEventListener("DOMContentLoaded", () => {
    const prevPageButton = document.getElementById("prevPage");
    const nextPageButton = document.getElementById("nextPage");
    let currentPage = new URLSearchParams(window.location.search).get("page") || 1;

    prevPageButton.addEventListener("click", () => {
        if (currentPage > 1) {
            window.location.href = `/hearthstone/?page=${parseInt(currentPage) - 1}`;
        }
    });

    nextPageButton.addEventListener("click", () => {
        window.location.href = `/hearthstone/?page=${parseInt(currentPage) + 1}`;
    });
});
