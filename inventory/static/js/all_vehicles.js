document.addEventListener('DOMContentLoaded', function () {
    console.log("JavaScript loaded");
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('click', () => {
            console.log("Card clicked");
            const vehicleId = card.getAttribute('data-id');
            if (vehicleId) {
                window.location.href = `/vehicles/${vehicleId}/`;
            }
        });
    });

    // Fade-in animation
    const faders = document.querySelectorAll('.fade-in');
    const appearOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };
    const appearOnScroll = new IntersectionObserver(function (entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.add('visible');
            observer.unobserve(entry.target);
        });
    }, appearOptions);

    faders.forEach(fader => {
        appearOnScroll.observe(fader);
    });
});
