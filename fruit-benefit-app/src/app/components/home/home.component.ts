import { Component, inject } from '@angular/core';
import { FormsModule, NgModel } from '@angular/forms';
import {MatFormFieldModule} from '@angular/material/form-field';
import { BenefitComponent } from '../benefit/benefit.component';
import { BenefitsService } from '../../benefits.service';
import { Fruit } from '../../../type/benefit';
import { NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [FormsModule, MatFormFieldModule,NgIf, BenefitComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  inputMode: 'name' | 'image' = 'name';
  selectedFruit: string = ''; 
  showBenefits: boolean = false; 
  predictedClass: string | null = null;
  selectedImage: File | null = null;
  Benefitservice=inject(BenefitsService)

  setInputMode(mode: 'name' | 'image'): void {
    this.inputMode = mode;
    this.resetState();
  }
  resetState(): void {
    this.selectedFruit = '';
    this.selectedImage = null;
    this.showBenefits = false;
  }
   // Handle image selection
   onImageSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input?.files?.length) {
      this.selectedImage = input.files[0];
    }
  }

  // Call the service to predict the fruit based on selected image
  predictfruit() {
    if (this.selectedImage) {
      this.Benefitservice.predictFruit(this.selectedImage).subscribe(
        result => {
          console.log(result);
          this.selectedFruit = result.predicted_class; // Assuming 'predicted_class' is in the response
          this.showBenefits = true; // Show benefits if prediction is successful
        },
        error => {
          console.error('Error predicting fruit:', error);
          this.selectedFruit = ''; // Reset prediction on error
          this.showBenefits = false;
        }
      );
    } else {
      alert('Please upload an image first!');
    }
  }

  onSubmit(): void {
    if (this.inputMode === 'name' && this.selectedFruit.trim()) {
      this.showBenefits = true;
    } else if (this.inputMode === 'image' && this.selectedImage) {
      this.predictfruit()
      
    } else {
      alert('Please provide a valid input!');
    }
  }
  
  // fruitName: string = '';
  
 



}
