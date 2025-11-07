// Logging
const log = (msg, data = null) => {
    const prefix = `[${new Date().toLocaleTimeString()}]`;
    if (data) console.log(prefix, msg, data);
    else console.log(prefix, msg);
};

// State
const state = {
    meta: null,
    summary: null,
    categoryData: null,
    sparklineData: null,
    selectedYear: '2024',
    selectedCategory: 'personal',
    selectedUniversities: new Set(),
    aggregationMode: 'sum',
    sortMode: 'alpha'
};

// University type mapping
const uniTypes = {
    'voll': ['UA', 'UB', 'UC', 'UD', 'UE', 'UF'],
    'tech': ['UG', 'UH', 'UI'],
    'kunst': ['UJ', 'UK', 'UL', 'UM', 'UO', 'UQ'],
    'med': ['US', 'UT', 'UU'],
    'special': ['UN', 'UV', 'UW', 'UR']
};

const uniTypeLabels = {
    'voll': 'Volluniversitäten',
    'tech': 'Technische Universitäten',
    'kunst': 'Künstlerische Universitäten',
    'med': 'Medizinische Universitäten',
    'special': 'Spezialisierte Universitäten'
};

const uniTypeIcons = {
    'voll': 'fa-university',
    'tech': 'fa-microchip',
    'kunst': 'fa-palette',
    'med': 'fa-user-md',
    'special': 'fa-graduation-cap'
};

// Initialize
async function init() {
    try {
        log('Init start');
        await loadInitialData();
        await loadCategoryData(state.selectedCategory);
        renderUniversityFilters();
        renderOverview();
        attachEventListeners();
        log('Init complete');
    } catch (error) {
        console.error('Initialisierungsfehler:', error);
        alert('Fehler beim Laden der Daten');
    }
}

// Load data
async function loadInitialData() {
    log('Load meta + summary');
    const [metaRes, summaryRes] = await Promise.all([
        fetch('data/meta.json'),
        fetch('data/summary.json')
    ]);

    state.meta = await metaRes.json();
    state.summary = await summaryRes.json();

    // Initialize all universities as selected
    Object.keys(state.meta.universities).forEach(code => {
        state.selectedUniversities.add(code);
    });
    log(`Loaded ${Object.keys(state.meta.universities).length} unis`);
}

async function loadCategoryData(category) {
    log(`Load category: ${category}`);
    showLoading();
    try {
        const res = await fetch(`data/categories/${category}.json`);
        state.categoryData = await res.json();
        log(`Category loaded`, Object.keys(state.categoryData));

        extractSparklineData(category);

        hideLoading();
    } catch (error) {
        console.error('Fehler beim Laden der Kategorie:', error);
        hideLoading();
        throw error;
    }
}

function extractSparklineData(category) {
    state.sparklineData = {};

    const categoryMapping = {
        'personal': 'koepfe',
        'studierende': 'gesamt',
        'neuzulassungen': 'gesamt',
        'studien': 'gesamt',
        'abschluesse': 'gesamt',
        'mobilitaet': 'gesamt',
        'infrastruktur': 'gesamt',
        'berufungen': 'gesamt',
        'frauenquote-kollegialorgane': 'gesamt',
        'gender-pay-gap': 'gesamt',
        'professorinnen-aequivalente': 'gesamt',
        'eingerichtete-studien': 'gesamt',
        'besondere-zulassungsbedingungen': 'gesamt',
        'belegte-ordentliche-studien': 'gesamt',
        'outgoing-studierende': 'gesamt',
        'incoming-studierende': 'gesamt',
        'doktoratsstudierende': 'gesamt',
        'ausserordentliche-abschluesse': 'gesamt',
        'ordentliche-abschluesse': 'gesamt'
    };

    const dataKey = categoryMapping[category];
    if (!state.categoryData || !state.categoryData[dataKey]) return;

    let maxValue = 0;

    Object.keys(state.meta.universities).forEach(code => {
        const uniData = state.categoryData[dataKey][code];
        if (!uniData) return;

        const firstCategory = Object.keys(uniData)[0];
        if (!firstCategory) return;

        const yearData = uniData[firstCategory];
        const values = extractYearValues(yearData);

        state.sparklineData[code] = values;

        maxValue = Math.max(maxValue, values.y2022, values.y2023, values.y2024);
    });

    state.sparklineData.maxValue = maxValue;
    log(`Sparkline data extracted, max: ${maxValue}`);
}

// Render functions
function renderUniversityFilters() {
    const container = document.getElementById('university-filters');
    container.innerHTML = '';

    Object.entries(uniTypes).forEach(([type, codes]) => {
        const typeLabel = document.createElement('div');
        typeLabel.className = 'uni-type-label';
        typeLabel.textContent = uniTypeLabels[type];
        container.appendChild(typeLabel);

        codes.forEach(code => {
            if (state.meta.universities[code]) {
                const wrapper = document.createElement('div');
                wrapper.className = 'filter-checkbox';

                const checkbox = document.createElement('input');
                checkbox.type = 'checkbox';
                checkbox.id = `uni-${code}`;
                checkbox.value = code;
                checkbox.checked = state.selectedUniversities.has(code);
                checkbox.addEventListener('change', handleUniversityFilterChange);

                const label = document.createElement('label');
                label.htmlFor = `uni-${code}`;
                label.innerHTML = `<span class="color-indicator ${type}"></span>${state.meta.universities[code]}`;

                wrapper.appendChild(checkbox);
                wrapper.appendChild(label);
                container.appendChild(wrapper);
            }
        });
    });
}

function renderOverview() {
    const grid = document.getElementById('university-grid');
    grid.innerHTML = '';

    const universities = getFilteredUniversities();
    const sortedUniversities = sortUniversities(universities);

    sortedUniversities.forEach(code => {
        const card = createUniversityCard(code);
        grid.appendChild(card);
    });
}

function createUniversityCard(code) {
    const card = document.createElement('div');
    card.className = 'university-card';
    card.dataset.code = code;

    const type = getUniversityType(code);

    const categoryConfig = {
        'personal': { key: 'personal_koepfe', label: 'Personal (Köpfe)' },
        'studierende': { key: 'studierende', label: 'Ordentliche Studierende' },
        'neuzulassungen': { key: 'neuzulassungen', label: 'Neuzulassungen' },
        'studien': { key: 'studien', label: 'Studien' },
        'abschluesse': { key: 'abschluesse', label: 'Abschlüsse' },
        'mobilitaet': { key: 'mobilitaet', label: 'Outgoing-Studierende' },
        'infrastruktur': { key: 'infrastruktur', label: 'Nutzfläche m²' },
        'berufungen': { key: 'berufungen', label: 'Berufungen gesamt' },
        'frauenquote-kollegialorgane': { key: 'frauenquote_kollegialorgane', label: 'Frauenquote Kollegialorgane %' },
        'gender-pay-gap': { key: 'gender_pay_gap', label: 'Gender Pay Gap %' },
        'professorinnen-aequivalente': { key: 'professorinnen_aequivalente', label: 'Professorinnen-Äquivalente' },
        'eingerichtete-studien': { key: 'eingerichtete_studien', label: 'Eingerichtete Studien' },
        'besondere-zulassungsbedingungen': { key: 'besondere_zulassungsbedingungen', label: 'Besondere Zulassungsbedingungen' },
        'belegte-ordentliche-studien': { key: 'belegte_ordentliche_studien', label: 'Belegte ordentliche Studien' },
        'outgoing-studierende': { key: 'outgoing_studierende_wb', label: 'Outgoing-Studierende (WB)' },
        'incoming-studierende': { key: 'incoming_studierende', label: 'Incoming-Studierende' },
        'doktoratsstudierende': { key: 'doktoratsstudierende', label: 'Doktoratsstudierende mit BV' },
        'ausserordentliche-abschluesse': { key: 'ausserordentliche_abschluesse', label: 'Außerordentliche Abschlüsse' },
        'ordentliche-abschluesse': { key: 'ordentliche_abschluesse_wb', label: 'Ordentliche Abschlüsse (WB)' }
    };

    const config = categoryConfig[state.selectedCategory] || { key: null, label: 'N/A' };
    const value = config.key ? (state.summary[code]?.[config.key] || 0) : 0;
    const label = config.label;
    const icon = uniTypeIcons[type];

    let sparklineHTML = '';
    if (state.sparklineData && state.sparklineData[code] && state.sparklineData.maxValue > 0) {
        const values = state.sparklineData[code];
        const max = state.sparklineData.maxValue;
        const h2022 = (values.y2022 / max) * 100;
        const h2023 = (values.y2023 / max) * 100;
        const h2024 = (values.y2024 / max) * 100;

        sparklineHTML = `
            <div class="sparkline">
                <div class="sparkline-bar" style="height: ${h2022}%;" title="2022: ${formatNumber(values.y2022)}"></div>
                <div class="sparkline-bar" style="height: ${h2023}%;" title="2023: ${formatNumber(values.y2023)}"></div>
                <div class="sparkline-bar" style="height: ${h2024}%;" title="2024: ${formatNumber(values.y2024)}"></div>
            </div>
        `;
    }

    card.innerHTML = `
        <div class="university-card-header">
            <div class="university-name">${state.meta.universities[code]}</div>
            <div class="university-type-badge ${type}" title="${uniTypeLabels[type]}">
                <i class="fa-solid ${icon}"></i>
            </div>
        </div>
        <div class="university-value">${formatNumber(value)}</div>
        <div class="university-label">${label}</div>
        ${sparklineHTML}
    `;

    card.addEventListener('click', () => handleCardClick(code));

    return card;
}

async function handleCardClick(code) {
    if (!state.categoryData) {
        await loadCategoryData(state.selectedCategory);
    }

    renderDetailView(code);
}

function renderDetailView(code) {
    const detailContent = document.getElementById('detail-content');
    const overviewView = document.getElementById('overview-view');
    const detailView = document.getElementById('detail-view');

    overviewView.classList.remove('active');
    detailView.classList.add('active');

    let tableHTML = `<h2>${state.meta.universities[code]}</h2>`;

    if (state.selectedCategory === 'personal') {
        const data = state.categoryData?.koepfe?.[code] || {};
        const categories = Object.keys(data);

        tableHTML += `
            <table class="detail-table">
                <thead>
                    <tr>
                        <th>Kategorie</th>
                        <th>2022</th>
                        <th>2023</th>
                        <th>2024</th>
                        <th>Veränderung</th>
                    </tr>
                </thead>
                <tbody>
        `;

        categories.forEach(category => {
            const years = data[category];
            const values = extractYearValues(years);
            const change = values.y2024 - values.y2022;
            const changePercent = values.y2022 ? ((change / values.y2022) * 100).toFixed(1) : 0;

            tableHTML += `
                <tr>
                    <td>${category}</td>
                    <td>${formatNumber(values.y2022)}</td>
                    <td>${formatNumber(values.y2023)}</td>
                    <td>${formatNumber(values.y2024)}</td>
                    <td>${change >= 0 ? '+' : ''}${formatNumber(change)} (${changePercent}%)</td>
                </tr>
            `;
        });

        tableHTML += '</tbody></table>';
    } else {
        const dataKey = state.selectedCategory === 'studierende' ? 'gesamt' : 'gesamt';
        const data = state.categoryData?.[dataKey]?.[code] || {};
        const categories = Object.keys(data);

        tableHTML += `
            <table class="detail-table">
                <thead>
                    <tr>
                        <th>Kategorie</th>
                        <th>Wert</th>
                    </tr>
                </thead>
                <tbody>
        `;

        categories.forEach(category => {
            const values = data[category];

            if (typeof values === 'object' && values !== null) {
                Object.entries(values).forEach(([key, value]) => {
                    tableHTML += `
                        <tr>
                            <td>${category} - ${key}</td>
                            <td>${formatNumber(value)}</td>
                        </tr>
                    `;
                });
            } else {
                tableHTML += `
                    <tr>
                        <td>${category}</td>
                        <td>${formatNumber(values)}</td>
                    </tr>
                `;
            }
        });

        tableHTML += '</tbody></table>';
    }

    detailContent.innerHTML = tableHTML;

    updateBreadcrumb(['Übersicht', state.meta.universities[code]]);
}

function extractYearValues(years) {
    const values = { y2022: 0, y2023: 0, y2024: 0 };

    Object.entries(years).forEach(([key, value]) => {
        if (key.includes('Studienjahr 2023/24') || key.includes('WS 2024') || (key.includes('2024') && !key.includes('2023/24'))) {
            values.y2024 = value;
        } else if (key.includes('Studienjahr 2022/23') || key.includes('WS 2023') || (key.includes('2023') && !key.includes('2022/23') && !key.includes('2023/24'))) {
            values.y2023 = value;
        } else if (key.includes('Studienjahr 2021/22') || key.includes('WS 2022') || (key.includes('2022') && !key.includes('2021/22') && !key.includes('2022/23'))) {
            values.y2022 = value;
        }
    });

    return values;
}

// Helper functions
function getFilteredUniversities() {
    return Array.from(state.selectedUniversities);
}

function sortUniversities(universities) {
    const sorted = [...universities];

    const categoryKeys = {
        'personal': 'personal_koepfe',
        'studierende': 'studierende',
        'neuzulassungen': 'neuzulassungen',
        'studien': 'studien',
        'abschluesse': 'abschluesse',
        'mobilitaet': 'mobilitaet',
        'infrastruktur': 'infrastruktur'
    };

    switch (state.sortMode) {
        case 'alpha':
            sorted.sort((a, b) => state.meta.universities[a].localeCompare(state.meta.universities[b]));
            break;
        case 'value':
            sorted.sort((a, b) => {
                const key = categoryKeys[state.selectedCategory];
                const valA = key ? (state.summary[a]?.[key] || 0) : 0;
                const valB = key ? (state.summary[b]?.[key] || 0) : 0;
                return valB - valA;
            });
            break;
        case 'change':
            sorted.sort((a, b) => a.localeCompare(b));
            break;
    }

    return sorted;
}

function getUniversityType(code) {
    for (const [type, codes] of Object.entries(uniTypes)) {
        if (codes.includes(code)) return type;
    }
    return 'voll';
}

function formatNumber(num) {
    if (!num) return '0';
    return Math.round(num).toLocaleString('de-AT');
}

function updateBreadcrumb(items) {
    const breadcrumb = document.querySelector('.breadcrumb');
    breadcrumb.innerHTML = items.map((item, i) => {
        const isLast = i === items.length - 1;
        return `<span class="breadcrumb-item ${isLast ? 'active' : ''}" data-index="${i}">${item}</span>`;
    }).join(' > ');

    breadcrumb.querySelectorAll('.breadcrumb-item').forEach(item => {
        item.addEventListener('click', handleBreadcrumbClick);
    });
}

function showLoading() {
    document.getElementById('loading').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loading').classList.add('hidden');
}

// Event handlers
function handleUniversityFilterChange(e) {
    const code = e.target.value;
    if (e.target.checked) {
        state.selectedUniversities.add(code);
    } else {
        state.selectedUniversities.delete(code);
    }

    // Ensure at least one is selected
    if (state.selectedUniversities.size === 0) {
        e.target.checked = true;
        state.selectedUniversities.add(code);
        alert('Mindestens eine Universität muss ausgewählt sein');
        return;
    }

    log(`Filter: ${state.selectedUniversities.size} unis`);
    renderOverview();
}

function handleBreadcrumbClick(e) {
    const index = parseInt(e.target.dataset.index);
    if (index === 0) {
        document.getElementById('detail-view').classList.remove('active');
        document.getElementById('overview-view').classList.add('active');
        updateBreadcrumb(['Übersicht']);
    }
}

function attachEventListeners() {
    // Select all / deselect all
    document.getElementById('select-all').addEventListener('click', () => {
        Object.keys(state.meta.universities).forEach(code => {
            state.selectedUniversities.add(code);
        });
        renderUniversityFilters();
        renderOverview();
    });

    document.getElementById('deselect-all').addEventListener('click', () => {
        const firstCode = Object.keys(state.meta.universities)[0];
        state.selectedUniversities.clear();
        state.selectedUniversities.add(firstCode);
        renderUniversityFilters();
        renderOverview();
    });

    // Year selector
    document.querySelectorAll('.year-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.year-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.selectedYear = btn.dataset.year;
            renderOverview();
        });
    });

    // Category selector
    document.querySelectorAll('.category-btn').forEach(btn => {
        btn.addEventListener('click', async () => {
            if (btn.disabled) return;

            document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.selectedCategory = btn.dataset.category;
            state.categoryData = null;
            state.sparklineData = null;

            document.getElementById('detail-view').classList.remove('active');
            document.getElementById('overview-view').classList.add('active');
            updateBreadcrumb(['Übersicht']);

            log(`Category: ${state.selectedCategory}`);
            await loadCategoryData(state.selectedCategory);
            renderOverview();
        });
    });

    // Aggregation
    document.querySelectorAll('.agg-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.agg-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            state.aggregationMode = btn.dataset.agg;
            renderOverview();
        });
    });

    // Sort
    document.getElementById('sort-select').addEventListener('change', (e) => {
        state.sortMode = e.target.value;
        log(`Sort: ${state.sortMode}`);
        renderOverview();
    });

    // Export
    document.getElementById('export-csv').addEventListener('click', () => {
        log('Export CSV');
        exportCSV();
    });
    document.getElementById('export-json').addEventListener('click', () => {
        log('Export JSON');
        exportJSON();
    });
}

function exportCSV() {
    const universities = getFilteredUniversities();
    const categoryLabel = state.selectedCategory === 'personal' ? 'Personal (Köpfe)' : 'Ordentliche Studierende';
    let csv = `Universität,Code,${categoryLabel}\n`;

    universities.forEach(code => {
        const name = state.meta.universities[code];
        let value;
        if (state.selectedCategory === 'personal') {
            value = state.summary[code]?.personal_koepfe || 0;
        } else if (state.selectedCategory === 'studierende') {
            value = state.summary[code]?.studierende || 0;
        } else {
            value = 0;
        }
        csv += `"${name}",${code},${value}\n`;
    });

    downloadFile(csv, 'wissensbilanz.csv', 'text/csv;charset=utf-8;');
}

function exportJSON() {
    const universities = getFilteredUniversities();
    const data = {};

    universities.forEach(code => {
        data[code] = {
            name: state.meta.universities[code]
        };

        if (state.selectedCategory === 'personal') {
            data[code].personal_koepfe = state.summary[code]?.personal_koepfe || 0;
        } else if (state.selectedCategory === 'studierende') {
            data[code].studierende = state.summary[code]?.studierende || 0;
        }
    });

    const json = JSON.stringify(data, null, 2);
    downloadFile(json, 'wissensbilanz.json', 'application/json');
}

function downloadFile(content, filename, mimeType) {
    const blob = new Blob(['\ufeff' + content], { type: mimeType });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = filename;
    link.click();
    URL.revokeObjectURL(url);
}

// Start
init();
