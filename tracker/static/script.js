document.addEventListener("DOMContentLoaded", function() {
    // --- 1. Tarih Kısıtlaması Ayarları ---
    const today = new Date().toISOString().split('T')[0];
    
    // Index sayfası için tarih inputu ayarı
    const dateInput = document.getElementById('dateInput');
    if (dateInput) {
        dateInput.setAttribute('max', today);
        dateInput.value = today;
    }

    // Edit sayfası için tarih inputu ayarı
    const editDateInput = document.getElementById('editDateInput');
    if (editDateInput) {
        editDateInput.setAttribute('max', today);
    }
});

// --- 2. Formu Aç/Kapat (Toggle) Fonksiyonu ---
function toggleForm() {
    const form = document.getElementById("transactionForm");
    if (form) {
        if (form.classList.contains("hidden")) {
            form.classList.remove("hidden");
        } else {
            form.classList.add("hidden");
        }
    }
}