This PR is to initiate Bengali localization based on </br>
- Issue to https://github.com/cncf/glossary/issues/339
- https://github.com/cncf/glossary/blob/main/LOCALIZATION.md guide 
</br>

Base and target branch of this PR is dev-bn which is development branch for Bengali localization.


This PR includes

- [languages.bn] section in config.toml
- content/bn/ directory
- i18n/bn.toml
- Some translated documents
    - Main page
        - content/bn/_index.md
    - Terms
        - "Cloud Native Technology": content/bn/cloud_native_tech.md
    - Others</br>
        - contribute: content/bn/contribute/_index.md (partially localized)
        - style-guide: content/bn/style-guide/_index.md (partially localized)</br>

Since Bengali localization team owns content/bn/*  only,
this PR will require approvals from upstream owners (maintainers).