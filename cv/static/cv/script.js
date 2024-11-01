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