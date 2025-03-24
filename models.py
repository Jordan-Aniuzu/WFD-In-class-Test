from django.db import models #PARTC OOP JORDAN ANUZU (B00151878) MODELING

# Create your models here.
#LIST OF ALL NEEDED FOR BELOW: 
#1. CAR
#2. CUSTOMER
#4. SALES PERSON
#3. SALES INVOIC
#5. MECHANIC
#6. SERVICE TICKET
#7. SERVICE MECHANIC
#8. SERVIE
#9. PART
#10. PARTS USED



class Car(models.Model): #CREATING A CAR CLASS
    SerialNumber = models.CharField(max_length=100)
    Make = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Colour = models.CharField(max_length=100)
    Year = models.IntegerField()
    CarforSale = models.BooleanField()




class Customer(models.Model): #CREATING A CUSTOMER CLASS
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    PhoneNumber = models.CharField(max_length=100)
    Address = models.TextField()
    City = models.CharField(max_length=100)
    StateProvince = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    PostalCode = models.CharField(max_length=20)




class Salesperson(models.Model): #CREATING A SALESPERSON CLASS
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)



class SalesInvoice(models.Model): #CREATING A SALES INVOICE CLASS
    Invoice_Number = models.CharField(max_length=100)
    Date = models.DateField()
    CarID = models.ForeignKey(Car)
    CustomerID = models.ForeignKey(Customer)
    SalespersonID = models.ForeignKey(Salesperson)




class Mechanic(models.Model): #CREATING A MECHANIC CLASS
    LastName = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)

class ServiceTicket(models.Model):#CREATING A SERVICE TICKET CLASS
    ServiceTicketNumber = models.CharField(max_length=100)
    CarID = models.ForeignKey(Car)
    CustomerID = models.ForeignKey(Customer)
    DateReceived = models.DateField()
    Comments = models.TextField()
    DateReturnedtoCustomer = models.DateField(null=True, blank=True)



class ServiceMechanic(models.Model): #CREATING A SERVICE MECHANIC CLASS
    ServiceTicketID = models.ForeignKey(ServiceTicket)
    ServiceID = models.ForeignKey()
    MechanicID = models.ForeignKey(Mechanic)
    Hours = models.FloatField()
    Comment = models.TextField()
    Rate = models.FloatField()




class Service(models.Model): #CREATING A SERVICE CLASS
    ServiceName = models.CharField(max_length=100)
    HourlyRate = models.FloatField()



class Part(models.Model): #CREATNG A PART CLASS
    PartNumber = models.CharField(max_length=100)
    Description = models.TextField()
    PurchasePrice = models.FloatField()
    RetailPrice = models.FloatField()



class PartsUsed(models.Model): #CREATING A PARTS USED CLASS
    Part = models.ForeignKey(Part)
    ServiceTicket = models.ForeignKey(ServiceTicket)
    NumberUsed = models.IntegerField()
    Price = models.FloatField()

    


