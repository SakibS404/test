document.addEventListener('DOMContentLoaded', function() {
    const cardsContainer = document.getElementById('cards-container');
    const startDate = document.querySelector('.date-input:first-child');
    const endDate = document.querySelector('.date-input:last-child');
    const dateError = document.getElementById('date-error');

    // Sample data with updated titles
    const performanceData = [
        {
            title: 'Departments',
            onTrack: 60,
            atRisk: 25,
            offTrack: 15,
            buttonText: 'View All'
        },
        {
            title: 'Teams',
            onTrack: 45,
            atRisk: 35,
            offTrack: 20,
            buttonText: 'View Team'
        },
        {
            title: 'Card: Fun',
            onTrack: 70,
            atRisk: 20,
            offTrack: 10,
            buttonText: 'View Card'
        }
    ];

    function createCard(data) {
        const card = document.createElement('div');
        card.className = 'performance-card';
        
        // Calculate the maximum width available for bars (in pixels)
        const maxBarWidth = 250; // You can adjust this value based on your card width

        card.innerHTML = `
            <div class="card-header">
                ${data.title}
            </div>
            <div class="metrics">
                <div class="metric">
                    <div class="bar-container">
                        <div class="bar on-track" style="width: ${data.onTrack}%"></div>
                    </div>
                    <span>${data.onTrack}%</span>
                </div>
                <div class="metric">
                    <div class="bar-container">
                        <div class="bar at-risk" style="width: ${data.atRisk}%"></div>
                    </div>
                    <span>${data.atRisk}%</span>
                </div>
                <div class="metric">
                    <div class="bar-container">
                        <div class="bar off-track" style="width: ${data.offTrack}%"></div>
                    </div>
                    <span>${data.offTrack}%</span>
                </div>
            </div>
            <button class="view-button">
                ${data.buttonText} ▼
            </button>
        `;
        
        return card;
    }

    // Render cards
    performanceData.forEach(data => {
        cardsContainer.appendChild(createCard(data));
    });

    // Date validation
    function validateDates() {
        if (startDate.value && endDate.value) {
            const start = new Date(startDate.value);
            const end = new Date(endDate.value);
            if (start > end) {
                dateError.textContent = 'Invalid date';
                return false;
            }
            dateError.textContent = '';
            return true;
        }
        return true;
    }

    startDate.addEventListener('change', validateDates);
    endDate.addEventListener('change', validateDates);
});