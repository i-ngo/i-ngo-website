document.addEventListener("DOMContentLoaded", () => {
    const themeBtn = document.getElementById("theme-toggle-btn");
    
    if (!themeBtn) return;

    themeBtn.addEventListener("click", () => {
        const switchTheme = () => {
            const html = document.documentElement;
            const isNowDark = html.classList.toggle("dark");
            localStorage.setItem("theme", isNowDark ? "dark" : "light");
        };

        if (document.startViewTransition) {
            document.startViewTransition(switchTheme);
        } else {
            switchTheme();
        }
    });
});
