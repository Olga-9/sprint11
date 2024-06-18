SELECT C.login,
    COUNT(O."courierId")
FROM "Couriers" AS C
LEFT JOIN "Orders" as O On C.id = O."courierId"
WHERE O."inDelivery" = true
GROUP BY C.login,  O."courierId";
