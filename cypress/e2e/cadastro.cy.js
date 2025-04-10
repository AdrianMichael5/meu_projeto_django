describe('Teste de Cadastro', () => {
    it('Deve cadastrar um novo usuário com sucesso', () => {
      cy.visit('http://localhost:8000/cadastro/');
  
      cy.get('input[name="username"]').type('usuarioTeste');
      cy.get('input[name="email"]').type('usuario@teste.com');
      cy.get('input[name="password"]').type('senhaForte123');
  
      cy.get('form').submit();
  
      cy.url().should('include', '/dashboard');
      cy.contains('Bem-vindo à Dashboard');
    });
  });
  