document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.main-nav a');
    const sections = document.querySelectorAll('section');

    buttons.forEach(button => {
        button.addEventListener('click', () => {
            const target = button.getAttribute('section');

            sections.forEach(section => {
                if (section.className === target) {
                    section.classList.add('active');
                } else {
                    section.classList.remove('active');
                }
            });
        });
    });
});
