const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');
let intervalID; // Variable global para el identificador del intervalo

search.addEventListener('click', () => {
    const APIKey = '55231b3811071ae335e463006f206de0';
    const city = document.querySelector('.search-box input').value;

    if (city === '') return;

    fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${APIKey}&lang=es`)
        .then(response => response.json())
        .then(json => {
            if (json.cod === '404') {
                container.style.height = '400px';
                weatherBox.style.display = 'none';
                weatherDetails.style.display = 'none';
                error404.style.display = 'block';
                error404.classList.add('fadeIn');
                return;
            }

            error404.style.display = 'none';
            error404.classList.remove('fadeIn');

            const image = document.querySelector('.weather-box img');
            const temperature = document.querySelector('.weather-box .temperature');
            const description = document.querySelector('.weather-box .description');
            const humidity = document.querySelector('.weather-details .humidity span');
            const wind = document.querySelector('.weather-details .wind span');
            const timezone = document.querySelector('.weather-details .timezone span');

            switch (json.weather[0].main) {
                case 'Clear':
                    image.src = 'images/clear.png';
                    changeBackground('clear');
                    break;
                case 'Rain':
                    image.src = 'images/rain.png';
                    changeBackground('rain');
                    break;
                case 'Snow':
                    image.src = 'images/snow.png';
                    changeBackground('snow');
                    break;
                case 'Clouds':
                    image.src = 'images/cloud.png';
                    changeBackground('clouds');
                    break;
                case 'Haze':
                    image.src = 'images/mist.png';
                    changeBackground('mist');
                    break;
                default:
                    image.src = '';
                    changeBackground('default');
            }

            temperature.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
            description.innerHTML = `${json.weather[0].description}`;
            humidity.innerHTML = `${json.main.humidity}%`;
            wind.innerHTML = `${parseInt(json.wind.speed)}Km/h`;

            weatherBox.style.display = '';
            weatherDetails.style.display = '';
            weatherBox.classList.add('fadeIn');
            weatherDetails.classList.add('fadeIn');
            container.style.height = '590px';

            // Obtener la zona horaria
            const lat = json.coord.lat;
            const lon = json.coord.lon;
            fetch(`https://api.timezonedb.com/v2.1/get-time-zone?key=C5V5JCD3F77E&format=json&by=position&lat=${lat}&lng=${lon}`)
                .then(response => response.json())
                .then(timeData => {
                    const timezoneName = timeData.zoneName;
                    updateClock(timezoneName);
                });
        });
});

function changeBackground(weatherType) {
    let imageUrl = '';

    switch (weatherType) {
        case 'clear':
            imageUrl = 'url(images/despejado.png)';
            break;
        case 'rain':
            imageUrl = 'url(images/lluvia.jpg)';
            break;
        case 'snow':
            imageUrl = 'url(images/nieve.jpg)';
            break;
        case 'clouds':
            imageUrl = 'url(images/nubes.jpg)';
            break;
        case 'mist':
            imageUrl = 'url(images/niebla.jpg)';
            break;
        default:
            imageUrl = 'url(images/default.jpg)';
    }

    document.body.style.backgroundImage = imageUrl;
}

function updateClock(timezone) {
    const timezoneSpan = document.querySelector('.weather-details .timezone span');

    // Limpiar cualquier intervalo anterior
    if (intervalID) {
        clearInterval(intervalID);
    }

    function updateTime() {
        const now = new Date(new Date().toLocaleString('en-US', { timeZone: timezone }));
        const hours = now.getHours().toString().padStart(2, '0');
        const minutes = now.getMinutes().toString().padStart(2, '0');
        const seconds = now.getSeconds().toString().padStart(2, '0');
        timezoneSpan.innerHTML = `${hours}:${minutes}:${seconds}`;
    }

    updateTime();
    intervalID = setInterval(updateTime, 1000);
}
