import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { finalize } from 'rxjs/operators';
import { DragDropModule, CdkDragDrop, moveItemInArray } from '@angular/cdk/drag-drop';
import { FormsModule } from '@angular/forms';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, HttpClientModule, DragDropModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  previews: string[] = [];
  selectedFiles: File[] = [];
  email: string = '';

  isLoading = false;
  errorMessage = '';

  constructor(private http: HttpClient) {}

  // ======================
  // FILE INPUT
  // ======================

  onFileSelected(event: any) {
    const files = event.target.files;

    this.previews = [];
    this.selectedFiles = [];

    for (let file of files) {
      if (file.type.startsWith('image/')) {
        this.selectedFiles.push(file);
        this.previews.push(URL.createObjectURL(file));
      }
    }
  }

  // ======================
  // DRAG FILES FROM PC
  // ======================

  onFileDragOver(event: Event) {
    event.preventDefault();
  }

  onFileDrop(event: Event) {
    event.preventDefault();

    const dragEvent = event as DragEvent;
    const files = dragEvent.dataTransfer?.files;
    if (!files) return;

    this.previews = [];
    this.selectedFiles = [];

    for (let i = 0; i < files.length; i++) {
      const file = files[i];
      if (file.type.startsWith('image/')) {
        this.selectedFiles.push(file);
        this.previews.push(URL.createObjectURL(file));
      }
    }
  }

  // ======================
  // REORDER IMAGES (CDK)
  // ======================

  drop(event: CdkDragDrop<string[]>) {
    if (event.previousIndex === event.currentIndex) return;

    moveItemInArray(this.previews, event.previousIndex, event.currentIndex);
    moveItemInArray(this.selectedFiles, event.previousIndex, event.currentIndex);
  }

  trackByIndex(index: number): number {
    return index;
  }

  // ======================
  // PDF GENERATION
  // ======================

  generatePDF() {
    if (this.selectedFiles.length === 0) return;

    this.isLoading = true;
    this.errorMessage = '';

    const formData = new FormData();
    this.selectedFiles.forEach(file => {
      formData.append('files', file);
    });

    formData.append('email', this.email);

    const apiUrl = 'http://127.0.0.1:8000/convert';

    this.http.post(apiUrl, formData, { responseType: 'blob' })
      .pipe(finalize(() => this.isLoading = false))
      .subscribe({
        next: (blob: Blob) => {
          const fileURL = window.URL.createObjectURL(blob);
          const link = document.createElement('a');
          link.href = fileURL;
          link.download = 'images.pdf';
          link.click();
          window.URL.revokeObjectURL(fileURL);

          /*this.selectedFiles = [];
          this.previews = [];
          this.email = '';*/
        },
        error: () => {
          this.errorMessage = 'Erreur serveur';
        }
      });
  }

  // ======================
  // REMOVE IMAGE
  // ======================

  removeImage(index: number) {
    this.previews.splice(index, 1);
    this.selectedFiles.splice(index, 1);
  }
}
