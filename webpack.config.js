const envsubst = require('@tuplo/envsubst');
const path = require('path');

module.exports = {
    optimization: {
        splitChunks: {
            cacheGroups: {
                config: {
                    name: 'config',
                    filename: 'config.js',
                    chunks: 'all',
                    test: (module) => module.resource?.includes('/src/config.ts'),
                    enforce: true,
                },
            },
        },
    },
    devServer: {
        setupMiddlewares: (middlewares, devServer) => {
            devServer.app.get('/config.js', (req, res) => {
                const { outputPath, outputFileSystem: fs } = devServer.compiler;
                const rawFile = fs.readFileSync(path.resolve(outputPath, 'config.js'), {
                    encoding: 'utf8',
                });
                const substituted = envsubst(rawFile);
                res.type('application/javascript').send(substituted);
            });

            return middlewares;
        },
    },
};
