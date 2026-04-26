const express = require("express")
const cors = require("cors")

const app = express()

app.use(cors())
app.use(express.json())
app.use(express.static(__dirname))

// GCD
function gcd(a,b){

    let steps=[]

    while(b!=0){

        steps.push(`${a} mod ${b} = ${a%b}`)

        let temp=b
        b=a%b
        a=temp
    }

    return {value:a,steps:steps}
}

// Modular inverse
function modInverse(e,phi){

    let t=0,newT=1
    let r=phi,newR=e

    let steps=[]

    while(newR!=0){

        let q=Math.floor(r/newR)

        steps.push(`q = ${r}/${newR} = ${q}`)

        let tempT=newT
        newT=t-q*newT
        t=tempT

        let tempR=newR
        newR=r-q*newR
        r=tempR
    }

    if(t<0)
        t+=phi

    return {value:t,steps:steps}
}

// Modular exponent
function powerMod(base,exp,mod){

    let result=1
    let steps=[]

    for(let i=1;i<=exp;i++){

        result=(result*base)%mod

        steps.push(`Step ${i}: (${result} × ${base}) mod ${mod} = ${result}`)
    }

    return {value:result,steps:steps}
}

app.post("/rsa",(req,res)=>{

    let p=parseInt(req.body.p)
    let q=parseInt(req.body.q)
    let e=parseInt(req.body.e)
    let m=parseInt(req.body.m)

    let n=p*q
    let phi=(p-1)*(q-1)

    let gcdResult=gcd(e,phi)

    let inverseResult=modInverse(e,phi)
    let d=inverseResult.value

    let encrypt=powerMod(m,e,n)
    let cipher=encrypt.value

    let decrypt=powerMod(cipher,d,n)
    let decrypted=decrypt.value

    res.json({

        n:n,
        phi:phi,

        gcdValue:gcdResult.value,
        gcdSteps:gcdResult.steps,

        d:d,
        inverseSteps:inverseResult.steps,

        cipher:cipher,
        encryptSteps:encrypt.steps,

        decrypted:decrypted,
        decryptSteps:decrypt.steps

    })

})

app.listen(3000,()=>{
    console.log("Server running on port 3000")
})
