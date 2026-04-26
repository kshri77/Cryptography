const express = require("express")
const cors = require("cors")

const app = express()

app.use(cors())
app.use(express.json())
app.use(express.static(__dirname))

function powerModSteps(base, exponent, modulus){

    let result = 1
    let steps = []

    for(let i=1;i<=exponent;i++){

        result = (result * base) % modulus

        steps.push(
            `Step ${i}: (${result} * ${base}) mod ${modulus} = ${result}`
        )
    }

    return {result, steps}
}

app.post("/diffie",(req,res)=>{

    let p = parseInt(req.body.p)
    let g = parseInt(req.body.g)
    let a = parseInt(req.body.a)
    let b = parseInt(req.body.b)

    let alicePublic = powerModSteps(g,a,p)
    let bobPublic = powerModSteps(g,b,p)

    let aliceSecret = powerModSteps(bobPublic.result,a,p)
    let bobSecret = powerModSteps(alicePublic.result,b,p)

    res.json({

        A: alicePublic.result,
        B: bobPublic.result,

        alicePublicSteps: alicePublic.steps,
        bobPublicSteps: bobPublic.steps,

        aliceSecretSteps: aliceSecret.steps,
        bobSecretSteps: bobSecret.steps,

        secretAlice: aliceSecret.result,
        secretBob: bobSecret.result
    })
})

app.listen(3000,()=>{
    console.log("Server running on port 3000")
})
