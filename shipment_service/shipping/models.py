from djongo import models

class Product(models.Model):
    id = models.ObjectIdField(db_column="_id", primary_key=True)
    ProductID = models.IntegerField()
    ProductName = models.CharField(max_length=255)
    BrandName = models.CharField(max_length=100)
    ProductSize = models.CharField(max_length=50)
    Category = models.CharField(max_length=100)
    MRP = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()

    class Meta:
        db_table = 'products'





class Shipment(models.Model):
    id = models.ObjectIdField(db_column="_id", primary_key=True)
    destination = models.CharField(max_length=255, null=True, blank=True)
    confirmedOn = models.DateTimeField(null=True, blank=True)
    purchase_orders = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Shipment #{self.id}"
    
    class Meta:
        db_table = 'shipments'



class POS(models.Model):
    id = models.ObjectIdField(db_column="_id", primary_key=True)
    poID = models.IntegerField()
    source = models.CharField(max_length=255)
    createdOn = models.DateTimeField()
    products = models.JSONField()
    shipment = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    READY_FOR_SHIPMENT = 'Ready for Shipment'
    ADDED_TO_SHIPMENT = 'Added to Shipment'
    IN_TRANSPORT = 'In Transport'
    STATUS_CHOICES = [
        (READY_FOR_SHIPMENT, 'Ready for Shipment'),
        (ADDED_TO_SHIPMENT, 'Added to Shipment'),
        (IN_TRANSPORT, 'In Transport'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=READY_FOR_SHIPMENT)

    def __str__(self):
        return f"Purchase Order #{self.poID} - Status: {self.status}"
    class Meta:
        db_table = 'pos'