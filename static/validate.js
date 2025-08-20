document.addEventListener('DOMContentLoaded', function() {
    // Details form 
    const detailsForm = document.querySelector('form[action="/details"]');
    if (detailsForm) {
        detailsForm.addEventListener('submit', function(e) {
            let valid = true;
            if (!detailsForm.first_name.value.trim()) valid = false;
            if (!detailsForm.last_name.value.trim()) valid = false;
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(detailsForm.email.value.trim())) valid = false;
            if (!detailsForm.dob.value) valid = false;
            if (!detailsForm.gender.value) valid = false;
            if (!detailsForm.phoneno.value.trim() || !/^\d{10}$/.test(detailsForm.phoneno.value.trim())) valid = false;
            if (!detailsForm.city.value.trim() || detailsForm.city.value.length > 50) valid = false;
            if (!detailsForm.state.value.trim() || detailsForm.state.value.length > 50) valid = false;

            if (!valid) {
                alert('Please fill all required fields correctly.');
                e.preventDefault();
            }
        });
    }

    // Education form 
    const eduForm = document.querySelector('form[action="/edu"]');
    if (eduForm) {
        eduForm.addEventListener('submit', function(e) {
            let valid = true;
            if (!eduForm.degree.value.trim()) valid = false;
            if (!eduForm.institution.value.trim()) valid = false;
            const cgpa = parseFloat(eduForm.cgpa.value);
            if (isNaN(cgpa) || cgpa < 0 || cgpa > 10) valid = false;
            const ys = parseInt(eduForm.year_started.value, 10);
            if (isNaN(ys) || ys < 1900 || ys > 2100) valid = false;
            const yg = parseInt(eduForm.year_graduated.value, 10);
            if (isNaN(yg) || yg < 1900 || yg > 2100 || yg < ys) valid = false;
            if (!valid) {
                alert('Please fill all required fields correctly.');
                e.preventDefault();
            }
        });
    }
});