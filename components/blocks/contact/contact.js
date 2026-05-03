document.addEventListener('alpine:init', () => {
  Alpine.data('contactForm', () => ({
    formData: {
      name: '',
      email: '',
      message: '',
    },
    status: 'idle',
    errorMessage: '',

    get isLoading() {
      return this.status === 'loading';
    },

    async submitForm() {
      this.errorMessage = '';

      const hcaptchaResponse = hcaptcha.getResponse();
      if (!hcaptchaResponse) {
        this.status = 'error';
        this.errorMessage = 'Please complete the CAPTCHA check.';
        return;
      }

      this.status = 'loading';

      const payload = new FormData();
      payload.append('name', this.formData.name);
      payload.append('email', this.formData.email);
      payload.append('message', this.formData.message);
      payload.append('date', new Date().toISOString());
      payload.append('h-captcha-response', hcaptchaResponse);

      try {
        const response = await fetch('/api/contact/', {
          method: 'POST',
          body: payload
        });

        if (response.ok) {
          this.status = 'success';
        } else {
          const data = await response.json();
          this.status = 'error';
          this.errorMessage = data.detail || 'Failed to send message. Please try again.';
          if (typeof hcaptcha !== 'undefined') hcaptcha.reset();
        }
      } catch (error) {
        this.status = 'error';
        this.errorMessage = 'Network error. Please check your connection and try again.';
        if (typeof hcaptcha !== 'undefined') hcaptcha.reset();
      }
    }
  }));
});
