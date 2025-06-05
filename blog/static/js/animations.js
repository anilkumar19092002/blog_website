document.addEventListener('DOMContentLoaded', function() {
    // Enhanced button animations
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(btn => {
        btn.addEventListener('mouseenter', () => {
            btn.classList.add('animate__animated', 'animate__pulse');
        });
        btn.addEventListener('mouseleave', () => {
            btn.classList.remove('animate__animated', 'animate__pulse');
        });
    });

    // Staggered card animations
    const cards = document.querySelectorAll('.card');
    cards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
    });

    // Background parallax effect
    if (window.innerWidth > 768) {
        window.addEventListener('scroll', function() {
            const scrollPosition = window.pageYOffset;
            document.body.style.backgroundPositionY = `${scrollPosition * 0.5}px`;
        });
    }

    // Copy link button animation
    document.querySelectorAll('.copy-link').forEach(button => {
        button.addEventListener('click', function() {
            const url = this.getAttribute('data-url');
            navigator.clipboard.writeText(url).then(() => {
                const originalHTML = this.innerHTML;
                this.innerHTML = '<i class="fas fa-check"></i> Copied!';
                this.classList.add('btn-success');
                this.classList.remove('btn-outline-secondary');
                
                setTimeout(() => {
                    this.innerHTML = originalHTML;
                    this.classList.remove('btn-success');
                    this.classList.add('btn-outline-secondary');
                }, 2000);
            });
        });
    });
});