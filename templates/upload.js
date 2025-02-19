const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://Abhishek98:abhishek@hotelbooking.9thwb.gcp.mongodb.net/HostelBooking?retryWrites=true&w=majority',{useNewUrlParser:true});
var conn = mongoose.Collection;

var uploadSchema = new mongoose.Schema({
    
})