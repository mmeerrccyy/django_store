const slugField = document.getElementById('id_slug');

slugField.addEventListener("change", (e) => {
    const slugValue = e.target.value;

    slugField.classList.remove('is-invalid');

    if (slugValue.length > 0) {
        fetch('/api/validate-slug/', {
            body: JSON.stringify({
                slug: slugValue
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.slug_error) {
                slugField.classList.add('is-invalid')
            }
        })
    }
});

slugField.addEventListener("keyup", (e) => {
    const slugValue = e.target.value;

    slugField.classList.remove('is-invalid');

    if (slugValue.length > 0) {
        fetch('/api/validate-slug/', {
            body: JSON.stringify({
                slug: slugValue
            }),
            method: "POST",
        }).then(res => res.json()).then(data => {
            if (data.slug_error) {
                slugField.classList.add('is-invalid')
            }
        })
    }
});