document.addEventListener("DOMContentLoaded", () => {
    const dot = document.querySelector(".cursor-dot");
    const outline = document.querySelector(".cursor-outline");

    // Cursor Follow Logic
    window.addEventListener("mousemove", (e) => {
        const posX = e.clientX;
        const posY = e.clientY;

        dot.style.left = `${posX}px`;
        dot.style.top = `${posY}px`;

        // Smooth outline follow
        outline.animate({
            left: `${posX}px`,
            top: `${posY}px`
        }, { duration: 500, fill: "forwards" });
    });

    // Reveal Animation on Scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll(".animate").forEach(el => observer.observe(el));
});

const mobileToggle = document.getElementById('mobileToggle');
const navWrapper = document.getElementById('navWrapper');

if (mobileToggle) {
    mobileToggle.addEventListener('click', () => {
        navWrapper.classList.toggle('active');
        mobileToggle.classList.toggle('open');
    });
}

// Close menu if a link is clicked
document.querySelectorAll('.mobile-nav-links a').forEach(link => {
    link.addEventListener('click', () => {
        navWrapper.classList.remove('active');
    });
});

window.addEventListener('scroll', () => {
    const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrolled = (winScroll / height) * 100;
    document.querySelector('.scroll-progress').style.width = scrolled + "%";
});

const magnetBtn = document.querySelector('.cta-nav');

window.addEventListener('mousemove', (e) => {
    const rect = magnetBtn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;

    // Only move if the mouse is within 100px of the button
    if (Math.abs(x) < 100 && Math.abs(y) < 100) {
        magnetBtn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
    } else {
        magnetBtn.style.transform = `translate(0, 0)`;
    }
});