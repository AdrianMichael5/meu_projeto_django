describe('Teste de Login', () => {
    it('Deve logar com um usuário existente', () => {
      cy.visit('http://localhost:8000/login/');
  
      cy.get('input[name="username"]').type('usuarioTeste');
      cy.get('input[name="password"]').type('senhaForte123');
  
      cy.get('form').submit();
  
      cy.url().should('include', '/dashboard');
      cy.contains('Bem-vindo à Dashboard');
    });
  });
  