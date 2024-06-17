const fs = require('fs');
const { importer } = require('@dbml/core');

// read PostgreSQL file script
const mySQL = fs.readFileSync('./schema.sql', 'utf-8');

// generate DBML from PostgreSQL script
const dbml = importer.import(mySQL, 'mysql');

const { exporter } = require('@dbml/core');

const str = exporter.export( dbml, 'dbml' );

fs.writeFileSync('./schema.dbml', str);