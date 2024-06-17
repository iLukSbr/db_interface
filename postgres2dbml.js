    const fs = require('fs');
    const { importer, exporter } = require('@dbml/core');

    const postgreSQL = fs.readFileSync('./schema.sql', 'utf-8');

    const dbml = importer.import(postgreSQL, 'postgres');

    const str = exporter.export(dbml, 'dbml');

    fs.writeFileSync('./schema.dbml', str);
