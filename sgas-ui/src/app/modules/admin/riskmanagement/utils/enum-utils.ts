// utils/enum-utils.ts
export function enumToArray(enumObj: any): { key: string; value: string }[] {
    return Object.entries(enumObj).map(([key, value]) => ({ key, value: value as string }));
  }
  