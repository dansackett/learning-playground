module.exports = {
    // Load Mock Product Data Into localStorage
    init: function() {
        localStorage.clear();
        localStorage.setItem('product', JSON.stringify([
            {
                id: '0011001',
                name: 'Product',
                image: 'dist/img/beer.png',
                description: 'My product is amazing!',
                variants: [
                    {
                        sku: '123123',
                        type: 'Option 1',
                        price: 4.99,
                        inventory: 1

                    },
                    {
                        sku: '123124',
                        type: 'Option 2',
                        price: 12.99,
                        inventory: 5
                    },
                    {
                        sku: '1231235',
                        type: 'Option 3',
                        price: 19.99,
                        inventory: 3
                    }
                ]
            }
        ]));
    }
};
