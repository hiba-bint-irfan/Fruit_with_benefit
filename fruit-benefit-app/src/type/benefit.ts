export interface Fruit {
  name: string;
  keyBenefits: {
    title: string;
    description: string;
  }[];
  moreBenefits?: string[];
  id?: string;
}
