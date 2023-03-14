export interface MenuItem {
    name: string;
    order?: number;
    url: string;
    title?: string;
    children?: Array<MenuItem>;
}

export interface MenuTreeItem {
    order?: number;
    title?: string;
    name: string;
    url: string;
    children: Map<string, MenuTreeItem>;
}
