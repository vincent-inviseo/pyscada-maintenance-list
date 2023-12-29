// ----------------------------------------------------------------------------------------------
// TRI DU TABLEAU
// ----------------------------------------------------------------------------------------------

const headers = document.querySelectorAll('.header');

headers.forEach(header => {
    header.addEventListener('click', () => {
        const table = header.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(header.parentElement.children, header);
        const isAscending = header.classList.contains('ascending');
        sortTable(table, headerIndex, !isAscending);
    });
});

function sortTable(table, headerIndex, isAscending) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    // Comparaison de deux lignes
    const comparator = (row1, row2) => {
        const cell1 = row1.querySelectorAll('td')[headerIndex];
        const cell2 = row2.querySelectorAll('td')[headerIndex];
        const value1 = cell1.textContent.trim();
        const value2 = cell2.textContent.trim();
        return value1.localeCompare(value2, undefined, {numeric: true, sensitivity: 'base'});
    };

    // Tri des lignes
    rows.sort(comparator);
    if (!isAscending) {
        rows.reverse();
    }
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));

    table.querySelectorAll('.header').forEach(header => header.classList.remove('ascending', 'descending'));
    const header = table.querySelector(`.header:nth-child(${headerIndex + 1})`);
    if (isAscending) {
        header.classList.add('ascending');
    } else {
        header.classList.add('descending');
    }
}

// Tri par défaut quand on arrive sur la page
const table = document.querySelector('.maintenance-table');
const header = table.querySelector('.header');
sortTable(table, 0, false);
header.click();

// ----------------------------------------------------------------------------------------------
// FILTRES DU TABLEAU
// ----------------------------------------------------------------------------------------------

const referenceFilter = document.getElementById("reference-filter");
const nameFilter = document.getElementById("name-filter");
const typeFilter = document.getElementById("type-filter");
const periodicityFilter = document.getElementById("periodicity-filter");

referenceFilter.addEventListener("change", updateTable);
nameFilter.addEventListener("keyup", updateTable);
typeFilter.addEventListener("change", updateTable);
periodicityFilter.addEventListener("change", updateTable);

function updateTable() {
    // Récupérer les valeurs des filtres
    const referenceValue = referenceFilter.value;
    const nameValue = nameFilter.value.toUpperCase();
    const typeValue = typeFilter.value;
    const periodicityValue = periodicityFilter.value;

    const table = document.querySelector('.maintenance-table');
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    // Cacher les lignes qui ne correspondent pas aux filtres
    rows.forEach(row => {
        const reference = row.querySelectorAll('td')[1].textContent.trim();
        const name = row.querySelectorAll('td')[2].textContent.trim().toUpperCase();
        const type = row.querySelectorAll('td')[3].textContent.trim();
        const periodicity = row.querySelectorAll('td')[4].textContent.trim();

        const referenceMatch = reference.includes(referenceValue);
        const nameMatch = name.includes(nameValue);
        const typeMatch = type.includes(typeValue);
        const periodicityMatch = periodicity.includes(periodicityValue);

        if (!referenceMatch || !nameMatch || !typeMatch || !periodicityMatch) {
            row.style.display = 'none';
        } else {
            row.style.display = '';
        }
    });
}

// onclick() du bouton "Nettoyer les filtres"
function clearFilters() {
    referenceFilter.value = '';
    nameFilter.value = '';
    typeFilter.value = '';
    periodicityFilter.value = '';
    updateTable();
}

