let today = new Date();
let currentMonth = today.getMonth();
let currentYear = today.getFullYear();
let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
let calendarValues = []; // Array to store values for each date

showCalendar(currentMonth, currentYear);

function next() {
    currentYear = (currentMonth === 11) ? currentYear + 1 : currentYear;
    currentMonth = (currentMonth + 1) % 12;
    showCalendar(currentMonth, currentYear);
}

function previous() {
    currentYear = (currentMonth === 0) ? currentYear - 1 : currentYear;
    currentMonth = (currentMonth === 0) ? 11 : currentMonth - 1;
    showCalendar(currentMonth, currentYear);
}


function showCalendar(month, year) {
    let firstDay = (new Date(year, month)).getDay();
    let daysInMonth = 32 - new Date(year, month, 32).getDate();

    let tbl = document.getElementById("calendar-body");
    tbl.innerHTML = ""; // Clear previous days

    monthAndYear.innerHTML = months[month] + " " + year;
    
    let date = 1;
    for (let i = 0; i < 6; i++) {
        let row = document.createElement("tr");
        
        for (let j = 0; j < 7; j++) {
            if (i === 0 && j < firstDay) {
                let cell = document.createElement("td");
                row.appendChild(cell);
            }
            else if (date > daysInMonth) {
                break;
            }
            else {
                let cell = document.createElement("td");
                let cellText = document.createTextNode(date);

                // Random color for each day
                let randomColor = getRandomColor();
                cell.style.backgroundColor = randomColor;

                cell.appendChild(cellText);
                row.appendChild(cell);
                date++;
            }
        }
        tbl.appendChild(row);
    }
}

// Function to get random color
function getRandomColor() {
    const colors = ['green', 'yellow', 'red', 'gray'];
    return colors[Math.floor(Math.random() * colors.length)];
}
