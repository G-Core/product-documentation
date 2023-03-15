module.exports = {
    "extends": "plugin:@angular-eslint/recommended",
    "plugins": [
        "@angular-eslint/eslint-plugin",
        "@angular-eslint/eslint-plugin-template",
    ],
    "rules": {
        "@angular-eslint/component-class-suffix": [
            "error",
            {
                "suffixes": [
                    "Component",
                ],
            },
        ],
        "@angular-eslint/component-max-inline-declarations": "error",
        "@angular-eslint/contextual-lifecycle": "error",
        "@angular-eslint/directive-class-suffix": [
            "error",
            {
                "suffixes": [
                    "Directive",
                ],
            },
        ],
        "@angular-eslint/no-attribute-decorator": "error",
        "@angular-eslint/no-conflicting-lifecycle": "error",
        "@angular-eslint/no-host-metadata-property": "error",
        "@angular-eslint/no-input-rename": "error",
        "@angular-eslint/no-inputs-metadata-property": "error",
        "@angular-eslint/no-lifecycle-call": "error",
        "@angular-eslint/no-output-native": "error",
        "@angular-eslint/no-output-on-prefix": "error",
        "@angular-eslint/no-output-rename": "error",
        "@angular-eslint/no-outputs-metadata-property": "error",
        "@angular-eslint/no-queries-metadata-property": "error",
        "@angular-eslint/use-lifecycle-interface": "error",
        "@angular-eslint/use-pipe-transform-interface": "error"
    },
};
