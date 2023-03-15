module.exports = {
    plugins: ['prettier'],
    extends: ['plugin:prettier/recommended'],
    rules: {
        'prettier/prettier': 'error',
        "lines-around-comment": ["warn", { "beforeBlockComment": true, "allowBlockStart": true }]
    },
};
