hola = {
  id: "9E499902CG860320A",
  intent: "CAPTURE",
  status: "COMPLETED",
  purchase_units: [
    {
      reference_id: "default",
      amount: { currency_code: "USD", value: "2.00" },
      payee: {
        email_address: "sb-jlwkj33302142@business.example.com",
        merchant_id: "NKJ6FPSDA9BSS",
      },
      shipping: {
        name: { full_name: "John Doe" },
        address: {
          address_line_1: "Free Trade Zone",
          admin_area_2: "Bogota",
          admin_area_1: "Bogota",
          postal_code: "110111",
          country_code: "CO",
        },
      },
      payments: {
        captures: [
          {
            id: "79T648331D514605P",
            status: "COMPLETED",
            amount: { currency_code: "USD", value: "2.00" },
            final_capture: True,
            seller_protection: {
              status: "ELIGIBLE",
              dispute_categories: [
                "ITEM_NOT_RECEIVED",
                "UNAUTHORIZED_TRANSACTION",
              ],
            },
            create_time: "2024-10-12T01:17:18Z",
            update_time: "2024-10-12T01:17:18Z",
          },
        ],
      },
    },
  ],
  payer: {
    name: { given_name: "John", surname: "Doe" },
    email_address: "sb-dfz8s33308430@personal.example.com",
    payer_id: "6M97SN2TMDJTS",
    address: { country_code: "CO" },
  },
  create_time: "2024-10-12T01:16:10Z",
  update_time: "2024-10-12T01:17:18Z",
  links: [
    {
      href: "https://api.sandbox.paypal.com/v2/checkout/orders/9E499902CG860320A",
      rel: "self",
      method: "GET",
    },
  ],
};
