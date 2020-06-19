const express = require('express')
const fs = require('fs')
const app = express()
const bodyParser = require('body-parser')
const port = 3000


app.use(bodyParser.json())
app.use(express.static('public'))
app.use('/scor' , express.urlencoded({extended:true}))
app.listen(port , () => console.log("Aplicatia a pornit"))
app.post('/scor' , function(req,res) {
    var date = fs.readFileSync('scor.json')
    var ob = JSON.parse(date)
    ob.push(req.body)
    fs.writeFileSync('scor.json', JSON.stringify(ob))
    // res.send('merge')
    // console.log("nush daca merge")
})

app.get('/get' , function(req,res) {
    
    var date = fs.readFileSync("scor.json")
    
    var ob = JSON.parse(date)
    console.log(ob.length)
    /*console.log("Datele sunt:\n")
    console.log(ob)*/
    res.send(ob)
    // console.log("Datele au fost trimise")
    
})
