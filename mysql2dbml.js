const fs = require('fs')
const { importer, exporter } = require('@dbml/core')

try{
    // read PostgreSQL file script
    const mySQL = fs.readFileSync('./schema.sql', 'utf-8')

    // generate DBML from PostgreSQL script
    const dbml = importer.import(mySQL, 'mysql')


    const str = exporter.export( dbml, 'dbml' )

    fs.writeFileSync('./schema.dbml', str)
}catch(err){
    console.log(err)
}