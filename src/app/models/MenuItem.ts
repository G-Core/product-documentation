export interface MenuItem {
  name: string;
  url: string;
  children?: MenuItem[];
}

export interface MenuTreeItem {
  name: string;
  url: string;
  children: Map<string, MenuTreeItem>;
}
