// main.js

document.addEventListener("DOMContentLoaded", () => {

    // Fade-in effect for elements with class 'fade-in'
    const fadeElements = document.querySelectorAll(".fade-in");
    fadeElements.forEach(el => {
        el.classList.add("opacity-0");
        setTimeout(() => {
            el.classList.remove("opacity-0");
            el.style.transition = "opacity 0.5s ease, transform 0.5s ease";
            el.style.transform = "translateY(0)";
            el.style.opacity = 1;
        }, 50);
    });

    // Smooth scroll for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute("href"));
            if (target) {
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Simple toast notification
    window.showToast = function(message, type = "info") {
        const toast = document.createElement("div");
        toast.textContent = message;
        toast.className = `fixed bottom-6 right-6 px-4 py-2 rounded-lg shadow-lg transition-all duration-500 
            ${type === "success" ? "bg-green-500" : type === "error" ? "bg-red-500" : "bg-indigo-500"} text-white`;
        document.body.appendChild(toast);
        setTimeout(() => {
            toast.style.opacity = 0;
            toast.style.transform = "translateY(20px)";
        }, 3000);
        setTimeout(() => document.body.removeChild(toast), 3500);
    }

    // Example usage: showToast("Welcome back!", "success");

});
