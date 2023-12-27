// 1. Récupérer les headers de colonne
const headers = document.querySelectorAll('.header');

// 2. Pour chaque header, ajouter un écouteur d'événement qui trie la table selon la colonne
headers.forEach(header => {
    header.addEventListener('click', () => {
        const table = header.parentElement.parentElement.parentElement;
        const headerIndex = Array.prototype.indexOf.call(header.parentElement.children, header);
        const isAscending = header.classList.contains('ascending');
        sortTable(table, headerIndex, !isAscending);
    });
});

// 3. Fonction de tri de la table
function sortTable(table, headerIndex, isAscending) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));

    // 3.1. Fonction de comparaison de deux lignes
    const comparator = (row1, row2) => {
        const cell1 = row1.querySelectorAll('td')[headerIndex];
        const cell2 = row2.querySelectorAll('td')[headerIndex];
        const value1 = cell1.textContent.trim();
        const value2 = cell2.textContent.trim();
        return value1.localeCompare(value2, undefined, {numeric: true, sensitivity: 'base'});
    };

    // 3.2. Tri des lignes
    rows.sort(comparator);
    if (!isAscending) {
        rows.reverse();
    }

    // 3.3. Remplacement des lignes dans le DOM
    tbody.innerHTML = '';
    rows.forEach(row => tbody.appendChild(row));

    // 3.4. Mise à jour des classes CSS
    table.querySelectorAll('.header').forEach(header => header.classList.remove('ascending', 'descending'));
    const header = table.querySelector(`.header:nth-child(${headerIndex + 1})`);
    if (isAscending) {
        header.classList.add('ascending');
    } else {
        header.classList.add('descending');
    }
}

// 4. Tri initial de la table
const table = document.querySelector('.maintenance-table');
const header = table.querySelector('.header');
sortTable(table, 0, true);
header.click();

