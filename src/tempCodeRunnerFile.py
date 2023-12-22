
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    self.pause = False

    def load_states(self):
        self.logo = LogoState(self)
        self.state_stack.append(self.logo)
