function handleButtonClick() {
    const searchValue = document.querySelector('.search-box').value;

    fetch("{% url 'handle_button' %}", {
        method: 'POST',
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ search: searchValue })
    })
    .then(response => response.json())
    .then(data => {
        const productContainer = document.querySelector('.product-container');
        productContainer.innerHTML = ''; // Clear the product container before adding new items

        data.products.forEach(product => {
            const productItem = `
                <div class="product-item">
                    <img src="${product.image}" alt="${product.productDisplayName}">
                    <div class="product-details">
                        <h2>${product.productDisplayName}</h2>
                        <p>Article Number: ${product.articleNumber}</p>
                        <p>Type: ${product.articleType}</p>
                        <p>Category: ${product.masterCategory} > ${product.subCategory}</p>
                        <p>Gender: ${product.gender}</p>
                        <p>Colour: ${product.baseColour}</p>
                        <p>Season: ${product.season} - Year: ${product.year}</p>
                        <p>Usage: ${product.usag}</p>
                        <div class="product-price">
                            <span class="price">$${product.price}</span>
                            ${product.on_sale ? `<span class="sale-tag">Sale</span>` : ''}
                        </div>
                    </div>
                </div>
            `;
            productContainer.innerHTML += productItem; // Add each product to the container
        });
    })
    .catch(error => console.error('Error:', error));
}
export { handleButtonClick };