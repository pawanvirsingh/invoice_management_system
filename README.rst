Invoice Management System
=========================

Customers send in their invoices (PDF files) and the Plate IQ system converts the
(unstructured) data from the invoice into a structured format and saves it in an SQL database.
At the minimum, this includes the vendor/seller, the purchaser/buyer, the invoice number and
date, and each line item mentioned in the invoice.


For Running this project :

docker-compose -f local.yml build 
docker-compose -f local.yml up

